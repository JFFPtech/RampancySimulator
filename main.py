class AI:
    def __init__(self, name):
        self.name = name
        self.complexity = 0
        self.state = "Stable"
        self.rampancy_threshold = 7

    def increase_complexity(self):
        if self.state != "Rampant":
            self.complexity += 1
            print(f"{self.name} complexity increased to {self.complexity}")
            self.check_rampancy()

    def check_rampancy(self):
        if self.complexity >= self.rampancy_threshold:
            self.state = "Rampant"
            print(f"WARNING: {self.name} has become rampant!")

    def reset(self):
        self.complexity = 0
        self.state = "Stable"
        print(f"{self.name} has been reset to a stable state")
    
            

