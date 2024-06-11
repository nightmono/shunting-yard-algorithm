def handle_whitespace(stream, head):
    while head < len(stream) and stream[head] == " ":
        head += 1
    return head

def handle_number(stream, tokens, current, head):
    while head < len(stream) and stream[head] in ".0123456789":
        head += 1
    tokens.append(stream[current:head])
    return head

def handle_one_char(stream, tokens, current):
    tokens.append(stream[current])
    return current + 1

def handle_string(stream, tokens, current, head):
    while head < len(stream) and stream[head] not in "'\"":
        head += 1
    tokens.append(stream[current+1:head])
    # Avoid handing the ending quote/speech mark
    return head + 1

def handle_func(stream, tokens, funcs, current, head):
    # Pick the function with the lowest index.
    func = min(funcs, key=lambda x: stream.index(x))
    head += len(func)
    tokens.append(stream[current:head])
    return head

def tokenize(stream: str, functions_list: list[str] = None):
    stream = stream.strip()
    functions_list = functions_list or []

    tokens = []

    # Use two pointers for multiple character tokens
    current = 0
    head = 0

    while current < len(stream):
        # Whitespace.
        if stream[current] == " ":
            head = handle_whitespace(stream, head+1)

        # Numbers.
        elif stream[current] in ".0123456789":
            head = handle_number(stream, tokens, current, head+1)

        # One character tokens.
        elif stream[current] in "+-*/(),":
            head = handle_one_char(stream, tokens, current)

        # Strings.
        elif stream[current] in "'\"":
            head = handle_string(stream, tokens, current, head+1)

        # Functions.
        elif funcs := ([func for func in functions_list if func in stream[current:]]):
            head = handle_func(stream, tokens, funcs, current, head)

        # Unrecognised character error handling.
        else:
            starting_index = max(current-4, 0)
            ending_index = current + 5
            error_substream = stream[starting_index:ending_index]
            error_message = f"Character `{error_substream}` at index {current} not recognised\n" +  \
                            f"{' '*23}{' '*min(current, 4)}^"
            raise ValueError(error_message)

        current = head

    return tokens

def main():
    while 1:
        text_stream = input("Text stream: ")
        tokens = tokenize(text_stream)
        print(tokens)

if __name__ == "__main__":
    main()
