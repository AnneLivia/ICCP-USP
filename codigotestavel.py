import Bhaskara

class TestBhaskara:
    # testing if there's one root
    def testOneRoot(self):
        code = Bhaskara.Bhaskara()
        assert code.calculate_roots(1,0,0) == (1,0)
    def testTwoRoot(self):
        code = Bhaskara.Bhaskara()
        assert code.calculate_roots(1,-5,6) == (2, 3, 2)
    def testZeroRoot(self):
        code = Bhaskara.Bhaskara()
        assert code.calculate_roots(10,10,10) == 0
    def negativeRoot(self):
        code = Bhaskara.Bhaskara()
        assert code.calculate_roots(10,20,10) == (1, -1)

def main():
    co = TestBhaskara()
    co.testOneRoot()
    co.testTwoRoot()
    co.testZeroRoot()
    co.negativeRoot()

main()