class Pipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter_function):
        self.filters.append(filter_function)

    def execute(self, data):

        for filter_function in self.filters:
            data = filter_function(data)

        return data


def remove_spaces(text):
    return text.strip()


def to_lowercase(text):
    return text.lower()


def remove_symbols(text):
    return text.replace("!", "")


pipeline = Pipeline()

pipeline.add_filter(remove_spaces)
pipeline.add_filter(to_lowercase)
pipeline.add_filter(remove_symbols)

result = pipeline.execute("  Hola MUNDO!!!  ")

print(result)
