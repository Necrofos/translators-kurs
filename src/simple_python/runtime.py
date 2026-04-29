class ReturnSignal(Exception):
    def __init__(self, value):
        super().__init__("function returned")
        self.value = value


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def declare(self, name, value):
        if name in self.values:
            raise NameError(f"Name '{name}' is already declared")
        self.values[name] = value

    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
            return

        if self.parent is not None:
            self.parent.assign(name, value)
            return

        self.values[name] = value

    def get(self, name):
        if name in self.values:
            return self.values[name]

        if self.parent is not None:
            return self.parent.get(name)

        raise NameError(f"Name '{name}' is not defined")


class UserFunction:
    def __init__(self, name, return_type, params, block, closure):
        self.name = name
        self.return_type = return_type
        self.params = params
        self.block = block
        self.closure = closure

    def call(self, interpreter, arguments):
        if len(arguments) != len(self.params):
            raise TypeError(
                f"Function '{self.name}' expected {len(self.params)} arguments, "
                f"got {len(arguments)}"
            )

        call_scope = Scope(parent=self.closure)
        for param, argument in zip(self.params, arguments):
            call_scope.define(param["name"], argument)

        previous_scope = interpreter.scope
        interpreter.scope = call_scope

        try:
            interpreter.visit(self.block)
        except ReturnSignal as signal:
            return signal.value
        finally:
            interpreter.scope = previous_scope

        return None
