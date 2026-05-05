# Generated from grammar/SimplePythonParser.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u0120\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\7\2D\n\2\f\2\16\2G\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4b\n\4")
        buf.write("\3\5\3\5\3\5\3\5\5\5h\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\5\7q\n\7\3\7\3\7\3\b\3\b\5\bw\n\b\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u0082\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\5\f\u008e\n\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\5\r\u0095\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u009c\n")
        buf.write("\16\3\17\3\17\3\17\3\17\7\17\u00a2\n\17\f\17\16\17\u00a5")
        buf.write("\13\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\7\21\u00b1\n\21\f\21\16\21\u00b4\13\21\3\22\3\22\3")
        buf.write("\22\3\23\3\23\3\23\7\23\u00bc\n\23\f\23\16\23\u00bf\13")
        buf.write("\23\3\24\3\24\7\24\u00c3\n\24\f\24\16\24\u00c6\13\24\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\26\7\26\u00cf\n\26\f\26")
        buf.write("\16\26\u00d2\13\26\3\27\3\27\3\27\7\27\u00d7\n\27\f\27")
        buf.write("\16\27\u00da\13\27\3\30\3\30\3\30\5\30\u00df\n\30\3\31")
        buf.write("\3\31\3\31\7\31\u00e4\n\31\f\31\16\31\u00e7\13\31\3\32")
        buf.write("\3\32\3\32\7\32\u00ec\n\32\f\32\16\32\u00ef\13\32\3\33")
        buf.write("\3\33\3\33\7\33\u00f4\n\33\f\33\16\33\u00f7\13\33\3\34")
        buf.write("\3\34\3\34\5\34\u00fc\n\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u0106\n\35\3\36\3\36\3\36\5\36\u010b")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\6\37\u0112\n\37\r\37\16")
        buf.write("\37\u0113\3 \3 \3 \7 \u0119\n \f \16 \u011c\13 \3!\3!")
        buf.write("\3!\2\2\"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@\2\6\3\2\21\26\3\2\31\32\3\2\33\35")
        buf.write("\4\2\r\16&\'\2\u0124\2E\3\2\2\2\4M\3\2\2\2\6a\3\2\2\2")
        buf.write("\bc\3\2\2\2\ni\3\2\2\2\fm\3\2\2\2\16t\3\2\2\2\20x\3\2")
        buf.write("\2\2\22z\3\2\2\2\24\u0083\3\2\2\2\26\u0089\3\2\2\2\30")
        buf.write("\u0094\3\2\2\2\32\u009b\3\2\2\2\34\u009d\3\2\2\2\36\u00a9")
        buf.write("\3\2\2\2 \u00ad\3\2\2\2\"\u00b5\3\2\2\2$\u00b8\3\2\2\2")
        buf.write("&\u00c0\3\2\2\2(\u00c9\3\2\2\2*\u00cb\3\2\2\2,\u00d3\3")
        buf.write("\2\2\2.\u00de\3\2\2\2\60\u00e0\3\2\2\2\62\u00e8\3\2\2")
        buf.write("\2\64\u00f0\3\2\2\2\66\u00fb\3\2\2\28\u0105\3\2\2\2:\u0107")
        buf.write("\3\2\2\2<\u010e\3\2\2\2>\u0115\3\2\2\2@\u011d\3\2\2\2")
        buf.write("BD\5\4\3\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3")
        buf.write("\2\2\2GE\3\2\2\2HI\7\2\2\3I\3\3\2\2\2JN\5\34\17\2KN\5")
        buf.write("\26\f\2LN\5\6\4\2MJ\3\2\2\2MK\3\2\2\2ML\3\2\2\2N\5\3\2")
        buf.write("\2\2OP\5\b\5\2PQ\7\37\2\2Qb\3\2\2\2RS\5\n\6\2ST\7\37\2")
        buf.write("\2Tb\3\2\2\2UV\5\f\7\2VW\7\37\2\2Wb\3\2\2\2XY\5\16\b\2")
        buf.write("YZ\7\37\2\2Zb\3\2\2\2[\\\5\20\t\2\\]\7\37\2\2]b\3\2\2")
        buf.write("\2^b\5\22\n\2_b\5\24\13\2`b\5&\24\2aO\3\2\2\2aR\3\2\2")
        buf.write("\2aU\3\2\2\2aX\3\2\2\2a[\3\2\2\2a^\3\2\2\2a_\3\2\2\2a")
        buf.write("`\3\2\2\2b\7\3\2\2\2cd\5\32\16\2dg\7%\2\2ef\7\27\2\2f")
        buf.write("h\5(\25\2ge\3\2\2\2gh\3\2\2\2h\t\3\2\2\2ij\5> \2jk\7\27")
        buf.write("\2\2kl\5(\25\2l\13\3\2\2\2mn\7\f\2\2np\7!\2\2oq\5$\23")
        buf.write("\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\"\2\2s\r\3\2\2\2")
        buf.write("tv\7\b\2\2uw\5(\25\2vu\3\2\2\2vw\3\2\2\2w\17\3\2\2\2x")
        buf.write("y\5(\25\2y\21\3\2\2\2z{\7\t\2\2{|\7!\2\2|}\5(\25\2}~\7")
        buf.write("\"\2\2~\u0081\5&\24\2\177\u0080\7\n\2\2\u0080\u0082\5")
        buf.write("&\24\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\23")
        buf.write("\3\2\2\2\u0083\u0084\7\13\2\2\u0084\u0085\7!\2\2\u0085")
        buf.write("\u0086\5(\25\2\u0086\u0087\7\"\2\2\u0087\u0088\5&\24\2")
        buf.write("\u0088\25\3\2\2\2\u0089\u008a\5\30\r\2\u008a\u008b\7%")
        buf.write("\2\2\u008b\u008d\7!\2\2\u008c\u008e\5 \21\2\u008d\u008c")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0090\7\"\2\2\u0090\u0091\5&\24\2\u0091\27\3\2\2\2\u0092")
        buf.write("\u0095\5\32\16\2\u0093\u0095\7\6\2\2\u0094\u0092\3\2\2")
        buf.write("\2\u0094\u0093\3\2\2\2\u0095\31\3\2\2\2\u0096\u009c\7")
        buf.write("\3\2\2\u0097\u009c\7\4\2\2\u0098\u009c\7\5\2\2\u0099\u009a")
        buf.write("\7\7\2\2\u009a\u009c\7%\2\2\u009b\u0096\3\2\2\2\u009b")
        buf.write("\u0097\3\2\2\2\u009b\u0098\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009c\33\3\2\2\2\u009d\u009e\7\7\2\2\u009e\u009f\7%\2")
        buf.write("\2\u009f\u00a3\7#\2\2\u00a0\u00a2\5\36\20\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a7\7$\2\2\u00a7\u00a8\7\37\2\2\u00a8\35\3\2")
        buf.write("\2\2\u00a9\u00aa\5\32\16\2\u00aa\u00ab\7%\2\2\u00ab\u00ac")
        buf.write("\7\37\2\2\u00ac\37\3\2\2\2\u00ad\u00b2\5\"\22\2\u00ae")
        buf.write("\u00af\7\36\2\2\u00af\u00b1\5\"\22\2\u00b0\u00ae\3\2\2")
        buf.write("\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3!\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6")
        buf.write("\5\32\16\2\u00b6\u00b7\7%\2\2\u00b7#\3\2\2\2\u00b8\u00bd")
        buf.write("\5(\25\2\u00b9\u00ba\7\36\2\2\u00ba\u00bc\5(\25\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be%\3\2\2\2\u00bf\u00bd\3\2\2")
        buf.write("\2\u00c0\u00c4\7#\2\2\u00c1\u00c3\5\6\4\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c7\u00c8\7$\2\2\u00c8\'\3\2\2\2\u00c9\u00ca\5*\26")
        buf.write("\2\u00ca)\3\2\2\2\u00cb\u00d0\5,\27\2\u00cc\u00cd\7\20")
        buf.write("\2\2\u00cd\u00cf\5,\27\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2")
        buf.write("\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("+\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d8\5.\30\2\u00d4")
        buf.write("\u00d5\7\17\2\2\u00d5\u00d7\5.\30\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9-\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc")
        buf.write("\7\30\2\2\u00dc\u00df\5.\30\2\u00dd\u00df\5\60\31\2\u00de")
        buf.write("\u00db\3\2\2\2\u00de\u00dd\3\2\2\2\u00df/\3\2\2\2\u00e0")
        buf.write("\u00e5\5\62\32\2\u00e1\u00e2\t\2\2\2\u00e2\u00e4\5\62")
        buf.write("\32\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\61\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e8\u00ed\5\64\33\2\u00e9\u00ea\t\3\2\2\u00ea")
        buf.write("\u00ec\5\64\33\2\u00eb\u00e9\3\2\2\2\u00ec\u00ef\3\2\2")
        buf.write("\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\63\3")
        buf.write("\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f5\5\66\34\2\u00f1")
        buf.write("\u00f2\t\4\2\2\u00f2\u00f4\5\66\34\2\u00f3\u00f1\3\2\2")
        buf.write("\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6\65\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9")
        buf.write("\7\32\2\2\u00f9\u00fc\5\66\34\2\u00fa\u00fc\58\35\2\u00fb")
        buf.write("\u00f8\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\67\3\2\2\2\u00fd")
        buf.write("\u0106\5@!\2\u00fe\u0106\5:\36\2\u00ff\u0106\5<\37\2\u0100")
        buf.write("\u0106\7%\2\2\u0101\u0102\7!\2\2\u0102\u0103\5(\25\2\u0103")
        buf.write("\u0104\7\"\2\2\u0104\u0106\3\2\2\2\u0105\u00fd\3\2\2\2")
        buf.write("\u0105\u00fe\3\2\2\2\u0105\u00ff\3\2\2\2\u0105\u0100\3")
        buf.write("\2\2\2\u0105\u0101\3\2\2\2\u01069\3\2\2\2\u0107\u0108")
        buf.write("\7%\2\2\u0108\u010a\7!\2\2\u0109\u010b\5$\23\2\u010a\u0109")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("\u010d\7\"\2\2\u010d;\3\2\2\2\u010e\u0111\7%\2\2\u010f")
        buf.write("\u0110\7 \2\2\u0110\u0112\7%\2\2\u0111\u010f\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114=\3\2\2\2\u0115\u011a\7%\2\2\u0116\u0117\7 \2\2")
        buf.write("\u0117\u0119\7%\2\2\u0118\u0116\3\2\2\2\u0119\u011c\3")
        buf.write("\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b?")
        buf.write("\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e\t\5\2\2\u011e")
        buf.write("A\3\2\2\2\33EMagpv\u0081\u008d\u0094\u009b\u00a3\u00b2")
        buf.write("\u00bd\u00c4\u00d0\u00d8\u00de\u00e5\u00ed\u00f5\u00fb")
        buf.write("\u0105\u010a\u0113\u011a")
        return buf.getvalue()


class SimplePythonParser ( Parser ):

    grammarFileName = "SimplePythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'bool'", "<INVALID>", "'void'", 
                     "'struct'", "'return'", "'if'", "'else'", "'while'", 
                     "'printf'", "'true'", "'false'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<='", "'>='", "'<'", "'>'", "'='", "'!'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "','", "';'", "'.'", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INT", "BOOL", "CHAR_PTR", "VOID", "STRUCT", 
                      "RETURN", "IF", "ELSE", "WHILE", "PRINTF", "TRUE", 
                      "FALSE", "AND", "OR", "EQ", "NE", "LE", "GE", "LT", 
                      "GT", "ASSIGN", "NOT", "PLUS", "MINUS", "STAR", "SLASH", 
                      "PERCENT", "COMMA", "SEMICOLON", "DOT", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "NAME", 
                      "NUMBER", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_statement = 2
    RULE_variableDeclaration = 3
    RULE_assignment = 4
    RULE_printfStatement = 5
    RULE_returnStatement = 6
    RULE_expressionStatement = 7
    RULE_ifStatement = 8
    RULE_whileStatement = 9
    RULE_functionDefinition = 10
    RULE_functionReturnType = 11
    RULE_typeSpecifier = 12
    RULE_structDefinition = 13
    RULE_structFieldDeclaration = 14
    RULE_parameterList = 15
    RULE_parameter = 16
    RULE_argumentList = 17
    RULE_block = 18
    RULE_expression = 19
    RULE_orExpression = 20
    RULE_andExpression = 21
    RULE_notExpression = 22
    RULE_comparison = 23
    RULE_additiveExpression = 24
    RULE_multiplicativeExpression = 25
    RULE_unaryExpression = 26
    RULE_primary = 27
    RULE_functionCall = 28
    RULE_fieldAccess = 29
    RULE_assignmentTarget = 30
    RULE_literal = 31

    ruleNames =  [ "program", "declaration", "statement", "variableDeclaration", 
                   "assignment", "printfStatement", "returnStatement", "expressionStatement", 
                   "ifStatement", "whileStatement", "functionDefinition", 
                   "functionReturnType", "typeSpecifier", "structDefinition", 
                   "structFieldDeclaration", "parameterList", "parameter", 
                   "argumentList", "block", "expression", "orExpression", 
                   "andExpression", "notExpression", "comparison", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "primary", 
                   "functionCall", "fieldAccess", "assignmentTarget", "literal" ]

    EOF = Token.EOF
    INT=1
    BOOL=2
    CHAR_PTR=3
    VOID=4
    STRUCT=5
    RETURN=6
    IF=7
    ELSE=8
    WHILE=9
    PRINTF=10
    TRUE=11
    FALSE=12
    AND=13
    OR=14
    EQ=15
    NE=16
    LE=17
    GE=18
    LT=19
    GT=20
    ASSIGN=21
    NOT=22
    PLUS=23
    MINUS=24
    STAR=25
    SLASH=26
    PERCENT=27
    COMMA=28
    SEMICOLON=29
    DOT=30
    OPEN_PAREN=31
    CLOSE_PAREN=32
    OPEN_BRACE=33
    CLOSE_BRACE=34
    NAME=35
    NUMBER=36
    STRING=37
    LINE_COMMENT=38
    BLOCK_COMMENT=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimplePythonParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.DeclarationContext,i)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimplePythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR) | (1 << SimplePythonParser.VOID) | (1 << SimplePythonParser.STRUCT) | (1 << SimplePythonParser.RETURN) | (1 << SimplePythonParser.IF) | (1 << SimplePythonParser.WHILE) | (1 << SimplePythonParser.PRINTF) | (1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.OPEN_BRACE) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 64
                self.declaration()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(SimplePythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structDefinition(self):
            return self.getTypedRuleContext(SimplePythonParser.StructDefinitionContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(SimplePythonParser.FunctionDefinitionContext,0)


        def statement(self):
            return self.getTypedRuleContext(SimplePythonParser.StatementContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = SimplePythonParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.structDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.functionDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(SimplePythonParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(SimplePythonParser.SEMICOLON, 0)

        def assignment(self):
            return self.getTypedRuleContext(SimplePythonParser.AssignmentContext,0)


        def printfStatement(self):
            return self.getTypedRuleContext(SimplePythonParser.PrintfStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(SimplePythonParser.ReturnStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SimplePythonParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(SimplePythonParser.WhileStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(SimplePythonParser.BlockContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SimplePythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.variableDeclaration()
                self.state = 78
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.assignment()
                self.state = 81
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.printfStatement()
                self.state = 84
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.returnStatement()
                self.state = 87
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.expressionStatement()
                self.state = 90
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(SimplePythonParser.TypeSpecifierContext,0)


        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def ASSIGN(self):
            return self.getToken(SimplePythonParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = SimplePythonParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.typeSpecifier()
            self.state = 98
            self.match(SimplePythonParser.NAME)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePythonParser.ASSIGN:
                self.state = 99
                self.match(SimplePythonParser.ASSIGN)
                self.state = 100
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentTarget(self):
            return self.getTypedRuleContext(SimplePythonParser.AssignmentTargetContext,0)


        def ASSIGN(self):
            return self.getToken(SimplePythonParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SimplePythonParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.assignmentTarget()
            self.state = 104
            self.match(SimplePythonParser.ASSIGN)
            self.state = 105
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTF(self):
            return self.getToken(SimplePythonParser.PRINTF, 0)

        def OPEN_PAREN(self):
            return self.getToken(SimplePythonParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(SimplePythonParser.CLOSE_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(SimplePythonParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_printfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintfStatement" ):
                return visitor.visitPrintfStatement(self)
            else:
                return visitor.visitChildren(self)




    def printfStatement(self):

        localctx = SimplePythonParser.PrintfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(SimplePythonParser.PRINTF)
            self.state = 108
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 109
                self.argumentList()


            self.state = 112
            self.match(SimplePythonParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SimplePythonParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = SimplePythonParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(SimplePythonParser.RETURN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 115
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_expressionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = SimplePythonParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimplePythonParser.IF, 0)

        def OPEN_PAREN(self):
            return self.getToken(SimplePythonParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SimplePythonParser.CLOSE_PAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.BlockContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(SimplePythonParser.ELSE, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SimplePythonParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(SimplePythonParser.IF)
            self.state = 121
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 122
            self.expression()
            self.state = 123
            self.match(SimplePythonParser.CLOSE_PAREN)
            self.state = 124
            self.block()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePythonParser.ELSE:
                self.state = 125
                self.match(SimplePythonParser.ELSE)
                self.state = 126
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SimplePythonParser.WHILE, 0)

        def OPEN_PAREN(self):
            return self.getToken(SimplePythonParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SimplePythonParser.CLOSE_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SimplePythonParser.BlockContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SimplePythonParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(SimplePythonParser.WHILE)
            self.state = 130
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 131
            self.expression()
            self.state = 132
            self.match(SimplePythonParser.CLOSE_PAREN)
            self.state = 133
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionReturnType(self):
            return self.getTypedRuleContext(SimplePythonParser.FunctionReturnTypeContext,0)


        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(SimplePythonParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(SimplePythonParser.CLOSE_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SimplePythonParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(SimplePythonParser.ParameterListContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_functionDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = SimplePythonParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.functionReturnType()
            self.state = 136
            self.match(SimplePythonParser.NAME)
            self.state = 137
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR) | (1 << SimplePythonParser.STRUCT))) != 0):
                self.state = 138
                self.parameterList()


            self.state = 141
            self.match(SimplePythonParser.CLOSE_PAREN)
            self.state = 142
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(SimplePythonParser.TypeSpecifierContext,0)


        def VOID(self):
            return self.getToken(SimplePythonParser.VOID, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_functionReturnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionReturnType" ):
                return visitor.visitFunctionReturnType(self)
            else:
                return visitor.visitChildren(self)




    def functionReturnType(self):

        localctx = SimplePythonParser.FunctionReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionReturnType)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePythonParser.INT, SimplePythonParser.BOOL, SimplePythonParser.CHAR_PTR, SimplePythonParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.typeSpecifier()
                pass
            elif token in [SimplePythonParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(SimplePythonParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimplePythonParser.INT, 0)

        def BOOL(self):
            return self.getToken(SimplePythonParser.BOOL, 0)

        def CHAR_PTR(self):
            return self.getToken(SimplePythonParser.CHAR_PTR, 0)

        def STRUCT(self):
            return self.getToken(SimplePythonParser.STRUCT, 0)

        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_typeSpecifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = SimplePythonParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typeSpecifier)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePythonParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(SimplePythonParser.INT)
                pass
            elif token in [SimplePythonParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(SimplePythonParser.BOOL)
                pass
            elif token in [SimplePythonParser.CHAR_PTR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(SimplePythonParser.CHAR_PTR)
                pass
            elif token in [SimplePythonParser.STRUCT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.match(SimplePythonParser.STRUCT)
                self.state = 152
                self.match(SimplePythonParser.NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(SimplePythonParser.STRUCT, 0)

        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def OPEN_BRACE(self):
            return self.getToken(SimplePythonParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(SimplePythonParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(SimplePythonParser.SEMICOLON, 0)

        def structFieldDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.StructFieldDeclarationContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.StructFieldDeclarationContext,i)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_structDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structDefinition(self):

        localctx = SimplePythonParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(SimplePythonParser.STRUCT)
            self.state = 156
            self.match(SimplePythonParser.NAME)
            self.state = 157
            self.match(SimplePythonParser.OPEN_BRACE)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR) | (1 << SimplePythonParser.STRUCT))) != 0):
                self.state = 158
                self.structFieldDeclaration()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(SimplePythonParser.CLOSE_BRACE)
            self.state = 165
            self.match(SimplePythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(SimplePythonParser.TypeSpecifierContext,0)


        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def SEMICOLON(self):
            return self.getToken(SimplePythonParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_structFieldDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldDeclaration" ):
                return visitor.visitStructFieldDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structFieldDeclaration(self):

        localctx = SimplePythonParser.StructFieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structFieldDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.typeSpecifier()
            self.state = 168
            self.match(SimplePythonParser.NAME)
            self.state = 169
            self.match(SimplePythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.ParameterContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.COMMA)
            else:
                return self.getToken(SimplePythonParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = SimplePythonParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.parameter()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.COMMA:
                self.state = 172
                self.match(SimplePythonParser.COMMA)
                self.state = 173
                self.parameter()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(SimplePythonParser.TypeSpecifierContext,0)


        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = SimplePythonParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.typeSpecifier()
            self.state = 180
            self.match(SimplePythonParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.COMMA)
            else:
                return self.getToken(SimplePythonParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = SimplePythonParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expression()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.COMMA:
                self.state = 183
                self.match(SimplePythonParser.COMMA)
                self.state = 184
                self.expression()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(SimplePythonParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(SimplePythonParser.CLOSE_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.StatementContext,i)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SimplePythonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(SimplePythonParser.OPEN_BRACE)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR) | (1 << SimplePythonParser.STRUCT) | (1 << SimplePythonParser.RETURN) | (1 << SimplePythonParser.IF) | (1 << SimplePythonParser.WHILE) | (1 << SimplePythonParser.PRINTF) | (1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.OPEN_BRACE) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 191
                self.statement()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self.match(SimplePythonParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpression(self):
            return self.getTypedRuleContext(SimplePythonParser.OrExpressionContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SimplePythonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.orExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.AndExpressionContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.AndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.OR)
            else:
                return self.getToken(SimplePythonParser.OR, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_orExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpression" ):
                return visitor.visitOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def orExpression(self):

        localctx = SimplePythonParser.OrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.andExpression()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.OR:
                self.state = 202
                self.match(SimplePythonParser.OR)
                self.state = 203
                self.andExpression()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.NotExpressionContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.NotExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.AND)
            else:
                return self.getToken(SimplePythonParser.AND, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_andExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def andExpression(self):

        localctx = SimplePythonParser.AndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.notExpression()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.AND:
                self.state = 210
                self.match(SimplePythonParser.AND)
                self.state = 211
                self.notExpression()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SimplePythonParser.NOT, 0)

        def notExpression(self):
            return self.getTypedRuleContext(SimplePythonParser.NotExpressionContext,0)


        def comparison(self):
            return self.getTypedRuleContext(SimplePythonParser.ComparisonContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_notExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)




    def notExpression(self):

        localctx = SimplePythonParser.NotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_notExpression)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePythonParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(SimplePythonParser.NOT)
                self.state = 218
                self.notExpression()
                pass
            elif token in [SimplePythonParser.TRUE, SimplePythonParser.FALSE, SimplePythonParser.MINUS, SimplePythonParser.OPEN_PAREN, SimplePythonParser.NAME, SimplePythonParser.NUMBER, SimplePythonParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.AdditiveExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.EQ)
            else:
                return self.getToken(SimplePythonParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.NE)
            else:
                return self.getToken(SimplePythonParser.NE, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.LT)
            else:
                return self.getToken(SimplePythonParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.GT)
            else:
                return self.getToken(SimplePythonParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.LE)
            else:
                return self.getToken(SimplePythonParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.GE)
            else:
                return self.getToken(SimplePythonParser.GE, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = SimplePythonParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.additiveExpression()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.EQ) | (1 << SimplePythonParser.NE) | (1 << SimplePythonParser.LE) | (1 << SimplePythonParser.GE) | (1 << SimplePythonParser.LT) | (1 << SimplePythonParser.GT))) != 0):
                self.state = 223
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.EQ) | (1 << SimplePythonParser.NE) | (1 << SimplePythonParser.LE) | (1 << SimplePythonParser.GE) | (1 << SimplePythonParser.LT) | (1 << SimplePythonParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.additiveExpression()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.PLUS)
            else:
                return self.getToken(SimplePythonParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.MINUS)
            else:
                return self.getToken(SimplePythonParser.MINUS, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_additiveExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = SimplePythonParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.multiplicativeExpression()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.PLUS or _la==SimplePythonParser.MINUS:
                self.state = 231
                _la = self._input.LA(1)
                if not(_la==SimplePythonParser.PLUS or _la==SimplePythonParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.multiplicativeExpression()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePythonParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(SimplePythonParser.UnaryExpressionContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.STAR)
            else:
                return self.getToken(SimplePythonParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.SLASH)
            else:
                return self.getToken(SimplePythonParser.SLASH, i)

        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.PERCENT)
            else:
                return self.getToken(SimplePythonParser.PERCENT, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_multiplicativeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = SimplePythonParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.unaryExpression()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.STAR) | (1 << SimplePythonParser.SLASH) | (1 << SimplePythonParser.PERCENT))) != 0):
                self.state = 239
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.STAR) | (1 << SimplePythonParser.SLASH) | (1 << SimplePythonParser.PERCENT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 240
                self.unaryExpression()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(SimplePythonParser.MINUS, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(SimplePythonParser.UnaryExpressionContext,0)


        def primary(self):
            return self.getTypedRuleContext(SimplePythonParser.PrimaryContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_unaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = SimplePythonParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExpression)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePythonParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(SimplePythonParser.MINUS)
                self.state = 247
                self.unaryExpression()
                pass
            elif token in [SimplePythonParser.TRUE, SimplePythonParser.FALSE, SimplePythonParser.OPEN_PAREN, SimplePythonParser.NAME, SimplePythonParser.NUMBER, SimplePythonParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(SimplePythonParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SimplePythonParser.FunctionCallContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(SimplePythonParser.FieldAccessContext,0)


        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(SimplePythonParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePythonParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SimplePythonParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = SimplePythonParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primary)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.fieldAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.match(SimplePythonParser.NAME)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.match(SimplePythonParser.OPEN_PAREN)
                self.state = 256
                self.expression()
                self.state = 257
                self.match(SimplePythonParser.CLOSE_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(SimplePythonParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(SimplePythonParser.CLOSE_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(SimplePythonParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return SimplePythonParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = SimplePythonParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(SimplePythonParser.NAME)
            self.state = 262
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 263
                self.argumentList()


            self.state = 266
            self.match(SimplePythonParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.NAME)
            else:
                return self.getToken(SimplePythonParser.NAME, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.DOT)
            else:
                return self.getToken(SimplePythonParser.DOT, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_fieldAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAccess" ):
                return visitor.visitFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldAccess(self):

        localctx = SimplePythonParser.FieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_fieldAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(SimplePythonParser.NAME)
            self.state = 271 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.match(SimplePythonParser.DOT)
                self.state = 270
                self.match(SimplePythonParser.NAME)
                self.state = 273 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimplePythonParser.DOT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.NAME)
            else:
                return self.getToken(SimplePythonParser.NAME, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePythonParser.DOT)
            else:
                return self.getToken(SimplePythonParser.DOT, i)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_assignmentTarget

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentTarget" ):
                return visitor.visitAssignmentTarget(self)
            else:
                return visitor.visitChildren(self)




    def assignmentTarget(self):

        localctx = SimplePythonParser.AssignmentTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignmentTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(SimplePythonParser.NAME)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.DOT:
                self.state = 276
                self.match(SimplePythonParser.DOT)
                self.state = 277
                self.match(SimplePythonParser.NAME)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SimplePythonParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(SimplePythonParser.STRING, 0)

        def TRUE(self):
            return self.getToken(SimplePythonParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SimplePythonParser.FALSE, 0)

        def getRuleIndex(self):
            return SimplePythonParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SimplePythonParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





