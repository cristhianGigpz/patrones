# "  Hola MUNDO!!!  "
def remove_spaces(text):
    return text.strip()


def to_lowercase(text):
    return text.lower()


def remove_symbols(text):
    return text.replace("!", "")


def process_text(text):

    text = remove_spaces(text)
    text = to_lowercase(text)
    text = remove_symbols(text)

    return text


result = process_text("  Hola MUNDO!!!  ")

print(result)
