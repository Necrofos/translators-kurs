from antlr4 import CommonTokenStream, FileStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from .generated.SimplePythonLexer import SimplePythonLexer
from .generated.SimplePythonParser import SimplePythonParser
from .interpreter import Interpreter


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")


def parse_source(source_text):
    input_stream = InputStream(source_text)
    lexer = SimplePythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimplePythonParser(token_stream)

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()
    if error_listener.errors:
        raise SyntaxError("\n".join(error_listener.errors))

    return tree


def run_source(source_text, output_stream=None):
    tree = parse_source(source_text)
    interpreter = Interpreter(output_stream=output_stream)
    interpreter.execute(tree)


def run_file(path, output_stream=None):
    source_text = FileStream(path, encoding="utf-8").strdata
    run_source(source_text, output_stream=output_stream)

