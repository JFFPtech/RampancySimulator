# AI Rampancy Simulation

This project is a simple simulation of the concept of AI rampancy, inspired by the Halo universe. The code models an AI that increases in complexity over time and becomes rampant if its complexity exceeds a certain threshold.

## Description

The `AI` class represents an artificial intelligence with the following attributes and methods:

- **Attributes**:
  - `name`: The name of the AI.
  - `complexity`: A measure of the AI's complexity.
  - `state`: The current state of the AI, either "Stable" or "Rampant".

- **Methods**:
  - `__init__(self, name)`: Initializes a new AI instance with the given name.
  - `increase_complexity(self)`: Increases the AI's complexity by 1 and checks for rampancy.
  - `check_rampancy(self)`: Checks if the AI's complexity has exceeded the rampancy threshold.
  - `reset(self)`: Resets the AI's complexity to 0 and its state to "Stable".

## Usage

1. Create an instance of the `AI` class.
2. Increase the AI's complexity using the `increase_complexity` method.
3. Check the AI's state to see if it has become rampant.
4. Reset the AI if needed using the `reset` method.
