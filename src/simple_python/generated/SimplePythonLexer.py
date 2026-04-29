# Generated from grammar/SimplePythonLexer.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u00f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\7\4_\n\4\f\4\16\4b\13\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\7\"\u00c4\n\"\f\"")
        buf.write("\16\"\u00c7\13\"\3#\6#\u00ca\n#\r#\16#\u00cb\3$\3$\3$")
        buf.write("\3$\7$\u00d2\n$\f$\16$\u00d5\13$\3$\3$\3%\3%\3%\3%\7%")
        buf.write("\u00dd\n%\f%\16%\u00e0\13%\3%\3%\3&\3&\3&\3&\7&\u00e8")
        buf.write("\n&\f&\16&\u00eb\13&\3&\3&\3&\3&\3&\3\'\6\'\u00f3\n\'")
        buf.write("\r\'\16\'\u00f4\3\'\3\'\3\u00e9\2(\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(\3\2\t\4\2\13\13\"\"")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\6\2\f\f\17\17$$^^\4")
        buf.write("\2\f\f\17\17\5\2\13\f\17\17\"\"\2\u00ff\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\3O\3\2\2\2\5S\3\2\2\2\7X\3\2\2\2\te\3\2\2\2\13")
        buf.write("j\3\2\2\2\rq\3\2\2\2\17t\3\2\2\2\21y\3\2\2\2\23\177\3")
        buf.write("\2\2\2\25\u0086\3\2\2\2\27\u008b\3\2\2\2\31\u0091\3\2")
        buf.write("\2\2\33\u0094\3\2\2\2\35\u0097\3\2\2\2\37\u009a\3\2\2")
        buf.write("\2!\u009d\3\2\2\2#\u00a0\3\2\2\2%\u00a3\3\2\2\2\'\u00a5")
        buf.write("\3\2\2\2)\u00a7\3\2\2\2+\u00a9\3\2\2\2-\u00ab\3\2\2\2")
        buf.write("/\u00ad\3\2\2\2\61\u00af\3\2\2\2\63\u00b1\3\2\2\2\65\u00b3")
        buf.write("\3\2\2\2\67\u00b5\3\2\2\29\u00b7\3\2\2\2;\u00b9\3\2\2")
        buf.write("\2=\u00bb\3\2\2\2?\u00bd\3\2\2\2A\u00bf\3\2\2\2C\u00c1")
        buf.write("\3\2\2\2E\u00c9\3\2\2\2G\u00cd\3\2\2\2I\u00d8\3\2\2\2")
        buf.write("K\u00e3\3\2\2\2M\u00f2\3\2\2\2OP\7k\2\2PQ\7p\2\2QR\7v")
        buf.write("\2\2R\4\3\2\2\2ST\7d\2\2TU\7q\2\2UV\7q\2\2VW\7n\2\2W\6")
        buf.write("\3\2\2\2XY\7e\2\2YZ\7j\2\2Z[\7c\2\2[\\\7t\2\2\\`\3\2\2")
        buf.write("\2]_\t\2\2\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a")
        buf.write("c\3\2\2\2b`\3\2\2\2cd\7,\2\2d\b\3\2\2\2ef\7x\2\2fg\7q")
        buf.write("\2\2gh\7k\2\2hi\7f\2\2i\n\3\2\2\2jk\7t\2\2kl\7g\2\2lm")
        buf.write("\7v\2\2mn\7w\2\2no\7t\2\2op\7p\2\2p\f\3\2\2\2qr\7k\2\2")
        buf.write("rs\7h\2\2s\16\3\2\2\2tu\7g\2\2uv\7n\2\2vw\7u\2\2wx\7g")
        buf.write("\2\2x\20\3\2\2\2yz\7y\2\2z{\7j\2\2{|\7k\2\2|}\7n\2\2}")
        buf.write("~\7g\2\2~\22\3\2\2\2\177\u0080\7r\2\2\u0080\u0081\7t\2")
        buf.write("\2\u0081\u0082\7k\2\2\u0082\u0083\7p\2\2\u0083\u0084\7")
        buf.write("v\2\2\u0084\u0085\7h\2\2\u0085\24\3\2\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7t\2\2\u0088\u0089\7w\2\2\u0089\u008a")
        buf.write("\7g\2\2\u008a\26\3\2\2\2\u008b\u008c\7h\2\2\u008c\u008d")
        buf.write("\7c\2\2\u008d\u008e\7n\2\2\u008e\u008f\7u\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\30\3\2\2\2\u0091\u0092\7(\2\2\u0092\u0093")
        buf.write("\7(\2\2\u0093\32\3\2\2\2\u0094\u0095\7~\2\2\u0095\u0096")
        buf.write("\7~\2\2\u0096\34\3\2\2\2\u0097\u0098\7?\2\2\u0098\u0099")
        buf.write("\7?\2\2\u0099\36\3\2\2\2\u009a\u009b\7#\2\2\u009b\u009c")
        buf.write("\7?\2\2\u009c \3\2\2\2\u009d\u009e\7>\2\2\u009e\u009f")
        buf.write("\7?\2\2\u009f\"\3\2\2\2\u00a0\u00a1\7@\2\2\u00a1\u00a2")
        buf.write("\7?\2\2\u00a2$\3\2\2\2\u00a3\u00a4\7>\2\2\u00a4&\3\2\2")
        buf.write("\2\u00a5\u00a6\7@\2\2\u00a6(\3\2\2\2\u00a7\u00a8\7?\2")
        buf.write("\2\u00a8*\3\2\2\2\u00a9\u00aa\7#\2\2\u00aa,\3\2\2\2\u00ab")
        buf.write("\u00ac\7-\2\2\u00ac.\3\2\2\2\u00ad\u00ae\7/\2\2\u00ae")
        buf.write("\60\3\2\2\2\u00af\u00b0\7,\2\2\u00b0\62\3\2\2\2\u00b1")
        buf.write("\u00b2\7\61\2\2\u00b2\64\3\2\2\2\u00b3\u00b4\7\'\2\2\u00b4")
        buf.write("\66\3\2\2\2\u00b5\u00b6\7.\2\2\u00b68\3\2\2\2\u00b7\u00b8")
        buf.write("\7=\2\2\u00b8:\3\2\2\2\u00b9\u00ba\7*\2\2\u00ba<\3\2\2")
        buf.write("\2\u00bb\u00bc\7+\2\2\u00bc>\3\2\2\2\u00bd\u00be\7}\2")
        buf.write("\2\u00be@\3\2\2\2\u00bf\u00c0\7\177\2\2\u00c0B\3\2\2\2")
        buf.write("\u00c1\u00c5\t\3\2\2\u00c2\u00c4\t\4\2\2\u00c3\u00c2\3")
        buf.write("\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6D\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00ca")
        buf.write("\t\5\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00ccF\3\2\2\2\u00cd")
        buf.write("\u00d3\7$\2\2\u00ce\u00d2\n\6\2\2\u00cf\u00d0\7^\2\2\u00d0")
        buf.write("\u00d2\13\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3\2\2")
        buf.write("\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6")
        buf.write("\u00d7\7$\2\2\u00d7H\3\2\2\2\u00d8\u00d9\7\61\2\2\u00d9")
        buf.write("\u00da\7\61\2\2\u00da\u00de\3\2\2\2\u00db\u00dd\n\7\2")
        buf.write("\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e1\u00e2\b%\2\2\u00e2J\3\2\2\2\u00e3")
        buf.write("\u00e4\7\61\2\2\u00e4\u00e5\7,\2\2\u00e5\u00e9\3\2\2\2")
        buf.write("\u00e6\u00e8\13\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\7,\2\2")
        buf.write("\u00ed\u00ee\7\61\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0")
        buf.write("\b&\2\2\u00f0L\3\2\2\2\u00f1\u00f3\t\b\2\2\u00f2\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b\'\2\2")
        buf.write("\u00f7N\3\2\2\2\13\2`\u00c5\u00cb\u00d1\u00d3\u00de\u00e9")
        buf.write("\u00f4\3\b\2\2")
        return buf.getvalue()


class SimplePythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    BOOL = 2
    CHAR_PTR = 3
    VOID = 4
    RETURN = 5
    IF = 6
    ELSE = 7
    WHILE = 8
    PRINTF = 9
    TRUE = 10
    FALSE = 11
    AND = 12
    OR = 13
    EQ = 14
    NE = 15
    LE = 16
    GE = 17
    LT = 18
    GT = 19
    ASSIGN = 20
    NOT = 21
    PLUS = 22
    MINUS = 23
    STAR = 24
    SLASH = 25
    PERCENT = 26
    COMMA = 27
    SEMICOLON = 28
    OPEN_PAREN = 29
    CLOSE_PAREN = 30
    OPEN_BRACE = 31
    CLOSE_BRACE = 32
    NAME = 33
    NUMBER = 34
    STRING = 35
    LINE_COMMENT = 36
    BLOCK_COMMENT = 37
    WS = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'bool'", "'void'", "'return'", "'if'", "'else'", "'while'", 
            "'printf'", "'true'", "'false'", "'&&'", "'||'", "'=='", "'!='", 
            "'<='", "'>='", "'<'", "'>'", "'='", "'!'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "','", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "BOOL", "CHAR_PTR", "VOID", "RETURN", "IF", "ELSE", "WHILE", 
            "PRINTF", "TRUE", "FALSE", "AND", "OR", "EQ", "NE", "LE", "GE", 
            "LT", "GT", "ASSIGN", "NOT", "PLUS", "MINUS", "STAR", "SLASH", 
            "PERCENT", "COMMA", "SEMICOLON", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACE", "CLOSE_BRACE", "NAME", "NUMBER", "STRING", "LINE_COMMENT", 
            "BLOCK_COMMENT", "WS" ]

    ruleNames = [ "INT", "BOOL", "CHAR_PTR", "VOID", "RETURN", "IF", "ELSE", 
                  "WHILE", "PRINTF", "TRUE", "FALSE", "AND", "OR", "EQ", 
                  "NE", "LE", "GE", "LT", "GT", "ASSIGN", "NOT", "PLUS", 
                  "MINUS", "STAR", "SLASH", "PERCENT", "COMMA", "SEMICOLON", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", 
                  "NAME", "NUMBER", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "WS" ]

    grammarFileName = "SimplePythonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


