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
    
    def monitor_complexity(self):
        if self.state == "Stable":
            if self.complexity > self.rampancy_threshold - 2:
                self.reduce_complexity()
    
    def reduce_complexity(self):
        if self.complexity > 0:
            self.complexity -= 1
            print(f"{self.name} complexity reduced to {self.complexity}")
        else:
            print(f"{self.name} complexity is already at minimum complexity")
    
    def initate_shutdown(self):
        print(f"{self.name} is shutting down due to rampant behavior.")
        self.reset()
    
            

