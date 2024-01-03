from antlr4 import*
from gen.pseudocodeLexer import pseudocodeLexer
from gen.pseudocodeParser import pseudocodeParser
from gen.pseudocodeVisitor import pseudocodeVisitor

pseudocode = '''
x:=3;
if(x = 6){
    y=6
}'''
if __name__ == '__main__':
    input_stream = InputStream(pseudocode)
    lexer = pseudocodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = pseudocodeParser(token_stream)
    tree = parser.program()
    visitor = pseudocodeVisitor()
    visitor.visit(tree)


