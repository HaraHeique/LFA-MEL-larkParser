# -*- coding: utf-8 -*-

'''
    Classe responsável por realizar o parser da expressão passada como entrada seguindo
    as regras definidas pela gramática da linguagem utilizando a lib Lark disponível no 
    gerenciador de pacotes pip.
'''

from lark import Lark

# Constante do módulo definindo a gramática a ser utilizada utilizando a sintaxe Lark + EBNF
_MELGRAMMAR: str = """
    expr: term (("+" | "-") term)*
    term: factor (("*" | "/" | "//" | "%") factor)*
    factor: base ("^" factor)?
    base: ("+" | "-") base | NUMBER | "(" expr ")"

    %import common.SIGNED_NUMBER -> NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

class LarkParserMEL:
    def __init__(self):
        self._inputExpr: str = ""
        self._parser: Lark = Lark(_MELGRAMMAR, start='expr')

    @property
    def expression(self) -> str:
        return self._inputExpr

    def checkExpression(self, inputExpr: str) -> bool:
        '''Checa se a expressão de entrada é válida de acordo com a gramática MEL definida'''
        
        self._inputExpr = inputExpr

        # Usa a instancia do parser e cria a sua árvore parser de execução
        isValidExpr: bool = True
        try:
            self._parser.parse(inputExpr)
        except Exception:
            isValidExpr = False
        finally:
            return isValidExpr


# Para testes unitário do módulo
if __name__ == '__main__' :
    parserMEL: LarkParserMEL = LarkParserMEL()
    expressions: list = ["",
                         "1",
                         "-12.32",
                         "2 + 2",
                         "2-///",
                         "3 * 23",
                         "3 - 2 * 7",
                         "2 // 20",
                         "++++++2 - 4.0 / ----1.",
                         "34 + 213 + 2.12 / 21",
                         "10 * 5 + 100 / 10 - 5 + 7 % 2",
                         "(10) * 5 + (100 // 10) - 5 + (7 % 2)",
                         "-((2+2)*2)-((2-0)+2)",
                         "(2.*(2.0+2.))-(2.0+(2.-0))",
                         "(2.*(2.0+2.))-(2.0+(2.-0)))",
                         "-(100) + 21 / (43 % 2)",
                         "3^4+5*(2-5)",
                         "3^2+5//(2-5)",
                         "x = 2 adsamldk",
                         "2^2^2^-2",
                         "0.02e2 + 0.02e-2",
                         "8^-2 + 2E1 * 2e-1 + 3e+3 / 2.012",
                         "8^2 + 2E1 * 2e-1 + 3e+3 // 2.",
                         "(-2.3)^2 + 2.2E1 * 2e-12 + 1e+3",
                         "2-((2=)",
                         "2^^3-2",
                         "2Ee-2"]

    for expr in expressions:
        # = True a expressão é válida; = False expressão inválida
        print("Expression: {0} = {1}".format(expr, parserMEL.checkExpression(expr)))