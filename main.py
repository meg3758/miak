from antlr4 import*
from gen.pseudocodeLexer import pseudocodeLexer
from gen.pseudocodeParser import pseudocodeParser
from gen.pseudocodeVisitor import pseudocodeVisitor

pseudocode = '''
i:=3;
i := i + 1;

while(i < 10) {
    function add(x,y){
    x := x + y;
}
}
for ( i := 40...50 ){
    function func_1(x, y){
        x:=4;
        }
    }'''
if __name__ == '__main__':
    input_stream = InputStream(pseudocode)
    lexer = pseudocodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = pseudocodeParser(token_stream)
    tree = parser.program()
    visitor = pseudocodeVisitor()
    visitor.visit(tree)
    with open('code.py', 'w') as file:
        file.write(visitor.code)


