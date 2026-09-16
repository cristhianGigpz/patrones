class CounterViewModel:
    def __init__(self):
        self.count = 0
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def increment(self):
        self.count += 1

        for observer in self.observers:
            observer(self.count)


class CounterView:
    def update(self, count):
        print(f"Contador: {count}")


view_model = CounterViewModel()
view = CounterView()
view_model.subscribe(view.update)

view_model.increment()
view_model.increment()
view_model.increment()

# count += 1

# label.set_text(str(count))

# if count >= 10:
#     button.disable()

# self.count += 1
# self.button_enabled = self.count < 10
