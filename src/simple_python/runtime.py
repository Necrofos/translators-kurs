class ReturnSignal(Exception):
    def __init__(self, value):
        super().__init__("function returned")
        self.value = value


class StructDefinition:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.field_names = {field["name"] for field in fields}

    def has_field(self, name):
        return name in self.field_names


class StructInstance:
    def __init__(self, definition, values):
        self.definition = definition
        self.values = values

    def copy(self):
        return StructInstance(
            self.definition,
            {name: copy_value(value) for name, value in self.values.items()},
        )

    def get_field(self, name):
        if not self.definition.has_field(name):
            raise AttributeError(f"Struct '{self.definition.name}' has no field '{name}'")
        return self.values[name]

    def set_field(self, name, value):
        if not self.definition.has_field(name):
            raise AttributeError(f"Struct '{self.definition.name}' has no field '{name}'")
        self.values[name] = copy_value(value)

    def __str__(self):
        fields = ", ".join(f"{name}={value}" for name, value in self.values.items())
        return f"{self.definition.name}{{{fields}}}"

    def __eq__(self, other):
        return (
            isinstance(other, StructInstance)
            and self.definition.name == other.definition.name
            and self.values == other.values
        )


def copy_value(value):
    if isinstance(value, StructInstance):
        return value.copy()
    return value


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
            call_scope.define(param["name"], copy_value(argument))

        previous_scope = interpreter.scope
        interpreter.scope = call_scope

        try:
            interpreter.visit(self.block)
        except ReturnSignal as signal:
            return copy_value(signal.value)
        finally:
            interpreter.scope = previous_scope

        return None
