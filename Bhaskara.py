import math

class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4  * a * c
    def main(self):
        a_type = float(input("Type value a: "))
        b_type = float(input("Type value b: "))
        c_type = float(input("Type value c: "))
        print(self.calculate_roots(a_type, b_type, c_type))
    def calculate_roots(self, a, b, c):
        d = self.delta(a,b,c)
        if d == 0: # only one root
            root1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, root1 # returning 2 values, 1 which means that there's one root and its value
        else:
            if d < 0: # there's any root
                return 0
            else:
                root1 = (-b + math.sqrt(d)) / (2 * a)
                root2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, root1, root2 # return 2 roots and value 2 to specify that there's two roots