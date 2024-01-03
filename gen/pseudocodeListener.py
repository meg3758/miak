# Generated from C:/Users/fuska/PycharmProjects/miak2/pseudocode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pseudocodeParser import pseudocodeParser
else:
    from pseudocodeParser import pseudocodeParser

# This class defines a complete listener for a parse tree produced by pseudocodeParser.
class pseudocodeListener(ParseTreeListener):

    # Enter a parse tree produced by pseudocodeParser#program.
    def enterProgram(self, ctx:pseudocodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#program.
    def exitProgram(self, ctx:pseudocodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#increment.
    def enterIncrement(self, ctx:pseudocodeParser.IncrementContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#increment.
    def exitIncrement(self, ctx:pseudocodeParser.IncrementContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#array.
    def enterArray(self, ctx:pseudocodeParser.ArrayContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#array.
    def exitArray(self, ctx:pseudocodeParser.ArrayContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#type.
    def enterType(self, ctx:pseudocodeParser.TypeContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#type.
    def exitType(self, ctx:pseudocodeParser.TypeContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#declaration.
    def enterDeclaration(self, ctx:pseudocodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#declaration.
    def exitDeclaration(self, ctx:pseudocodeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#if_statement.
    def enterIf_statement(self, ctx:pseudocodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#if_statement.
    def exitIf_statement(self, ctx:pseudocodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#for_statement.
    def enterFor_statement(self, ctx:pseudocodeParser.For_statementContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#for_statement.
    def exitFor_statement(self, ctx:pseudocodeParser.For_statementContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#while_statement.
    def enterWhile_statement(self, ctx:pseudocodeParser.While_statementContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#while_statement.
    def exitWhile_statement(self, ctx:pseudocodeParser.While_statementContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#statement.
    def enterStatement(self, ctx:pseudocodeParser.StatementContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#statement.
    def exitStatement(self, ctx:pseudocodeParser.StatementContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#expr.
    def enterExpr(self, ctx:pseudocodeParser.ExprContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#expr.
    def exitExpr(self, ctx:pseudocodeParser.ExprContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#divisibility.
    def enterDivisibility(self, ctx:pseudocodeParser.DivisibilityContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#divisibility.
    def exitDivisibility(self, ctx:pseudocodeParser.DivisibilityContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#return_statement.
    def enterReturn_statement(self, ctx:pseudocodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#return_statement.
    def exitReturn_statement(self, ctx:pseudocodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#function_def.
    def enterFunction_def(self, ctx:pseudocodeParser.Function_defContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#function_def.
    def exitFunction_def(self, ctx:pseudocodeParser.Function_defContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#function.
    def enterFunction(self, ctx:pseudocodeParser.FunctionContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#function.
    def exitFunction(self, ctx:pseudocodeParser.FunctionContext):
        pass


    # Enter a parse tree produced by pseudocodeParser#array_elem.
    def enterArray_elem(self, ctx:pseudocodeParser.Array_elemContext):
        pass

    # Exit a parse tree produced by pseudocodeParser#array_elem.
    def exitArray_elem(self, ctx:pseudocodeParser.Array_elemContext):
        pass



del pseudocodeParser