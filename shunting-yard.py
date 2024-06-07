precenders = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

def get_precedence(token):
    return precenders.get(token, 0)

def isdigit(token):
    """Custom isdigit function that supports negative and decimal numbers."""
    return token.replace(".", "").replace("-", "").isdigit()

def shunting_yard(tokens: list[str]):
    output = []
    operators = []

    for token in tokens:
        if isdigit(token):
            output.append(token)
        elif token in "+-*/":
            while operators and get_precedence(operators[-1]) >= get_precedence(token):
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append("(")
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            # Pop open bracket
            operators.pop()

    while operators:
        output.append(operators.pop())

    return output

def tokenizer(stream):
    return stream.split()

def evaluate_postfix(expression: list[str]):
    stack = []

    for token in expression:
        if isdigit(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b

            stack.append(result)

    return stack

exp1 = shunting_yard(tokenizer("1 + 2 * 4"))
exp2 = shunting_yard(tokenizer("2 * 3 / 2 + 2"))

print(evaluate_postfix(exp1))
print(evaluate_postfix(exp2))

while 1:
    text_stream = input("Text stream: ")
    exp = shunting_yard(tokenizer(text_stream))
    print(exp)
    print(evaluate_postfix(exp))