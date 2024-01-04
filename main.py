from antlr4 import*
from gen.pseudocodeLexer import pseudocodeLexer
from gen.pseudocodeParser import pseudocodeParser
from gen.pseudocodeVisitor import pseudocodeVisitor

pseudocode = '''
x := 3;
i := 2;
x := i + 1;
function add(x,y){
    x := x + y;
    return x;
}
while(i < 10) {
    add(x,1);
}
for ( k := 40...50 ){
    function func_1(x){
        return x;
        }
    func_1(k);
    }
array := [1,2,3];
array[2] := 5;
if(x < 5){
    x := 6;
}
else{
    x := 4;
}
while(x < 1000){
    for(i := 1...10){
        add(x,5);
    }
}
'''
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


