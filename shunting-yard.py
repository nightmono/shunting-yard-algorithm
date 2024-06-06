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

print(shunting_yard(tokenizer("1 + 2 * 4")))
print(shunting_yard(tokenizer("1 + 3 / 2 - 4")))