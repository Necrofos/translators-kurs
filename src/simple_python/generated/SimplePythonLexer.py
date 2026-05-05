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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0105\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4c\n\4\f\4\16\4f\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\7$\u00d1\n$\f$\16$\u00d4")
        buf.write("\13$\3%\6%\u00d7\n%\r%\16%\u00d8\3&\3&\3&\3&\7&\u00df")
        buf.write("\n&\f&\16&\u00e2\13&\3&\3&\3\'\3\'\3\'\3\'\7\'\u00ea\n")
        buf.write("\'\f\'\16\'\u00ed\13\'\3\'\3\'\3(\3(\3(\3(\7(\u00f5\n")
        buf.write("(\f(\16(\u00f8\13(\3(\3(\3(\3(\3(\3)\6)\u0100\n)\r)\16")
        buf.write(")\u0101\3)\3)\3\u00f6\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*\3\2\t\4\2\13\13\"\"\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\3\2\62;\6\2\f\f\17\17$$^^\4\2\f")
        buf.write("\f\17\17\5\2\13\f\17\17\"\"\2\u010c\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3S\3\2\2\2\5W\3\2\2\2\7\\")
        buf.write("\3\2\2\2\ti\3\2\2\2\13n\3\2\2\2\ru\3\2\2\2\17|\3\2\2\2")
        buf.write("\21\177\3\2\2\2\23\u0084\3\2\2\2\25\u008a\3\2\2\2\27\u0091")
        buf.write("\3\2\2\2\31\u0096\3\2\2\2\33\u009c\3\2\2\2\35\u009f\3")
        buf.write("\2\2\2\37\u00a2\3\2\2\2!\u00a5\3\2\2\2#\u00a8\3\2\2\2")
        buf.write("%\u00ab\3\2\2\2\'\u00ae\3\2\2\2)\u00b0\3\2\2\2+\u00b2")
        buf.write("\3\2\2\2-\u00b4\3\2\2\2/\u00b6\3\2\2\2\61\u00b8\3\2\2")
        buf.write("\2\63\u00ba\3\2\2\2\65\u00bc\3\2\2\2\67\u00be\3\2\2\2")
        buf.write("9\u00c0\3\2\2\2;\u00c2\3\2\2\2=\u00c4\3\2\2\2?\u00c6\3")
        buf.write("\2\2\2A\u00c8\3\2\2\2C\u00ca\3\2\2\2E\u00cc\3\2\2\2G\u00ce")
        buf.write("\3\2\2\2I\u00d6\3\2\2\2K\u00da\3\2\2\2M\u00e5\3\2\2\2")
        buf.write("O\u00f0\3\2\2\2Q\u00ff\3\2\2\2ST\7k\2\2TU\7p\2\2UV\7v")
        buf.write("\2\2V\4\3\2\2\2WX\7d\2\2XY\7q\2\2YZ\7q\2\2Z[\7n\2\2[\6")
        buf.write("\3\2\2\2\\]\7e\2\2]^\7j\2\2^_\7c\2\2_`\7t\2\2`d\3\2\2")
        buf.write("\2ac\t\2\2\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2e")
        buf.write("g\3\2\2\2fd\3\2\2\2gh\7,\2\2h\b\3\2\2\2ij\7x\2\2jk\7q")
        buf.write("\2\2kl\7k\2\2lm\7f\2\2m\n\3\2\2\2no\7u\2\2op\7v\2\2pq")
        buf.write("\7t\2\2qr\7w\2\2rs\7e\2\2st\7v\2\2t\f\3\2\2\2uv\7t\2\2")
        buf.write("vw\7g\2\2wx\7v\2\2xy\7w\2\2yz\7t\2\2z{\7p\2\2{\16\3\2")
        buf.write("\2\2|}\7k\2\2}~\7h\2\2~\20\3\2\2\2\177\u0080\7g\2\2\u0080")
        buf.write("\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\u0083\7g\2\2\u0083")
        buf.write("\22\3\2\2\2\u0084\u0085\7y\2\2\u0085\u0086\7j\2\2\u0086")
        buf.write("\u0087\7k\2\2\u0087\u0088\7n\2\2\u0088\u0089\7g\2\2\u0089")
        buf.write("\24\3\2\2\2\u008a\u008b\7r\2\2\u008b\u008c\7t\2\2\u008c")
        buf.write("\u008d\7k\2\2\u008d\u008e\7p\2\2\u008e\u008f\7v\2\2\u008f")
        buf.write("\u0090\7h\2\2\u0090\26\3\2\2\2\u0091\u0092\7v\2\2\u0092")
        buf.write("\u0093\7t\2\2\u0093\u0094\7w\2\2\u0094\u0095\7g\2\2\u0095")
        buf.write("\30\3\2\2\2\u0096\u0097\7h\2\2\u0097\u0098\7c\2\2\u0098")
        buf.write("\u0099\7n\2\2\u0099\u009a\7u\2\2\u009a\u009b\7g\2\2\u009b")
        buf.write("\32\3\2\2\2\u009c\u009d\7(\2\2\u009d\u009e\7(\2\2\u009e")
        buf.write("\34\3\2\2\2\u009f\u00a0\7~\2\2\u00a0\u00a1\7~\2\2\u00a1")
        buf.write("\36\3\2\2\2\u00a2\u00a3\7?\2\2\u00a3\u00a4\7?\2\2\u00a4")
        buf.write(" \3\2\2\2\u00a5\u00a6\7#\2\2\u00a6\u00a7\7?\2\2\u00a7")
        buf.write("\"\3\2\2\2\u00a8\u00a9\7>\2\2\u00a9\u00aa\7?\2\2\u00aa")
        buf.write("$\3\2\2\2\u00ab\u00ac\7@\2\2\u00ac\u00ad\7?\2\2\u00ad")
        buf.write("&\3\2\2\2\u00ae\u00af\7>\2\2\u00af(\3\2\2\2\u00b0\u00b1")
        buf.write("\7@\2\2\u00b1*\3\2\2\2\u00b2\u00b3\7?\2\2\u00b3,\3\2\2")
        buf.write("\2\u00b4\u00b5\7#\2\2\u00b5.\3\2\2\2\u00b6\u00b7\7-\2")
        buf.write("\2\u00b7\60\3\2\2\2\u00b8\u00b9\7/\2\2\u00b9\62\3\2\2")
        buf.write("\2\u00ba\u00bb\7,\2\2\u00bb\64\3\2\2\2\u00bc\u00bd\7\61")
        buf.write("\2\2\u00bd\66\3\2\2\2\u00be\u00bf\7\'\2\2\u00bf8\3\2\2")
        buf.write("\2\u00c0\u00c1\7.\2\2\u00c1:\3\2\2\2\u00c2\u00c3\7=\2")
        buf.write("\2\u00c3<\3\2\2\2\u00c4\u00c5\7\60\2\2\u00c5>\3\2\2\2")
        buf.write("\u00c6\u00c7\7*\2\2\u00c7@\3\2\2\2\u00c8\u00c9\7+\2\2")
        buf.write("\u00c9B\3\2\2\2\u00ca\u00cb\7}\2\2\u00cbD\3\2\2\2\u00cc")
        buf.write("\u00cd\7\177\2\2\u00cdF\3\2\2\2\u00ce\u00d2\t\3\2\2\u00cf")
        buf.write("\u00d1\t\4\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3H\3\2\2")
        buf.write("\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7\t\5\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9J\3\2\2\2\u00da\u00e0\7$\2\2\u00db")
        buf.write("\u00df\n\6\2\2\u00dc\u00dd\7^\2\2\u00dd\u00df\13\2\2\2")
        buf.write("\u00de\u00db\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e2\3")
        buf.write("\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7$\2\2\u00e4")
        buf.write("L\3\2\2\2\u00e5\u00e6\7\61\2\2\u00e6\u00e7\7\61\2\2\u00e7")
        buf.write("\u00eb\3\2\2\2\u00e8\u00ea\n\7\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef")
        buf.write("\b\'\2\2\u00efN\3\2\2\2\u00f0\u00f1\7\61\2\2\u00f1\u00f2")
        buf.write("\7,\2\2\u00f2\u00f6\3\2\2\2\u00f3\u00f5\13\2\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f9\u00fa\7,\2\2\u00fa\u00fb\7\61\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fd\b(\2\2\u00fdP\3\2\2\2\u00fe\u0100")
        buf.write("\t\b\2\2\u00ff\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103\u0104\b)\2\2\u0104R\3\2\2\2\13\2d\u00d2\u00d8\u00de")
        buf.write("\u00e0\u00eb\u00f6\u0101\3\b\2\2")
        return buf.getvalue()


class SimplePythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    BOOL = 2
    CHAR_PTR = 3
    VOID = 4
    STRUCT = 5
    RETURN = 6
    IF = 7
    ELSE = 8
    WHILE = 9
    PRINTF = 10
    TRUE = 11
    FALSE = 12
    AND = 13
    OR = 14
    EQ = 15
    NE = 16
    LE = 17
    GE = 18
    LT = 19
    GT = 20
    ASSIGN = 21
    NOT = 22
    PLUS = 23
    MINUS = 24
    STAR = 25
    SLASH = 26
    PERCENT = 27
    COMMA = 28
    SEMICOLON = 29
    DOT = 30
    OPEN_PAREN = 31
    CLOSE_PAREN = 32
    OPEN_BRACE = 33
    CLOSE_BRACE = 34
    NAME = 35
    NUMBER = 36
    STRING = 37
    LINE_COMMENT = 38
    BLOCK_COMMENT = 39
    WS = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'bool'", "'void'", "'struct'", "'return'", "'if'", 
            "'else'", "'while'", "'printf'", "'true'", "'false'", "'&&'", 
            "'||'", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", "'='", 
            "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", "','", "';'", "'.'", 
            "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "BOOL", "CHAR_PTR", "VOID", "STRUCT", "RETURN", "IF", 
            "ELSE", "WHILE", "PRINTF", "TRUE", "FALSE", "AND", "OR", "EQ", 
            "NE", "LE", "GE", "LT", "GT", "ASSIGN", "NOT", "PLUS", "MINUS", 
            "STAR", "SLASH", "PERCENT", "COMMA", "SEMICOLON", "DOT", "OPEN_PAREN", 
            "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "NAME", "NUMBER", 
            "STRING", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    ruleNames = [ "INT", "BOOL", "CHAR_PTR", "VOID", "STRUCT", "RETURN", 
                  "IF", "ELSE", "WHILE", "PRINTF", "TRUE", "FALSE", "AND", 
                  "OR", "EQ", "NE", "LE", "GE", "LT", "GT", "ASSIGN", "NOT", 
                  "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", "COMMA", 
                  "SEMICOLON", "DOT", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
                  "CLOSE_BRACE", "NAME", "NUMBER", "STRING", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "WS" ]

    grammarFileName = "SimplePythonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


