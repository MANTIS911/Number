class Solver:
    def __init__(self, exp):
        self.exp = exp

    def show(self):
        print("Result:", eval(self.exp))

s = Solver(input("Enter expression: "))
s.show()
