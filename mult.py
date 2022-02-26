import unittest

def multiply(x, y):
  return x * y

# usually tests live in a separate file or module. For the sake of simplicity it is here inline
class TestMult(unittest.TestCase):
    
    # test cases must begin with "test_"
    def test_mutiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "should be 50")

# how to run tests without a test runner - just good to experiment or if there a very few tests
if __name__ == "__main__":
    unittest.main()
# another way of executing unittests not using the main execution is by executing the command `python -m -v unittest mult (test file)` (-m means module, -v verbose)