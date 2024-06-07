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
            while head < len(stream) and stream[head] == " ":
                head += 1

        # One character tokens.
        elif stream[current] in "+-*/(),":
            head += 1
            tokens.append(stream[current])

        # Numbers.
        elif stream[current] in "-.0123456789":
            # Only check `-` at the beginning so 1-2 is not treated as a number.
            while head < len(stream) and stream[head] in ".0123456789":
                head += 1
            tokens.append(stream[current:head])

        # Strings.
        elif stream[current] in "'\"":
            # Avoid handling the opening quote/speech mark
            head += 1
            while head < len(stream) and stream[head] not in "'\"":
                head += 1
            tokens.append(stream[current+1:head])
            # Avoid handing the ending quote/speech mark
            head += 1

        # Functions.
        elif funcs := ([func for func in functions_list if func in stream[current:]]):
            # Pick the function with the lowest index.
            func = min(funcs, key=lambda x: stream.index(x))
            head += len(func)
            tokens.append(stream[current:head])

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
