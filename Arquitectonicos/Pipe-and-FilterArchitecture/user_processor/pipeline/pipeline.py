class Pipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter_function):
        self.filters.append(filter_function)

    def execute(self, data):

        for filter_function in self.filters:
            data = filter_function(data)

        return data
