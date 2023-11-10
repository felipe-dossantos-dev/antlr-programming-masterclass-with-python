// Generated from /workspaces/antlr-programming-masterclass-with-python/bazilio/Bazilio.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BazilioParser}.
 */
public interface BazilioListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BazilioParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(BazilioParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(BazilioParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#procedure}.
	 * @param ctx the parse tree
	 */
	void enterProcedure(BazilioParser.ProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#procedure}.
	 * @param ctx the parse tree
	 */
	void exitProcedure(BazilioParser.ProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#instructions}.
	 * @param ctx the parse tree
	 */
	void enterInstructions(BazilioParser.InstructionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#instructions}.
	 * @param ctx the parse tree
	 */
	void exitInstructions(BazilioParser.InstructionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#instruction}.
	 * @param ctx the parse tree
	 */
	void enterInstruction(BazilioParser.InstructionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#instruction}.
	 * @param ctx the parse tree
	 */
	void exitInstruction(BazilioParser.InstructionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#assigment}.
	 * @param ctx the parse tree
	 */
	void enterAssigment(BazilioParser.AssigmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#assigment}.
	 * @param ctx the parse tree
	 */
	void exitAssigment(BazilioParser.AssigmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#input_}.
	 * @param ctx the parse tree
	 */
	void enterInput_(BazilioParser.Input_Context ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#input_}.
	 * @param ctx the parse tree
	 */
	void exitInput_(BazilioParser.Input_Context ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#output_}.
	 * @param ctx the parse tree
	 */
	void enterOutput_(BazilioParser.Output_Context ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#output_}.
	 * @param ctx the parse tree
	 */
	void exitOutput_(BazilioParser.Output_Context ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#reproduction}.
	 * @param ctx the parse tree
	 */
	void enterReproduction(BazilioParser.ReproductionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#reproduction}.
	 * @param ctx the parse tree
	 */
	void exitReproduction(BazilioParser.ReproductionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(BazilioParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(BazilioParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(BazilioParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(BazilioParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#while_}.
	 * @param ctx the parse tree
	 */
	void enterWhile_(BazilioParser.While_Context ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#while_}.
	 * @param ctx the parse tree
	 */
	void exitWhile_(BazilioParser.While_Context ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(BazilioParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(BazilioParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#list_add}.
	 * @param ctx the parse tree
	 */
	void enterList_add(BazilioParser.List_addContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#list_add}.
	 * @param ctx the parse tree
	 */
	void exitList_add(BazilioParser.List_addContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#list_cut}.
	 * @param ctx the parse tree
	 */
	void enterList_cut(BazilioParser.List_cutContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#list_cut}.
	 * @param ctx the parse tree
	 */
	void exitList_cut(BazilioParser.List_cutContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#procedure_call}.
	 * @param ctx the parse tree
	 */
	void enterProcedure_call(BazilioParser.Procedure_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#procedure_call}.
	 * @param ctx the parse tree
	 */
	void exitProcedure_call(BazilioParser.Procedure_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#procedure_call_parameters}.
	 * @param ctx the parse tree
	 */
	void enterProcedure_call_parameters(BazilioParser.Procedure_call_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#procedure_call_parameters}.
	 * @param ctx the parse tree
	 */
	void exitProcedure_call_parameters(BazilioParser.Procedure_call_parametersContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Add}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAdd(BazilioParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Add}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAdd(BazilioParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Sub}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterSub(BazilioParser.SubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Sub}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitSub(BazilioParser.SubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parenteses}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParenteses(BazilioParser.ParentesesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parenteses}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParenteses(BazilioParser.ParentesesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMod(BazilioParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMod(BazilioParser.ModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMul(BazilioParser.MulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMul(BazilioParser.MulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Var}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterVar(BazilioParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Var}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitVar(BazilioParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Lt}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLt(BazilioParser.LtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Lt}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLt(BazilioParser.LtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code String}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterString(BazilioParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code String}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitString(BazilioParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Eq}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterEq(BazilioParser.EqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Eq}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitEq(BazilioParser.EqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Gt}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGt(BazilioParser.GtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Gt}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGt(BazilioParser.GtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Div}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterDiv(BazilioParser.DivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Div}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitDiv(BazilioParser.DivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ListSize}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterListSize(BazilioParser.ListSizeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ListSize}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitListSize(BazilioParser.ListSizeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Note}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNote(BazilioParser.NoteContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Note}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNote(BazilioParser.NoteContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Value}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterValue(BazilioParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Value}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitValue(BazilioParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Gte}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGte(BazilioParser.GteContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Gte}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGte(BazilioParser.GteContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Neq}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNeq(BazilioParser.NeqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Neq}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNeq(BazilioParser.NeqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Lte}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLte(BazilioParser.LteContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Lte}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLte(BazilioParser.LteContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ListQuery}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterListQuery(BazilioParser.ListQueryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ListQuery}
	 * labeled alternative in {@link BazilioParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitListQuery(BazilioParser.ListQueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#list_size}.
	 * @param ctx the parse tree
	 */
	void enterList_size(BazilioParser.List_sizeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#list_size}.
	 * @param ctx the parse tree
	 */
	void exitList_size(BazilioParser.List_sizeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazilioParser#list_query}.
	 * @param ctx the parse tree
	 */
	void enterList_query(BazilioParser.List_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazilioParser#list_query}.
	 * @param ctx the parse tree
	 */
	void exitList_query(BazilioParser.List_queryContext ctx);
}