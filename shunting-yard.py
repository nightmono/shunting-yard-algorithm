precenders = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

def get_precedence(token):
    return precenders.get(token, 0)

def shunting_yard(tokens: list[str]):
    output = []
    operators = []

    for token in tokens:
        if token.isdigit():
            output.append(token)
        else:
            while operators and get_precedence(operators[-1]) >= get_precedence(token):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output

def tokenizer(stream):
    return stream.split()

def evaluate_postfix(expression: list[str]):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
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