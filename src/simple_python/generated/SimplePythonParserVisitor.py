# Generated from grammar/SimplePythonParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimplePythonParser import SimplePythonParser
else:
    from SimplePythonParser import SimplePythonParser

# This class defines a complete generic visitor for a parse tree produced by SimplePythonParser.

class SimplePythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimplePythonParser#program.
    def visitProgram(self, ctx:SimplePythonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#declaration.
    def visitDeclaration(self, ctx:SimplePythonParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#statement.
    def visitStatement(self, ctx:SimplePythonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SimplePythonParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#assignment.
    def visitAssignment(self, ctx:SimplePythonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#printfStatement.
    def visitPrintfStatement(self, ctx:SimplePythonParser.PrintfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#returnStatement.
    def visitReturnStatement(self, ctx:SimplePythonParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#expressionStatement.
    def visitExpressionStatement(self, ctx:SimplePythonParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#ifStatement.
    def visitIfStatement(self, ctx:SimplePythonParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#whileStatement.
    def visitWhileStatement(self, ctx:SimplePythonParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:SimplePythonParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#functionReturnType.
    def visitFunctionReturnType(self, ctx:SimplePythonParser.FunctionReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:SimplePythonParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#structDefinition.
    def visitStructDefinition(self, ctx:SimplePythonParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#structFieldDeclaration.
    def visitStructFieldDeclaration(self, ctx:SimplePythonParser.StructFieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#parameterList.
    def visitParameterList(self, ctx:SimplePythonParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#parameter.
    def visitParameter(self, ctx:SimplePythonParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#argumentList.
    def visitArgumentList(self, ctx:SimplePythonParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#block.
    def visitBlock(self, ctx:SimplePythonParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#expression.
    def visitExpression(self, ctx:SimplePythonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#orExpression.
    def visitOrExpression(self, ctx:SimplePythonParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#andExpression.
    def visitAndExpression(self, ctx:SimplePythonParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#notExpression.
    def visitNotExpression(self, ctx:SimplePythonParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#comparison.
    def visitComparison(self, ctx:SimplePythonParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:SimplePythonParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SimplePythonParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#unaryExpression.
    def visitUnaryExpression(self, ctx:SimplePythonParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#primary.
    def visitPrimary(self, ctx:SimplePythonParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#functionCall.
    def visitFunctionCall(self, ctx:SimplePythonParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#fieldAccess.
    def visitFieldAccess(self, ctx:SimplePythonParser.FieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#assignmentTarget.
    def visitAssignmentTarget(self, ctx:SimplePythonParser.AssignmentTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePythonParser#literal.
    def visitLiteral(self, ctx:SimplePythonParser.LiteralContext):
        return self.visitChildren(ctx)



del SimplePythonParser