import numpy as np

class LinearEquationSolver:
    def __init__(self, coefficients, constants):
        self.coefficients = coefficients
        self.constants = constants

    def solve(self):
        try:
            solution = np.linalg.solve(self.coefficients, self.constants)
            return solution
        except np.linalg.LinAlgError:
            return "The system of equations has no solution."

coefficients = np.array([[2, 1], [3, 2]])
constants = np.array([5, 8])

solver = LinearEquationSolver(coefficients, constants)
solution = solver.solve()

print("Solution:", solution)
