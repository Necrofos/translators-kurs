import ast

from .runtime import ReturnSignal, Scope, UserFunction
from .generated.SimplePythonParser import SimplePythonParser
from .generated.SimplePythonParserVisitor import SimplePythonParserVisitor


class Interpreter(SimplePythonParserVisitor):
    def __init__(self, output_stream=None):
        self.globals = Scope()
        self.scope = self.globals
        self.output_stream = output_stream

    def execute(self, tree):
        return self.visit(tree)

    def _write_output(self, value):
        if self.output_stream is None:
            print(value, end="")
        else:
            self.output_stream.write(value)

    def _default_value(self, type_name):
        if type_name == "bool":
            return False
        if type_name == "char*":
            return ""
        return 0

    def _format_printf(self, arguments):
        if not arguments:
            return ""

        def stringify(value, placeholder=None):
            if placeholder == "%d" and isinstance(value, bool):
                return str(int(value))
            return str(value)

        first = arguments[0]
        if isinstance(first, str) and len(arguments) > 1:
            result = first
            for value in arguments[1:]:
                for placeholder in ("%d", "%s", "%c"):
                    if placeholder in result:
                        result = result.replace(placeholder, stringify(value, placeholder), 1)
                        break
                else:
                    result += stringify(value)
            return result

        return " ".join(stringify(value) for value in arguments)

    def visitProgram(self, ctx):
        for declaration in ctx.declaration():
            self.visit(declaration)
        return None

    def visitDeclaration(self, ctx):
        if ctx.functionDefinition():
            return self.visit(ctx.functionDefinition())
        return self.visit(ctx.statement())

    def visitBlock(self, ctx):
        previous_scope = self.scope
        self.scope = Scope(parent=previous_scope)
        try:
            for statement in ctx.statement():
                self.visit(statement)
        finally:
            self.scope = previous_scope
        return None

    def visitStatement(self, ctx):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.printfStatement():
            return self.visit(ctx.printfStatement())
        if ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        if ctx.expressionStatement():
            return self.visit(ctx.expressionStatement())
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        if ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        return self.visit(ctx.block())

    def visitVariableDeclaration(self, ctx):
        type_name = self.visit(ctx.typeSpecifier())
        value = self._default_value(type_name)
        if ctx.expression():
            value = self.visit(ctx.expression())
        self.scope.declare(ctx.NAME().getText(), value)
        return value

    def visitAssignment(self, ctx):
        name = ctx.NAME().getText()
        value = self.visit(ctx.expression())
        self.scope.assign(name, value)
        return value

    def visitPrintfStatement(self, ctx):
        values = []
        if ctx.argumentList():
            for expression in ctx.argumentList().expression():
                values.append(self.visit(expression))
        self._write_output(self._format_printf(values))
        return None

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expression()) if ctx.expression() else None
        raise ReturnSignal(value)

    def visitExpressionStatement(self, ctx):
        return self.visit(ctx.expression())

    def visitIfStatement(self, ctx):
        blocks = ctx.block()
        if self.visit(ctx.expression()):
            return self.visit(blocks[0])
        if len(blocks) > 1:
            return self.visit(blocks[1])
        return None

    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())
        return None

    def visitFunctionDefinition(self, ctx):
        name = ctx.NAME().getText()
        return_type = self.visit(ctx.functionReturnType())
        params = []
        if ctx.parameterList():
            params = [self.visit(parameter) for parameter in ctx.parameterList().parameter()]
        function = UserFunction(name, return_type, params, ctx.block(), self.scope)
        self.scope.declare(name, function)
        return function

    def visitFunctionReturnType(self, ctx):
        if ctx.VOID():
            return "void"
        return "int"

    def visitTypeSpecifier(self, ctx):
        return ctx.getText().replace(" ", "")

    def visitParameter(self, ctx):
        return {
            "type": self.visit(ctx.typeSpecifier()),
            "name": ctx.NAME().getText(),
        }

    def visitOrExpression(self, ctx):
        values = ctx.andExpression()
        result = self.visit(values[0])
        for expression in values[1:]:
            result = result or self.visit(expression)
        return result

    def visitAndExpression(self, ctx):
        values = ctx.notExpression()
        result = self.visit(values[0])
        for expression in values[1:]:
            result = result and self.visit(expression)
        return result

    def visitNotExpression(self, ctx):
        if ctx.NOT():
            return not self.visit(ctx.notExpression())
        return self.visit(ctx.comparison())

    def visitComparison(self, ctx):
        values = ctx.additiveExpression()
        result = self.visit(values[0])

        for index, operator in enumerate(ctx.children[1::2], start=1):
            right = self.visit(values[index])
            operator_text = operator.getText()

            if operator_text == "==":
                comparison_ok = result == right
            elif operator_text == "!=":
                comparison_ok = result != right
            elif operator_text == "<":
                comparison_ok = result < right
            elif operator_text == ">":
                comparison_ok = result > right
            elif operator_text == "<=":
                comparison_ok = result <= right
            else:
                comparison_ok = result >= right

            if not comparison_ok:
                return False

            result = right

        return True if len(values) > 1 else result

    def visitAdditiveExpression(self, ctx):
        result = self.visit(ctx.multiplicativeExpression(0))

        for index in range(1, len(ctx.multiplicativeExpression())):
            right = self.visit(ctx.multiplicativeExpression(index))
            operator = ctx.getChild(2 * index - 1).getText()
            if operator == "+":
                result = result + right
            else:
                result = result - right

        return result

    def visitMultiplicativeExpression(self, ctx):
        result = self.visit(ctx.unaryExpression(0))

        for index in range(1, len(ctx.unaryExpression())):
            right = self.visit(ctx.unaryExpression(index))
            operator = ctx.getChild(2 * index - 1).getText()
            if operator == "*":
                result = result * right
            elif operator == "/":
                result = int(result / right)
            else:
                result = result % right

        return result

    def visitUnaryExpression(self, ctx):
        if ctx.MINUS():
            return -self.visit(ctx.unaryExpression())
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        if ctx.NAME():
            return self.scope.get(ctx.NAME().getText())
        return self.visit(ctx.expression())

    def visitFunctionCall(self, ctx):
        function_name = ctx.NAME().getText()
        arguments = []
        if ctx.argumentList():
            arguments = [self.visit(expression) for expression in ctx.argumentList().expression()]

        if function_name == "printf":
            self._write_output(self._format_printf(arguments))
            return None

        function = self.scope.get(function_name)
        if not isinstance(function, UserFunction):
            raise TypeError(f"'{function_name}' is not callable")

        return function.call(self, arguments)

    def visitLiteral(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        if ctx.STRING():
            return ast.literal_eval(ctx.STRING().getText())
        return ctx.TRUE() is not None
