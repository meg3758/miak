# Generated from C:/Users/mcebu/PycharmProjects/miak/pseudocode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pseudocodeParser import pseudocodeParser
else:
    from pseudocodeParser import pseudocodeParser

# This class defines a complete generic visitor for a parse tree produced by pseudocodeParser.

class pseudocodeVisitor(ParseTreeVisitor):
    def __int__(self):
        self.code = ""
        self.tabs = 0
    def add_to_code(self,token,name):
        name = str(name)
        if token == "ASSIGN":
            self.code += "="

        elif token in ("COMPARE_SYM", "MATH_SYM"):
            if name == "=":
                name = "=="
            self.code += name

        elif token == "FUNCTION":
            self.code += "def "

        elif token == "C_BRACKET_OPEN":
            self.code += ":\n"
            self.tabs += 1
            self.code += self.tabs * 4 * " "

        elif token == "CURLY_BRACKET_END":
            self.code = self.code[:-4]
            self.tabs -= 1

        elif token == "SEMICOLON":
            self.code += "\n"
            self.code += " " * 4 * self.tabs

        elif token == "BOOL":
            if name == "true":
                self.code += "TRUE"
            if name == "false":
                self.code += "FALSE"

        elif token in ["IF", "FOR", "OR", "AND", "NOT",
                       "RETURN", "FUNCTION"]:
            self.code += name + " "

        else:
            self.code += name
    # Visit a parse tree produced by pseudocodeParser#program.
    def visitProgram(self, ctx:pseudocodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#array.
    def visitArray(self, ctx:pseudocodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#type.
    def visitType(self, ctx:pseudocodeParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#declaration.
    def visitDeclaration(self, ctx:pseudocodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#if_statement.
    def visitIf_statement(self, ctx:pseudocodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#for_statement.
    def visitFor_statement(self, ctx:pseudocodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#while_statement.
    def visitWhile_statement(self, ctx:pseudocodeParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#statement.
    def visitStatement(self, ctx:pseudocodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#expr.
    def visitExpr(self, ctx:pseudocodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#divisibility.
    def visitDivisibility(self, ctx:pseudocodeParser.DivisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#return_statement.
    def visitReturn_statement(self, ctx:pseudocodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#function_def.
    def visitFunction_def(self, ctx:pseudocodeParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#function.
    def visitFunction(self, ctx:pseudocodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudocodeParser#array_elem.
    def visitArray_elem(self, ctx:pseudocodeParser.Array_elemContext):
        return self.visitChildren(ctx)



del pseudocodeParser