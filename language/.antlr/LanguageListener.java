// Generated from /workspaces/antlr/language/Language.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LanguageParser}.
 */
public interface LanguageListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LanguageParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(LanguageParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(LanguageParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#inss}.
	 * @param ctx the parse tree
	 */
	void enterInss(LanguageParser.InssContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#inss}.
	 * @param ctx the parse tree
	 */
	void exitInss(LanguageParser.InssContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#ins}.
	 * @param ctx the parse tree
	 */
	void enterIns(LanguageParser.InsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#ins}.
	 * @param ctx the parse tree
	 */
	void exitIns(LanguageParser.InsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#output}.
	 * @param ctx the parse tree
	 */
	void enterOutput(LanguageParser.OutputContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#output}.
	 * @param ctx the parse tree
	 */
	void exitOutput(LanguageParser.OutputContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(LanguageParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(LanguageParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link LanguageParser#while_}.
	 * @param ctx the parse tree
	 */
	void enterWhile_(LanguageParser.While_Context ctx);
	/**
	 * Exit a parse tree produced by {@link LanguageParser#while_}.
	 * @param ctx the parse tree
	 */
	void exitWhile_(LanguageParser.While_Context ctx);
	/**
	 * Enter a parse tree produced by the {@code Sub}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSub(LanguageParser.SubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Sub}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSub(LanguageParser.SubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Var}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVar(LanguageParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Var}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVar(LanguageParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Value}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterValue(LanguageParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Value}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitValue(LanguageParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Lt}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLt(LanguageParser.LtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Lt}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLt(LanguageParser.LtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Sum}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSum(LanguageParser.SumContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Sum}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSum(LanguageParser.SumContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Neq}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNeq(LanguageParser.NeqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Neq}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNeq(LanguageParser.NeqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Eq}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterEq(LanguageParser.EqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Eq}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitEq(LanguageParser.EqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Gt}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterGt(LanguageParser.GtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Gt}
	 * labeled alternative in {@link LanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitGt(LanguageParser.GtContext ctx);
}