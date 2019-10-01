import operator as op
import re

"""
Logic of calculator:
It takes a string then using a lookup table it generates tokens such as NUMBER:4 ADD:- etc.
Then I consumes this tokens in a LL(1) fashion, If I am remembering the name of the parser correctly.

Parser Rules
LOW_PRECEDENCE -> HI_PRECEDENCE (ADD HI_PRECEDENCE)*
ADD -> + | -
HI_PRECEDENCE -> UNIT (MUL UNIT)*
MUL -> * | /
UNIT -> NUMBER | NEGATIVE | ( LOW_PRECEDENCE )
NEGATIVE -> ADD NUMBER | ADD ( LOW_PRECEDENCE )

I didn't want to generate a Operation tree from and then calculate the result,
So I calculated in between values inside of parser directly. 
"""

UNIT = "UNIT"
NEGATIVE = "NEGATIVE"
NUMBER = "NUMBER"
LEFT = "LEFT"
RIGHT = "RIGHT"
ADD = "ADD"
MUL = "MUL"
LOW_PRECEDENCE = "LOW_PRECEDENCE"
HI_PRECEDENCE = "HI_PRECEDENCE"
EOF = "END_OF_FILE"


# Custom cast function to make the casting act like JS Numbers.
def cast_to_number(string: str):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            raise ValueError("String is not a number.")


# Custom tuple class to hold Tokens.
# It detect the type of token based on a look up table.
# If something is invalid it will trigger an Exception while trying to cast it to a Number.
class Token:
    lut = {"(": LEFT, ")": RIGHT, "*": MUL, "/": MUL, "-": ADD, "+": ADD}

    def __init__(self, value, type=None):
        if type is None:
            self.type = self.lut.get(value, "NUMBER")
        else:
            self.type = type

        if self.type == NUMBER:
            self.value = cast_to_number(value)
        else:
            self.value = value

    def __repr__(self):
        return "%s:'%s'" % (self.type, self.value)


# Calculator class is the main parser class.
# It goes through list of tokens, and can be reused. You don't have to re-init for every expression.
# Parser rules are on the top of the file.
class Calculator:
    lut = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv
    }

    token_pattern = r'[.\d]+|[\d.\d]+|[\d]+|[\+|\-|\/|\*|\(|\)|]'

    def __init__(self):
        self.tokens = None
        self.current = None

    # The exposed function to be used by the user.
    def calculate(self, expression):
        if type(expression) is not str:
            raise TypeError("Expression must be a string.")

        self.tokens = iter([Token(token) for token in re.findall(self.token_pattern, expression)])

        try:
            self.current = next(self.tokens)
        except StopIteration:
            if expression:
                raise TypeError("Not a expression.")
            return 0

        result = self.__low_precedence()

        if self.current.type == EOF:
            return result
        else:
            raise ArithmeticError("Invalid Expression.")

    # This function does the last check before the token is consumed and Checks the end of the iteration.
    def __consume(self, token_type):
        if token_type == self.current.type:
            try:
                self.current = next(self.tokens)
            except StopIteration:
                self.current = Token(EOF, EOF)
        else:
            raise ArithmeticError("Invalid Expression.")

    # Handler for addition and subtraction.
    def __low_precedence(self):
        result = self.__hi_precedence()

        while self.current.type == ADD:
            operator = self.current.value
            self.__consume(ADD)
            result = self.lut[operator](result, self.__hi_precedence())

        return result

    # Handler for multiplication and division.
    def __hi_precedence(self):
        result = self.__unit()

        while self.current.type == MUL:
            operator = self.current.value
            self.__consume(MUL)
            result = self.lut[operator](result, self.__unit())

        return result

    # Handler for numbers and parentheses. Bypass for negatives.
    def __unit(self):
        if self.current.type == NUMBER:
            result = self.current.value
            self.__consume(NUMBER)
            return result

        if self.current.type == ADD:
            return self.__negative()

        if self.current.type == LEFT:
            self.__consume(LEFT)
            result = self.__low_precedence()
            self.__consume(RIGHT)
            return result

        raise ArithmeticError("Expression is not valid.")
    # Handler for negative numbers or negative parentheses.
    def __negative(self):
        result = 0
        operand = self.current.value

        self.__consume(ADD)

        if self.current.type == NUMBER:
            result = self.current.value
            self.__consume(NUMBER)
        if self.current.type == LEFT:
            self.__consume(LEFT)
            result = self.__low_precedence()
            self.__consume(RIGHT)

        return self.lut[operand](0, result)
