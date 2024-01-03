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

    def add_to_code(self, token, name):
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

        elif token == "C_BRACKET_CLOSE":
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
    def visitProgram(self, ctx: pseudocodeParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by pseudocodeParser#array.
    def visitArray(self, ctx: pseudocodeParser.ArrayContext):
        token = ctx.getToken(pseudocodeParser.S_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code("S_BRACKET_OPEN", token)
        node = ctx
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)
            if i == 0 or i == n - 1 or i % 2 != 0:
                continue
            self.add_to_code('COMMA', ',')

        token = ctx.getToken(pseudocodeParser.S_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code('S_BRACKET_CLOSE', token)

    # Visit a parse tree produced by pseudocodeParser#type.
    def visitType(self, ctx: pseudocodeParser.TypeContext):
        token = ctx.getToken(pseudocodeParser.BOOL, 0)
        if token != None:
            self.add_to_code('BOOL', token)

        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.NUMBER, 0)
        if token != None:
            self.add_to_code('NUMBER', token)

        token = ctx.getToken(pseudocodeParser.STRING, 0)
        if token != None:
            self.add_to_code('STRING', token)

        res = self.visitChildren(ctx)

        return res

    # Visit a parse tree produced by pseudocodeParser#declaration.
    def visitDeclaration(self, ctx: pseudocodeParser.DeclarationContext):
        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.S_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code('S_BRACKET_OPEN', token)

        token = ctx.getToken(pseudocodeParser.NUMBER, 0)
        if token != None:
            self.add_to_code('NUMBER', token)

        token = ctx.getToken(pseudocodeParser.S_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code('S_BRACKET_CLOSE', token)

        token = ctx.getToken(pseudocodeParser.ASSIGN, 0)
        if token != None:
            self.add_to_code('ASSIGN', token)

        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudocodeParser.SEMICOLON, 0)
        if token != None:
            self.add_to_code('SEMICOLON', token)

        return res

    # Visit a parse tree produced by pseudocodeParser#if_statement.
    def visitIf_statement(self, ctx: pseudocodeParser.If_statementContext):
        token = ctx.getToken(pseudocodeParser.IF, 0)
        if token != None:
            self.add_to_code("IF", token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_OPEN, 0)
        if token != None:
            # self.add_to_code("R_BRACKET_OPEN", token)
            pass
        c = ctx.getChild(2)
        c.accept(self)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_CLOSE, 0)
        if token != None:
            # self.add_to_code("R_BRACKET_CLOSE", token)
            pass
        token = ctx.getToken(pseudocodeParser.C_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code("C_BRACKET_OPEN", token)

        c = ctx.getChild(5)
        c.accept(self)

        token = ctx.getToken(pseudocodeParser.C_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code("C_BRACKET_CLOSE", token)

    # Visit a parse tree produced by pseudocodeParser#for_statement.
    def visitFor_statement(self, ctx: pseudocodeParser.For_statementContext):
        token = ctx.getToken(pseudocodeParser.FOR, 0)
        if token != None:
            self.add_to_code("FOR", token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_OPEN, 0)
        if token != None:
            # self.add_to_code("R_BRACKET_OPEN", token)
            pass

        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code("ID", token)

        self.code += " in range("

        id_ctr = 1
        token = ctx.getToken(pseudocodeParser.ID, id_ctr)
        if token != None:
            id_ctr += 1
            self.add_to_code("ID", token)

        nr_ctr = 0
        token = ctx.getToken(pseudocodeParser.NUMBER, nr_ctr)
        if token != None:
            nr_ctr += 1
            self.add_to_code("NUMBER", token)

        self.code += ","

        token = ctx.getToken(pseudocodeParser.ID, id_ctr)
        if token != None:
            self.add_to_code("ID", token)

        token = ctx.getToken(pseudocodeParser.NUMBER, nr_ctr)
        if token != None:
            self.add_to_code("NUMBER", token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code("R_BRACKET_CLOSE", token)

        token = ctx.getToken(pseudocodeParser.C_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code("C_BRACKET_OPEN", token)

        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudocodeParser.C_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code("C_BRACKET_CLOSE", token)

    # Visit a parse tree produced by pseudocodeParser#while_statement.
    def visitWhile_statement(self, ctx: pseudocodeParser.While_statementContext):
        token = ctx.getToken(pseudocodeParser.WHILE, 0)
        if token != None:
            self.add_to_code("WHILE", token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_OPEN, 0)
        if token != None:
            # self.add_to_code("R_BRACKET_OPEN", token)
            pass
        c = ctx.getChild(2)
        c.accept(self)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_CLOSE, 0)
        if token != None:
            # self.add_to_code("R_BRACKET_CLOSE", token)
            pass
        token = ctx.getToken(pseudocodeParser.C_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code("C_BRACKET_OPEN", token)

        c = ctx.getChild(5)
        c.accept(self)

        token = ctx.getToken(pseudocodeParser.C_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code("C_BRACKET_CLOSE", token)

    # Visit a parse tree produced by pseudocodeParser#statement.
    def visitStatement(self, ctx: pseudocodeParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by pseudocodeParser#expr.
    def visitExpr(self, ctx: pseudocodeParser.ExprContext):
        flag = 0
        token = ctx.getToken(pseudocodeParser.NOT, 0)
        if token != None:
            self.add_to_code('NOT', token)
            flag += 1

        c = ctx.getChild(flag)
        c.accept(self)

        token = ctx.getToken(pseudocodeParser.AND, 0)
        if token != None:
            self.add_to_code('AND', token)

        token = ctx.getToken(pseudocodeParser.OR, 0)
        if token != None:
            self.add_to_code('OR', token)

        token = ctx.getToken(pseudocodeParser.MATH_SYM, 0)
        if token != None:
            self.add_to_code('MATH_SYM', token)

        token = ctx.getToken(pseudocodeParser.COMPARE_SYM, 0)
        if token != None:
            self.add_to_code('COMPARE_SYM', token)

        c = ctx.getChild(2 + flag)
        c.accept(self)

    # Visit a parse tree produced by pseudocodeParser#divisibility.
    def visitDivisibility(self, ctx: pseudocodeParser.DivisibilityContext):
        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.NUMBER, 0)
        if token != None:
            self.add_to_code('NUMBER', token)

        token = ctx.getToken(pseudocodeParser.IS, 0)
        if token != None:
            self.add_to_code('is', token)

        token = ctx.getToken(pseudocodeParser.DIVISIBLE, 0)
        if token != None:
            self.add_to_code('DIVISIBLE', token)

        token = ctx.getToken(pseudocodeParser.BY, 0)
        if token != None:
            self.add_to_code('BY', token)

        token = ctx.getToken(pseudocodeParser.NUMBER, 0)
        if token != None:
            self.add_to_code('NUMBER', token)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by pseudocodeParser#return_statement.
    def visitReturn_statement(self, ctx: pseudocodeParser.Return_statementContext):
        token = ctx.getToken(pseudocodeParser.RETURN, 0)
        if token != None:
            self.add_to_code("RETURN", token)

        token = ctx.getToken(pseudocodeParser.SEMICOLON, 0)
        if token != None:
            self.add_to_code("SEMICOLON", token)

    # Visit a parse tree produced by pseudocodeParser#function_def.
    def visitFunction_def(self, ctx: pseudocodeParser.Function_defContext):
        token = ctx.getToken(pseudocodeParser.FUNCTION, 0)
        if token != None:
            self.add_to_code('FUNCTION', token)

        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code('R_BRACKET_OPEN', token)

        token = ctx.getToken(pseudocodeParser.ID, 1)
        if token != None:
            self.add_to_code('ID', token)

        id_ctr = 2
        comma_ctr = 0
        while token != None:
            token = ctx.getToken(pseudocodeParser.COMMA, comma_ctr)
            comma_ctr += 1
            if token == None:
                break
            self.add_to_code('COMMA', token)
            token = ctx.getToken(pseudocodeParser.ID, id_ctr)
            id_ctr += 1
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code('R_BRACKET_CLOSE', token)

        token = ctx.getToken(pseudocodeParser.C_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code('C_BRACKET_OPEN', token)

        res = self.visitChildren(ctx)
        token = ctx.getToken(pseudocodeParser.C_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code('C_BRACKET_CLOSE', token)
        return res

    # Visit a parse tree produced by pseudocodeParser#function.
    def visitFunction(self, ctx: pseudocodeParser.FunctionContext):

        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.R_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code('R_BRACKET_OPEN', token)

        node = ctx
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)
            if i == 0 or i == n - 1 or i == n - 3 or i % 2 != 0:
                continue
            self.add_to_code('COMMA', ',')

        token = ctx.getToken(pseudocodeParser.R_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code('R_BRACKET_CLOSE', token)

        token = ctx.getToken(pseudocodeParser.SEMICOLON, 0)
        if token != None:
            self.add_to_code('SEMICOLON', token)

    # Visit a parse tree produced by pseudocodeParser#array_elem.
    def visitArray_elem(self, ctx: pseudocodeParser.Array_elemContext):
        token = ctx.getToken(pseudocodeParser.ID, 0)
        if token != None:
            self.add_to_code('ID', token)

        token = ctx.getToken(pseudocodeParser.S_BRACKET_OPEN, 0)
        if token != None:
            self.add_to_code('S_BRACKET_OPEN', token)
        res = self.visitChildren(ctx)
        token = ctx.getToken(pseudocodeParser.S_BRACKET_CLOSE, 0)
        if token != None:
            self.add_to_code('S_BRACKET_CLOSE', token)

        return res


del pseudocodeParser
