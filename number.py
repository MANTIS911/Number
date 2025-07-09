class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error solving expression: {e}"

    def __del__(self):
        print(f"Expression '{self.expression}' instance deleted.")

exp1 = ExpressionSolver("2 + 3 * 4")
exp2 = ExpressionSolver("(10 - 2) / 4")

# Solving and printing results
print(f"The result of the first expression is: {exp1.solve()}")
print(f"The result of the second expression is: {exp2.solve()}")

del exp1
del exp2
