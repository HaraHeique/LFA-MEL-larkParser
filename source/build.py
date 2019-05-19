'''
    Responsável pela execução principal do programa
'''

from models.LarkParserMEL import LarkParserMEL

def main():
    parserMEL: LarkParserMEL = LarkParserMEL()

    while True:
        inputExpression: str = input("Enter your math expression: ")
        isValidExpr: bool = parserMEL.checkExpression(inputExpression)
        strIsValidExpr: str = "valid" if isValidExpr else "invalid"
        
        print("Expression {0} is {1}.".format(inputExpression, strIsValidExpr))
        print()

    return 0

if __name__ == '__main__' :
    main()