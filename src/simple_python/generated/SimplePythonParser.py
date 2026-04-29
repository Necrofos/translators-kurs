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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u00f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\7\2")
        buf.write("<\n\2\f\2\16\2?\13\2\3\2\3\2\3\3\3\3\5\3E\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4Y\n\4\3\5\3\5\3\5\3\5\5\5_\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\5\7h\n\7\3\7\3\7\3\b\3\b\5\bn\n\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\ny\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u0085\n\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\7\17\u0091\n")
        buf.write("\17\f\17\16\17\u0094\13\17\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\7\21\u009c\n\21\f\21\16\21\u009f\13\21\3\22\3\22\7")
        buf.write("\22\u00a3\n\22\f\22\16\22\u00a6\13\22\3\22\3\22\3\23\3")
        buf.write("\23\3\24\3\24\3\24\7\24\u00af\n\24\f\24\16\24\u00b2\13")
        buf.write("\24\3\25\3\25\3\25\7\25\u00b7\n\25\f\25\16\25\u00ba\13")
        buf.write("\25\3\26\3\26\3\26\5\26\u00bf\n\26\3\27\3\27\3\27\7\27")
        buf.write("\u00c4\n\27\f\27\16\27\u00c7\13\27\3\30\3\30\3\30\7\30")
        buf.write("\u00cc\n\30\f\30\16\30\u00cf\13\30\3\31\3\31\3\31\7\31")
        buf.write("\u00d4\n\31\f\31\16\31\u00d7\13\31\3\32\3\32\3\32\5\32")
        buf.write("\u00dc\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00e5")
        buf.write("\n\33\3\34\3\34\3\34\5\34\u00ea\n\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\2\2\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668\2\b\4\2\3\3\6\6\3\2\3\5\3\2\20")
        buf.write("\25\3\2\30\31\3\2\32\34\4\2\f\r$%\2\u00ef\2=\3\2\2\2\4")
        buf.write("D\3\2\2\2\6X\3\2\2\2\bZ\3\2\2\2\n`\3\2\2\2\fd\3\2\2\2")
        buf.write("\16k\3\2\2\2\20o\3\2\2\2\22q\3\2\2\2\24z\3\2\2\2\26\u0080")
        buf.write("\3\2\2\2\30\u0089\3\2\2\2\32\u008b\3\2\2\2\34\u008d\3")
        buf.write("\2\2\2\36\u0095\3\2\2\2 \u0098\3\2\2\2\"\u00a0\3\2\2\2")
        buf.write("$\u00a9\3\2\2\2&\u00ab\3\2\2\2(\u00b3\3\2\2\2*\u00be\3")
        buf.write("\2\2\2,\u00c0\3\2\2\2.\u00c8\3\2\2\2\60\u00d0\3\2\2\2")
        buf.write("\62\u00db\3\2\2\2\64\u00e4\3\2\2\2\66\u00e6\3\2\2\28\u00ed")
        buf.write("\3\2\2\2:<\5\4\3\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2")
        buf.write("\2\2>@\3\2\2\2?=\3\2\2\2@A\7\2\2\3A\3\3\2\2\2BE\5\26\f")
        buf.write("\2CE\5\6\4\2DB\3\2\2\2DC\3\2\2\2E\5\3\2\2\2FG\5\b\5\2")
        buf.write("GH\7\36\2\2HY\3\2\2\2IJ\5\n\6\2JK\7\36\2\2KY\3\2\2\2L")
        buf.write("M\5\f\7\2MN\7\36\2\2NY\3\2\2\2OP\5\16\b\2PQ\7\36\2\2Q")
        buf.write("Y\3\2\2\2RS\5\20\t\2ST\7\36\2\2TY\3\2\2\2UY\5\22\n\2V")
        buf.write("Y\5\24\13\2WY\5\"\22\2XF\3\2\2\2XI\3\2\2\2XL\3\2\2\2X")
        buf.write("O\3\2\2\2XR\3\2\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\7\3")
        buf.write("\2\2\2Z[\5\32\16\2[^\7#\2\2\\]\7\26\2\2]_\5$\23\2^\\\3")
        buf.write("\2\2\2^_\3\2\2\2_\t\3\2\2\2`a\7#\2\2ab\7\26\2\2bc\5$\23")
        buf.write("\2c\13\3\2\2\2de\7\13\2\2eg\7\37\2\2fh\5 \21\2gf\3\2\2")
        buf.write("\2gh\3\2\2\2hi\3\2\2\2ij\7 \2\2j\r\3\2\2\2km\7\7\2\2l")
        buf.write("n\5$\23\2ml\3\2\2\2mn\3\2\2\2n\17\3\2\2\2op\5$\23\2p\21")
        buf.write("\3\2\2\2qr\7\b\2\2rs\7\37\2\2st\5$\23\2tu\7 \2\2ux\5\"")
        buf.write("\22\2vw\7\t\2\2wy\5\"\22\2xv\3\2\2\2xy\3\2\2\2y\23\3\2")
        buf.write("\2\2z{\7\n\2\2{|\7\37\2\2|}\5$\23\2}~\7 \2\2~\177\5\"")
        buf.write("\22\2\177\25\3\2\2\2\u0080\u0081\5\30\r\2\u0081\u0082")
        buf.write("\7#\2\2\u0082\u0084\7\37\2\2\u0083\u0085\5\34\17\2\u0084")
        buf.write("\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0087\7 \2\2\u0087\u0088\5\"\22\2\u0088\27\3\2")
        buf.write("\2\2\u0089\u008a\t\2\2\2\u008a\31\3\2\2\2\u008b\u008c")
        buf.write("\t\3\2\2\u008c\33\3\2\2\2\u008d\u0092\5\36\20\2\u008e")
        buf.write("\u008f\7\35\2\2\u008f\u0091\5\36\20\2\u0090\u008e\3\2")
        buf.write("\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\35\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096")
        buf.write("\5\32\16\2\u0096\u0097\7#\2\2\u0097\37\3\2\2\2\u0098\u009d")
        buf.write("\5$\23\2\u0099\u009a\7\35\2\2\u009a\u009c\5$\23\2\u009b")
        buf.write("\u0099\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e!\3\2\2\2\u009f\u009d\3\2\2")
        buf.write("\2\u00a0\u00a4\7!\2\2\u00a1\u00a3\5\6\4\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a7\u00a8\7\"\2\2\u00a8#\3\2\2\2\u00a9\u00aa\5&\24")
        buf.write("\2\u00aa%\3\2\2\2\u00ab\u00b0\5(\25\2\u00ac\u00ad\7\17")
        buf.write("\2\2\u00ad\u00af\5(\25\2\u00ae\u00ac\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\'\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b8\5*\26\2\u00b4")
        buf.write("\u00b5\7\16\2\2\u00b5\u00b7\5*\26\2\u00b6\u00b4\3\2\2")
        buf.write("\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9)\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc")
        buf.write("\7\27\2\2\u00bc\u00bf\5*\26\2\u00bd\u00bf\5,\27\2\u00be")
        buf.write("\u00bb\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf+\3\2\2\2\u00c0")
        buf.write("\u00c5\5.\30\2\u00c1\u00c2\t\4\2\2\u00c2\u00c4\5.\30\2")
        buf.write("\u00c3\u00c1\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3")
        buf.write("\2\2\2\u00c5\u00c6\3\2\2\2\u00c6-\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c8\u00cd\5\60\31\2\u00c9\u00ca\t\5\2\2\u00ca")
        buf.write("\u00cc\5\60\31\2\u00cb\u00c9\3\2\2\2\u00cc\u00cf\3\2\2")
        buf.write("\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce/\3\2")
        buf.write("\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d5\5\62\32\2\u00d1\u00d2")
        buf.write("\t\6\2\2\u00d2\u00d4\5\62\32\2\u00d3\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\61\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7\31")
        buf.write("\2\2\u00d9\u00dc\5\62\32\2\u00da\u00dc\5\64\33\2\u00db")
        buf.write("\u00d8\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\63\3\2\2\2\u00dd")
        buf.write("\u00e5\58\35\2\u00de\u00e5\5\66\34\2\u00df\u00e5\7#\2")
        buf.write("\2\u00e0\u00e1\7\37\2\2\u00e1\u00e2\5$\23\2\u00e2\u00e3")
        buf.write("\7 \2\2\u00e3\u00e5\3\2\2\2\u00e4\u00dd\3\2\2\2\u00e4")
        buf.write("\u00de\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4\u00e0\3\2\2\2")
        buf.write("\u00e5\65\3\2\2\2\u00e6\u00e7\7#\2\2\u00e7\u00e9\7\37")
        buf.write("\2\2\u00e8\u00ea\5 \21\2\u00e9\u00e8\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\7 \2\2\u00ec")
        buf.write("\67\3\2\2\2\u00ed\u00ee\t\7\2\2\u00ee9\3\2\2\2\26=DX^")
        buf.write("gmx\u0084\u0092\u009d\u00a4\u00b0\u00b8\u00be\u00c5\u00cd")
        buf.write("\u00d5\u00db\u00e4\u00e9")
        return buf.getvalue()


class SimplePythonParser ( Parser ):

    grammarFileName = "SimplePythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'bool'", "<INVALID>", "'void'", 
                     "'return'", "'if'", "'else'", "'while'", "'printf'", 
                     "'true'", "'false'", "'&&'", "'||'", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'", "'='", "'!'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "','", "';'", "'('", "')'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INT", "BOOL", "CHAR_PTR", "VOID", "RETURN", 
                      "IF", "ELSE", "WHILE", "PRINTF", "TRUE", "FALSE", 
                      "AND", "OR", "EQ", "NE", "LE", "GE", "LT", "GT", "ASSIGN", 
                      "NOT", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
                      "COMMA", "SEMICOLON", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACE", "CLOSE_BRACE", "NAME", "NUMBER", "STRING", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

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
    RULE_parameterList = 13
    RULE_parameter = 14
    RULE_argumentList = 15
    RULE_block = 16
    RULE_expression = 17
    RULE_orExpression = 18
    RULE_andExpression = 19
    RULE_notExpression = 20
    RULE_comparison = 21
    RULE_additiveExpression = 22
    RULE_multiplicativeExpression = 23
    RULE_unaryExpression = 24
    RULE_primary = 25
    RULE_functionCall = 26
    RULE_literal = 27

    ruleNames =  [ "program", "declaration", "statement", "variableDeclaration", 
                   "assignment", "printfStatement", "returnStatement", "expressionStatement", 
                   "ifStatement", "whileStatement", "functionDefinition", 
                   "functionReturnType", "typeSpecifier", "parameterList", 
                   "parameter", "argumentList", "block", "expression", "orExpression", 
                   "andExpression", "notExpression", "comparison", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "primary", 
                   "functionCall", "literal" ]

    EOF = Token.EOF
    INT=1
    BOOL=2
    CHAR_PTR=3
    VOID=4
    RETURN=5
    IF=6
    ELSE=7
    WHILE=8
    PRINTF=9
    TRUE=10
    FALSE=11
    AND=12
    OR=13
    EQ=14
    NE=15
    LE=16
    GE=17
    LT=18
    GT=19
    ASSIGN=20
    NOT=21
    PLUS=22
    MINUS=23
    STAR=24
    SLASH=25
    PERCENT=26
    COMMA=27
    SEMICOLON=28
    OPEN_PAREN=29
    CLOSE_PAREN=30
    OPEN_BRACE=31
    CLOSE_BRACE=32
    NAME=33
    NUMBER=34
    STRING=35
    LINE_COMMENT=36
    BLOCK_COMMENT=37
    WS=38

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
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR) | (1 << SimplePythonParser.VOID) | (1 << SimplePythonParser.RETURN) | (1 << SimplePythonParser.IF) | (1 << SimplePythonParser.WHILE) | (1 << SimplePythonParser.PRINTF) | (1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.OPEN_BRACE) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 56
                self.declaration()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.functionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.variableDeclaration()
                self.state = 69
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.assignment()
                self.state = 72
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.printfStatement()
                self.state = 75
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.returnStatement()
                self.state = 78
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.expressionStatement()
                self.state = 81
                self.match(SimplePythonParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 85
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
            self.state = 88
            self.typeSpecifier()
            self.state = 89
            self.match(SimplePythonParser.NAME)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePythonParser.ASSIGN:
                self.state = 90
                self.match(SimplePythonParser.ASSIGN)
                self.state = 91
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

        def NAME(self):
            return self.getToken(SimplePythonParser.NAME, 0)

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
            self.state = 94
            self.match(SimplePythonParser.NAME)
            self.state = 95
            self.match(SimplePythonParser.ASSIGN)
            self.state = 96
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
            self.state = 98
            self.match(SimplePythonParser.PRINTF)
            self.state = 99
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 100
                self.argumentList()


            self.state = 103
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
            self.state = 105
            self.match(SimplePythonParser.RETURN)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 106
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
            self.state = 109
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
            self.state = 111
            self.match(SimplePythonParser.IF)
            self.state = 112
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(SimplePythonParser.CLOSE_PAREN)
            self.state = 115
            self.block()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePythonParser.ELSE:
                self.state = 116
                self.match(SimplePythonParser.ELSE)
                self.state = 117
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
            self.state = 120
            self.match(SimplePythonParser.WHILE)
            self.state = 121
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 122
            self.expression()
            self.state = 123
            self.match(SimplePythonParser.CLOSE_PAREN)
            self.state = 124
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
            self.state = 126
            self.functionReturnType()
            self.state = 127
            self.match(SimplePythonParser.NAME)
            self.state = 128
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR))) != 0):
                self.state = 129
                self.parameterList()


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


    class FunctionReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimplePythonParser.INT, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not(_la==SimplePythonParser.INT or _la==SimplePythonParser.VOID):
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR))) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.parameter()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.COMMA:
                self.state = 140
                self.match(SimplePythonParser.COMMA)
                self.state = 141
                self.parameter()
                self.state = 146
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
        self.enterRule(localctx, 28, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.typeSpecifier()
            self.state = 148
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
        self.enterRule(localctx, 30, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expression()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.COMMA:
                self.state = 151
                self.match(SimplePythonParser.COMMA)
                self.state = 152
                self.expression()
                self.state = 157
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
        self.enterRule(localctx, 32, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(SimplePythonParser.OPEN_BRACE)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.INT) | (1 << SimplePythonParser.BOOL) | (1 << SimplePythonParser.CHAR_PTR) | (1 << SimplePythonParser.RETURN) | (1 << SimplePythonParser.IF) | (1 << SimplePythonParser.WHILE) | (1 << SimplePythonParser.PRINTF) | (1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.OPEN_BRACE) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 159
                self.statement()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
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
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 36, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.andExpression()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.OR:
                self.state = 170
                self.match(SimplePythonParser.OR)
                self.state = 171
                self.andExpression()
                self.state = 176
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
        self.enterRule(localctx, 38, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.notExpression()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.AND:
                self.state = 178
                self.match(SimplePythonParser.AND)
                self.state = 179
                self.notExpression()
                self.state = 184
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
        self.enterRule(localctx, 40, self.RULE_notExpression)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePythonParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(SimplePythonParser.NOT)
                self.state = 186
                self.notExpression()
                pass
            elif token in [SimplePythonParser.TRUE, SimplePythonParser.FALSE, SimplePythonParser.MINUS, SimplePythonParser.OPEN_PAREN, SimplePythonParser.NAME, SimplePythonParser.NUMBER, SimplePythonParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
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
        self.enterRule(localctx, 42, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.additiveExpression()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.EQ) | (1 << SimplePythonParser.NE) | (1 << SimplePythonParser.LE) | (1 << SimplePythonParser.GE) | (1 << SimplePythonParser.LT) | (1 << SimplePythonParser.GT))) != 0):
                self.state = 191
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.EQ) | (1 << SimplePythonParser.NE) | (1 << SimplePythonParser.LE) | (1 << SimplePythonParser.GE) | (1 << SimplePythonParser.LT) | (1 << SimplePythonParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.additiveExpression()
                self.state = 197
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
        self.enterRule(localctx, 44, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.multiplicativeExpression()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePythonParser.PLUS or _la==SimplePythonParser.MINUS:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==SimplePythonParser.PLUS or _la==SimplePythonParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.multiplicativeExpression()
                self.state = 205
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
        self.enterRule(localctx, 46, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.unaryExpression()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.STAR) | (1 << SimplePythonParser.SLASH) | (1 << SimplePythonParser.PERCENT))) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.STAR) | (1 << SimplePythonParser.SLASH) | (1 << SimplePythonParser.PERCENT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.unaryExpression()
                self.state = 213
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
        self.enterRule(localctx, 48, self.RULE_unaryExpression)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePythonParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(SimplePythonParser.MINUS)
                self.state = 215
                self.unaryExpression()
                pass
            elif token in [SimplePythonParser.TRUE, SimplePythonParser.FALSE, SimplePythonParser.OPEN_PAREN, SimplePythonParser.NAME, SimplePythonParser.NUMBER, SimplePythonParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
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
        self.enterRule(localctx, 50, self.RULE_primary)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(SimplePythonParser.NAME)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(SimplePythonParser.OPEN_PAREN)
                self.state = 223
                self.expression()
                self.state = 224
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
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(SimplePythonParser.NAME)
            self.state = 229
            self.match(SimplePythonParser.OPEN_PAREN)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePythonParser.TRUE) | (1 << SimplePythonParser.FALSE) | (1 << SimplePythonParser.NOT) | (1 << SimplePythonParser.MINUS) | (1 << SimplePythonParser.OPEN_PAREN) | (1 << SimplePythonParser.NAME) | (1 << SimplePythonParser.NUMBER) | (1 << SimplePythonParser.STRING))) != 0):
                self.state = 230
                self.argumentList()


            self.state = 233
            self.match(SimplePythonParser.CLOSE_PAREN)
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
        self.enterRule(localctx, 54, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
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





