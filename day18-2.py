from dataclasses import dataclass
import re

from aoc import get_input

# thanks to https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing


def expression(rbp=0):
    global token
    t = token
    token = next(tokens)
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = next(tokens)
        left = t.led(left)

    return left


def match(tok=None):
    global token
    if tok and tok != type(token):
        raise SyntaxError('Expected %s' % tok)
    token = next(tokens)


@dataclass
class LiteralToken(object):
    value: int
    def nud(self):
        return self.value


class OperatorAddToken(object):
    lbp = 10
    def led(self, left):
        right = expression(10)
        return left + right


class OperatorAddToken2(object):
    lbp = 20
    def led(self, left):
        right = expression(20)
        return left + right


class OperatorMulToken(object):
    lbp = 10
    def led(self, left):
        return left * expression(10)


class OperatorLParenToken(object):
    lbp = 0
    def nud(self):
        expr = expression()
        match(OperatorRParenToken)
        return expr


class OperatorRParenToken(object):
    lbp = 0


class EndToken(object):
    lbp = 0


token_pat = re.compile("\s*(?:(\d+)|(.))")
def tokenize(program, problem):
    for number, operator in token_pat.findall(program):
        if number:
            yield LiteralToken(int(number))
        elif operator == "+":
            if problem == 1:
                yield OperatorAddToken()
            elif problem == 2:
                yield OperatorAddToken2()
        elif operator == "*":
            yield OperatorMulToken()
        elif operator == '(':
            yield OperatorLParenToken()
        elif operator == ')':
            yield OperatorRParenToken()
        else:
            raise SyntaxError('unknown operator: %s', operator)
    yield EndToken()


def parse(program, problem):
    global token, tokens
    tokens = tokenize(program, problem)
    token = next(tokens)
    return expression()


equations = get_input(day=18)
print(sum(parse(equation, problem=1) for equation in equations))
print(sum(parse(equation, problem=2) for equation in equations))
