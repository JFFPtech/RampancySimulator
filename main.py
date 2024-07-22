class AI:
    def __init__(self, name):
        self.name = name
        self.complexity = 0
        self.state = "Stable"
        self.rampancy_threshold = 7

    def increase_complexity(self):
        if self.state != "Rampant":
            self.complexity += 1

