// Generated from /workspaces/antlr-programming-masterclass-with-python/bazilio/Bazilio.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BazilioParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, ADD=13, SUB=14, MUL=15, DIV=16, MOD=17, LT=18, 
		LTE=19, GT=20, GTE=21, EQ=22, NEQ=23, NOTE=24, NUM=25, VAR=26, PROCEDURE_NAME=27, 
		STRING=28, LEFT_BAR=29, RIGHT_BAR=30, LEFT_BRACKET=31, RIGHT_BRACKET=32, 
		LEFT_PAREN=33, RIGHT_PAREN=34, WS=35, COMMENT=36;
	public static final int
		RULE_root = 0, RULE_procedure = 1, RULE_instructions = 2, RULE_instruction = 3, 
		RULE_assignment = 4, RULE_input_ = 5, RULE_output_ = 6, RULE_reproduction = 7, 
		RULE_parameters = 8, RULE_condition = 9, RULE_while_ = 10, RULE_list_expression = 11, 
		RULE_list_add = 12, RULE_list_cut = 13, RULE_procedure_call = 14, RULE_procedure_call_parameters = 15, 
		RULE_expression = 16, RULE_list_size = 17, RULE_list_query = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "procedure", "instructions", "instruction", "assignment", "input_", 
			"output_", "reproduction", "parameters", "condition", "while_", "list_expression", 
			"list_add", "list_cut", "procedure_call", "procedure_call_parameters", 
			"expression", "list_size", "list_query"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<-'", "'<?>'", "'<w>'", "'(:)'", "'if'", "'else'", "'while'", 
			"'{'", "'}'", "'<<'", "'8<'", "'#'", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'<'", "'<='", "'>'", "'>='", "'='", "'/='", null, null, null, null, 
			null, "'|:'", "':|'", "'['", "']'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "LTE", "GT", "GTE", "EQ", 
			"NEQ", "NOTE", "NUM", "VAR", "PROCEDURE_NAME", "STRING", "LEFT_BAR", 
			"RIGHT_BAR", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_PAREN", "RIGHT_PAREN", 
			"WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Bazilio.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BazilioParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public List<ProcedureContext> procedure() {
			return getRuleContexts(ProcedureContext.class);
		}
		public ProcedureContext procedure(int i) {
			return getRuleContext(ProcedureContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterRoot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitRoot(this);
		}
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PROCEDURE_NAME) {
				{
				{
				setState(38);
				procedure();
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProcedureContext extends ParserRuleContext {
		public TerminalNode PROCEDURE_NAME() { return getToken(BazilioParser.PROCEDURE_NAME, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode LEFT_BAR() { return getToken(BazilioParser.LEFT_BAR, 0); }
		public InstructionsContext instructions() {
			return getRuleContext(InstructionsContext.class,0);
		}
		public TerminalNode RIGHT_BAR() { return getToken(BazilioParser.RIGHT_BAR, 0); }
		public ProcedureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterProcedure(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitProcedure(this);
		}
	}

	public final ProcedureContext procedure() throws RecognitionException {
		ProcedureContext _localctx = new ProcedureContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_procedure);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(PROCEDURE_NAME);
			setState(45);
			parameters();
			setState(46);
			match(LEFT_BAR);
			setState(47);
			instructions();
			setState(48);
			match(RIGHT_BAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstructionsContext extends ParserRuleContext {
		public List<InstructionContext> instruction() {
			return getRuleContexts(InstructionContext.class);
		}
		public InstructionContext instruction(int i) {
			return getRuleContext(InstructionContext.class,i);
		}
		public InstructionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instructions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterInstructions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitInstructions(this);
		}
	}

	public final InstructionsContext instructions() throws RecognitionException {
		InstructionsContext _localctx = new InstructionsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_instructions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 201328828L) != 0)) {
				{
				{
				setState(50);
				instruction();
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstructionContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Input_Context input_() {
			return getRuleContext(Input_Context.class,0);
		}
		public Output_Context output_() {
			return getRuleContext(Output_Context.class,0);
		}
		public ReproductionContext reproduction() {
			return getRuleContext(ReproductionContext.class,0);
		}
		public Procedure_callContext procedure_call() {
			return getRuleContext(Procedure_callContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public While_Context while_() {
			return getRuleContext(While_Context.class,0);
		}
		public List_addContext list_add() {
			return getRuleContext(List_addContext.class,0);
		}
		public List_cutContext list_cut() {
			return getRuleContext(List_cutContext.class,0);
		}
		public InstructionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterInstruction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitInstruction(this);
		}
	}

	public final InstructionContext instruction() throws RecognitionException {
		InstructionContext _localctx = new InstructionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_instruction);
		try {
			setState(65);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				input_();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(58);
				output_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(59);
				reproduction();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				procedure_call();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(61);
				condition();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(62);
				while_();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(63);
				list_add();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(64);
				list_cut();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(VAR);
			setState(68);
			match(T__0);
			setState(69);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Input_Context extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public Input_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterInput_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitInput_(this);
		}
	}

	public final Input_Context input_() throws RecognitionException {
		Input_Context _localctx = new Input_Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_input_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(T__1);
			setState(72);
			match(VAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Output_Context extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public TerminalNode STRING() { return getToken(BazilioParser.STRING, 0); }
		public Output_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterOutput_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitOutput_(this);
		}
	}

	public final Output_Context output_() throws RecognitionException {
		Output_Context _localctx = new Output_Context(_ctx, getState());
		enterRule(_localctx, 12, RULE_output_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(T__2);
			setState(75);
			_la = _input.LA(1);
			if ( !(_la==VAR || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReproductionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReproductionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reproduction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterReproduction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitReproduction(this);
		}
	}

	public final ReproductionContext reproduction() throws RecognitionException {
		ReproductionContext _localctx = new ReproductionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_reproduction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(T__3);
			setState(78);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(BazilioParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(BazilioParser.VAR, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterParameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitParameters(this);
		}
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(80);
				match(VAR);
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> LEFT_BAR() { return getTokens(BazilioParser.LEFT_BAR); }
		public TerminalNode LEFT_BAR(int i) {
			return getToken(BazilioParser.LEFT_BAR, i);
		}
		public List<InstructionsContext> instructions() {
			return getRuleContexts(InstructionsContext.class);
		}
		public InstructionsContext instructions(int i) {
			return getRuleContext(InstructionsContext.class,i);
		}
		public List<TerminalNode> RIGHT_BAR() { return getTokens(BazilioParser.RIGHT_BAR); }
		public TerminalNode RIGHT_BAR(int i) {
			return getToken(BazilioParser.RIGHT_BAR, i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(T__4);
			setState(87);
			expression(0);
			setState(88);
			match(LEFT_BAR);
			setState(89);
			instructions();
			setState(90);
			match(RIGHT_BAR);
			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(91);
				match(T__5);
				setState(92);
				match(LEFT_BAR);
				setState(93);
				instructions();
				setState(94);
				match(RIGHT_BAR);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_Context extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode LEFT_BAR() { return getToken(BazilioParser.LEFT_BAR, 0); }
		public InstructionsContext instructions() {
			return getRuleContext(InstructionsContext.class,0);
		}
		public TerminalNode RIGHT_BAR() { return getToken(BazilioParser.RIGHT_BAR, 0); }
		public While_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterWhile_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitWhile_(this);
		}
	}

	public final While_Context while_() throws RecognitionException {
		While_Context _localctx = new While_Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_while_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(T__6);
			setState(99);
			expression(0);
			setState(100);
			match(LEFT_BAR);
			setState(101);
			instructions();
			setState(102);
			match(RIGHT_BAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class List_expressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterList_expression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitList_expression(this);
		}
	}

	public final List_expressionContext list_expression() throws RecognitionException {
		List_expressionContext _localctx = new List_expressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_list_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(T__7);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8975814912L) != 0)) {
				{
				{
				setState(105);
				expression(0);
				}
				}
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(111);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class List_addContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List_addContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_add; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterList_add(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitList_add(this);
		}
	}

	public final List_addContext list_add() throws RecognitionException {
		List_addContext _localctx = new List_addContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_list_add);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(VAR);
			setState(114);
			match(T__9);
			setState(115);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class List_cutContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public TerminalNode LEFT_BRACKET() { return getToken(BazilioParser.LEFT_BRACKET, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(BazilioParser.RIGHT_BRACKET, 0); }
		public List_cutContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_cut; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterList_cut(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitList_cut(this);
		}
	}

	public final List_cutContext list_cut() throws RecognitionException {
		List_cutContext _localctx = new List_cutContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_list_cut);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(T__10);
			setState(118);
			match(VAR);
			setState(119);
			match(LEFT_BRACKET);
			setState(120);
			expression(0);
			setState(121);
			match(RIGHT_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Procedure_callContext extends ParserRuleContext {
		public TerminalNode PROCEDURE_NAME() { return getToken(BazilioParser.PROCEDURE_NAME, 0); }
		public Procedure_call_parametersContext procedure_call_parameters() {
			return getRuleContext(Procedure_call_parametersContext.class,0);
		}
		public Procedure_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterProcedure_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitProcedure_call(this);
		}
	}

	public final Procedure_callContext procedure_call() throws RecognitionException {
		Procedure_callContext _localctx = new Procedure_callContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_procedure_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(PROCEDURE_NAME);
			setState(124);
			procedure_call_parameters();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Procedure_call_parametersContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Procedure_call_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure_call_parameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterProcedure_call_parameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitProcedure_call_parameters(this);
		}
	}

	public final Procedure_call_parametersContext procedure_call_parameters() throws RecognitionException {
		Procedure_call_parametersContext _localctx = new Procedure_call_parametersContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_procedure_call_parameters);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(126);
					expression(0);
					}
					} 
				}
				setState(131);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ADD() { return getToken(BazilioParser.ADD, 0); }
		public AddContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterAdd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitAdd(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SubContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode SUB() { return getToken(BazilioParser.SUB, 0); }
		public SubContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterSub(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitSub(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParentesesContext extends ExpressionContext {
		public TerminalNode LEFT_PAREN() { return getToken(BazilioParser.LEFT_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BazilioParser.RIGHT_PAREN, 0); }
		public ParentesesContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterParenteses(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitParenteses(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MOD() { return getToken(BazilioParser.MOD, 0); }
		public ModContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitMod(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(BazilioParser.MUL, 0); }
		public MulContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterMul(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitMul(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ExpressionContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public VarContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitVar(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LtContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LT() { return getToken(BazilioParser.LT, 0); }
		public LtContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterLt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitLt(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ExpressionContext {
		public TerminalNode STRING() { return getToken(BazilioParser.STRING, 0); }
		public StringContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitString(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EqContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(BazilioParser.EQ, 0); }
		public EqContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterEq(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitEq(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GtContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GT() { return getToken(BazilioParser.GT, 0); }
		public GtContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterGt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitGt(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DivContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode DIV() { return getToken(BazilioParser.DIV, 0); }
		public DivContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterDiv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitDiv(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListSizeContext extends ExpressionContext {
		public List_sizeContext list_size() {
			return getRuleContext(List_sizeContext.class,0);
		}
		public ListSizeContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterListSize(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitListSize(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NoteContext extends ExpressionContext {
		public TerminalNode NOTE() { return getToken(BazilioParser.NOTE, 0); }
		public NoteContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterNote(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitNote(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ExpressionContext {
		public TerminalNode NUM() { return getToken(BazilioParser.NUM, 0); }
		public ValueContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitValue(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GteContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GTE() { return getToken(BazilioParser.GTE, 0); }
		public GteContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterGte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitGte(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListExprContext extends ExpressionContext {
		public List_expressionContext list_expression() {
			return getRuleContext(List_expressionContext.class,0);
		}
		public ListExprContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterListExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitListExpr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NeqContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode NEQ() { return getToken(BazilioParser.NEQ, 0); }
		public NeqContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterNeq(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitNeq(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LteContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LTE() { return getToken(BazilioParser.LTE, 0); }
		public LteContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterLte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitLte(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListQueryContext extends ExpressionContext {
		public List_queryContext list_query() {
			return getRuleContext(List_queryContext.class,0);
		}
		public ListQueryContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterListQuery(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitListQuery(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				_localctx = new ParentesesContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(133);
				match(LEFT_PAREN);
				setState(134);
				expression(0);
				setState(135);
				match(RIGHT_PAREN);
				}
				break;
			case 2:
				{
				_localctx = new VarContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(137);
				match(VAR);
				}
				break;
			case 3:
				{
				_localctx = new ValueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(138);
				match(NUM);
				}
				break;
			case 4:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(139);
				match(STRING);
				}
				break;
			case 5:
				{
				_localctx = new ListExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(140);
				list_expression();
				}
				break;
			case 6:
				{
				_localctx = new ListSizeContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(141);
				list_size();
				}
				break;
			case 7:
				{
				_localctx = new ListQueryContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(142);
				list_query();
				}
				break;
			case 8:
				{
				_localctx = new NoteContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(143);
				match(NOTE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(181);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(179);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new MulContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(146);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(147);
						match(MUL);
						setState(148);
						expression(19);
						}
						break;
					case 2:
						{
						_localctx = new DivContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(149);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(150);
						match(DIV);
						setState(151);
						expression(18);
						}
						break;
					case 3:
						{
						_localctx = new ModContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(152);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(153);
						match(MOD);
						setState(154);
						expression(17);
						}
						break;
					case 4:
						{
						_localctx = new AddContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(155);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(156);
						match(ADD);
						setState(157);
						expression(16);
						}
						break;
					case 5:
						{
						_localctx = new SubContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(158);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(159);
						match(SUB);
						setState(160);
						expression(15);
						}
						break;
					case 6:
						{
						_localctx = new LtContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(161);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(162);
						match(LT);
						setState(163);
						expression(14);
						}
						break;
					case 7:
						{
						_localctx = new LteContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(164);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(165);
						match(LTE);
						setState(166);
						expression(13);
						}
						break;
					case 8:
						{
						_localctx = new GtContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(167);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(168);
						match(GT);
						setState(169);
						expression(12);
						}
						break;
					case 9:
						{
						_localctx = new GteContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(170);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(171);
						match(GTE);
						setState(172);
						expression(11);
						}
						break;
					case 10:
						{
						_localctx = new EqContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(173);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(174);
						match(EQ);
						setState(175);
						expression(10);
						}
						break;
					case 11:
						{
						_localctx = new NeqContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(176);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(177);
						match(NEQ);
						setState(178);
						expression(9);
						}
						break;
					}
					} 
				}
				setState(183);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class List_sizeContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public List_sizeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_size; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterList_size(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitList_size(this);
		}
	}

	public final List_sizeContext list_size() throws RecognitionException {
		List_sizeContext _localctx = new List_sizeContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_list_size);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			match(T__11);
			setState(185);
			match(VAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class List_queryContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BazilioParser.VAR, 0); }
		public TerminalNode LEFT_BRACKET() { return getToken(BazilioParser.LEFT_BRACKET, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(BazilioParser.RIGHT_BRACKET, 0); }
		public List_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).enterList_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazilioListener ) ((BazilioListener)listener).exitList_query(this);
		}
	}

	public final List_queryContext list_query() throws RecognitionException {
		List_queryContext _localctx = new List_queryContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_list_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(VAR);
			setState(188);
			match(LEFT_BRACKET);
			setState(189);
			expression(0);
			setState(190);
			match(RIGHT_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 18);
		case 1:
			return precpred(_ctx, 17);
		case 2:
			return precpred(_ctx, 16);
		case 3:
			return precpred(_ctx, 15);
		case 4:
			return precpred(_ctx, 14);
		case 5:
			return precpred(_ctx, 13);
		case 6:
			return precpred(_ctx, 12);
		case 7:
			return precpred(_ctx, 11);
		case 8:
			return precpred(_ctx, 10);
		case 9:
			return precpred(_ctx, 9);
		case 10:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u00c1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0005\u00024\b\u0002\n\u0002\f\u00027\t\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003B\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0005\bR\b\b"+
		"\n\b\f\bU\t\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0003\ta\b\t\u0001\n\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0005\u000bk\b\u000b\n\u000b"+
		"\f\u000bn\t\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0005\u000f\u0080\b\u000f\n\u000f\f\u000f\u0083"+
		"\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0003\u0010\u0091\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005"+
		"\u0010\u00b4\b\u0010\n\u0010\f\u0010\u00b7\t\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0000\u0001 \u0013\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$\u0000\u0001\u0002\u0000"+
		"\u001a\u001a\u001c\u001c\u00cd\u0000)\u0001\u0000\u0000\u0000\u0002,\u0001"+
		"\u0000\u0000\u0000\u00045\u0001\u0000\u0000\u0000\u0006A\u0001\u0000\u0000"+
		"\u0000\bC\u0001\u0000\u0000\u0000\nG\u0001\u0000\u0000\u0000\fJ\u0001"+
		"\u0000\u0000\u0000\u000eM\u0001\u0000\u0000\u0000\u0010S\u0001\u0000\u0000"+
		"\u0000\u0012V\u0001\u0000\u0000\u0000\u0014b\u0001\u0000\u0000\u0000\u0016"+
		"h\u0001\u0000\u0000\u0000\u0018q\u0001\u0000\u0000\u0000\u001au\u0001"+
		"\u0000\u0000\u0000\u001c{\u0001\u0000\u0000\u0000\u001e\u0081\u0001\u0000"+
		"\u0000\u0000 \u0090\u0001\u0000\u0000\u0000\"\u00b8\u0001\u0000\u0000"+
		"\u0000$\u00bb\u0001\u0000\u0000\u0000&(\u0003\u0002\u0001\u0000\'&\u0001"+
		"\u0000\u0000\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000"+
		")*\u0001\u0000\u0000\u0000*\u0001\u0001\u0000\u0000\u0000+)\u0001\u0000"+
		"\u0000\u0000,-\u0005\u001b\u0000\u0000-.\u0003\u0010\b\u0000./\u0005\u001d"+
		"\u0000\u0000/0\u0003\u0004\u0002\u000001\u0005\u001e\u0000\u00001\u0003"+
		"\u0001\u0000\u0000\u000024\u0003\u0006\u0003\u000032\u0001\u0000\u0000"+
		"\u000047\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u000056\u0001\u0000"+
		"\u0000\u00006\u0005\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u0000"+
		"8B\u0003\b\u0004\u00009B\u0003\n\u0005\u0000:B\u0003\f\u0006\u0000;B\u0003"+
		"\u000e\u0007\u0000<B\u0003\u001c\u000e\u0000=B\u0003\u0012\t\u0000>B\u0003"+
		"\u0014\n\u0000?B\u0003\u0018\f\u0000@B\u0003\u001a\r\u0000A8\u0001\u0000"+
		"\u0000\u0000A9\u0001\u0000\u0000\u0000A:\u0001\u0000\u0000\u0000A;\u0001"+
		"\u0000\u0000\u0000A<\u0001\u0000\u0000\u0000A=\u0001\u0000\u0000\u0000"+
		"A>\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000A@\u0001\u0000\u0000"+
		"\u0000B\u0007\u0001\u0000\u0000\u0000CD\u0005\u001a\u0000\u0000DE\u0005"+
		"\u0001\u0000\u0000EF\u0003 \u0010\u0000F\t\u0001\u0000\u0000\u0000GH\u0005"+
		"\u0002\u0000\u0000HI\u0005\u001a\u0000\u0000I\u000b\u0001\u0000\u0000"+
		"\u0000JK\u0005\u0003\u0000\u0000KL\u0007\u0000\u0000\u0000L\r\u0001\u0000"+
		"\u0000\u0000MN\u0005\u0004\u0000\u0000NO\u0003 \u0010\u0000O\u000f\u0001"+
		"\u0000\u0000\u0000PR\u0005\u001a\u0000\u0000QP\u0001\u0000\u0000\u0000"+
		"RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000"+
		"\u0000T\u0011\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0005"+
		"\u0005\u0000\u0000WX\u0003 \u0010\u0000XY\u0005\u001d\u0000\u0000YZ\u0003"+
		"\u0004\u0002\u0000Z`\u0005\u001e\u0000\u0000[\\\u0005\u0006\u0000\u0000"+
		"\\]\u0005\u001d\u0000\u0000]^\u0003\u0004\u0002\u0000^_\u0005\u001e\u0000"+
		"\u0000_a\u0001\u0000\u0000\u0000`[\u0001\u0000\u0000\u0000`a\u0001\u0000"+
		"\u0000\u0000a\u0013\u0001\u0000\u0000\u0000bc\u0005\u0007\u0000\u0000"+
		"cd\u0003 \u0010\u0000de\u0005\u001d\u0000\u0000ef\u0003\u0004\u0002\u0000"+
		"fg\u0005\u001e\u0000\u0000g\u0015\u0001\u0000\u0000\u0000hl\u0005\b\u0000"+
		"\u0000ik\u0003 \u0010\u0000ji\u0001\u0000\u0000\u0000kn\u0001\u0000\u0000"+
		"\u0000lj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mo\u0001\u0000"+
		"\u0000\u0000nl\u0001\u0000\u0000\u0000op\u0005\t\u0000\u0000p\u0017\u0001"+
		"\u0000\u0000\u0000qr\u0005\u001a\u0000\u0000rs\u0005\n\u0000\u0000st\u0003"+
		" \u0010\u0000t\u0019\u0001\u0000\u0000\u0000uv\u0005\u000b\u0000\u0000"+
		"vw\u0005\u001a\u0000\u0000wx\u0005\u001f\u0000\u0000xy\u0003 \u0010\u0000"+
		"yz\u0005 \u0000\u0000z\u001b\u0001\u0000\u0000\u0000{|\u0005\u001b\u0000"+
		"\u0000|}\u0003\u001e\u000f\u0000}\u001d\u0001\u0000\u0000\u0000~\u0080"+
		"\u0003 \u0010\u0000\u007f~\u0001\u0000\u0000\u0000\u0080\u0083\u0001\u0000"+
		"\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000"+
		"\u0000\u0000\u0082\u001f\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000"+
		"\u0000\u0000\u0084\u0085\u0006\u0010\uffff\uffff\u0000\u0085\u0086\u0005"+
		"!\u0000\u0000\u0086\u0087\u0003 \u0010\u0000\u0087\u0088\u0005\"\u0000"+
		"\u0000\u0088\u0091\u0001\u0000\u0000\u0000\u0089\u0091\u0005\u001a\u0000"+
		"\u0000\u008a\u0091\u0005\u0019\u0000\u0000\u008b\u0091\u0005\u001c\u0000"+
		"\u0000\u008c\u0091\u0003\u0016\u000b\u0000\u008d\u0091\u0003\"\u0011\u0000"+
		"\u008e\u0091\u0003$\u0012\u0000\u008f\u0091\u0005\u0018\u0000\u0000\u0090"+
		"\u0084\u0001\u0000\u0000\u0000\u0090\u0089\u0001\u0000\u0000\u0000\u0090"+
		"\u008a\u0001\u0000\u0000\u0000\u0090\u008b\u0001\u0000\u0000\u0000\u0090"+
		"\u008c\u0001\u0000\u0000\u0000\u0090\u008d\u0001\u0000\u0000\u0000\u0090"+
		"\u008e\u0001\u0000\u0000\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0091"+
		"\u00b5\u0001\u0000\u0000\u0000\u0092\u0093\n\u0012\u0000\u0000\u0093\u0094"+
		"\u0005\u000f\u0000\u0000\u0094\u00b4\u0003 \u0010\u0013\u0095\u0096\n"+
		"\u0011\u0000\u0000\u0096\u0097\u0005\u0010\u0000\u0000\u0097\u00b4\u0003"+
		" \u0010\u0012\u0098\u0099\n\u0010\u0000\u0000\u0099\u009a\u0005\u0011"+
		"\u0000\u0000\u009a\u00b4\u0003 \u0010\u0011\u009b\u009c\n\u000f\u0000"+
		"\u0000\u009c\u009d\u0005\r\u0000\u0000\u009d\u00b4\u0003 \u0010\u0010"+
		"\u009e\u009f\n\u000e\u0000\u0000\u009f\u00a0\u0005\u000e\u0000\u0000\u00a0"+
		"\u00b4\u0003 \u0010\u000f\u00a1\u00a2\n\r\u0000\u0000\u00a2\u00a3\u0005"+
		"\u0012\u0000\u0000\u00a3\u00b4\u0003 \u0010\u000e\u00a4\u00a5\n\f\u0000"+
		"\u0000\u00a5\u00a6\u0005\u0013\u0000\u0000\u00a6\u00b4\u0003 \u0010\r"+
		"\u00a7\u00a8\n\u000b\u0000\u0000\u00a8\u00a9\u0005\u0014\u0000\u0000\u00a9"+
		"\u00b4\u0003 \u0010\f\u00aa\u00ab\n\n\u0000\u0000\u00ab\u00ac\u0005\u0015"+
		"\u0000\u0000\u00ac\u00b4\u0003 \u0010\u000b\u00ad\u00ae\n\t\u0000\u0000"+
		"\u00ae\u00af\u0005\u0016\u0000\u0000\u00af\u00b4\u0003 \u0010\n\u00b0"+
		"\u00b1\n\b\u0000\u0000\u00b1\u00b2\u0005\u0017\u0000\u0000\u00b2\u00b4"+
		"\u0003 \u0010\t\u00b3\u0092\u0001\u0000\u0000\u0000\u00b3\u0095\u0001"+
		"\u0000\u0000\u0000\u00b3\u0098\u0001\u0000\u0000\u0000\u00b3\u009b\u0001"+
		"\u0000\u0000\u0000\u00b3\u009e\u0001\u0000\u0000\u0000\u00b3\u00a1\u0001"+
		"\u0000\u0000\u0000\u00b3\u00a4\u0001\u0000\u0000\u0000\u00b3\u00a7\u0001"+
		"\u0000\u0000\u0000\u00b3\u00aa\u0001\u0000\u0000\u0000\u00b3\u00ad\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b0\u0001\u0000\u0000\u0000\u00b4\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b6!\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000"+
		"\u0000\u0000\u00b8\u00b9\u0005\f\u0000\u0000\u00b9\u00ba\u0005\u001a\u0000"+
		"\u0000\u00ba#\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005\u001a\u0000\u0000"+
		"\u00bc\u00bd\u0005\u001f\u0000\u0000\u00bd\u00be\u0003 \u0010\u0000\u00be"+
		"\u00bf\u0005 \u0000\u0000\u00bf%\u0001\u0000\u0000\u0000\n)5AS`l\u0081"+
		"\u0090\u00b3\u00b5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}