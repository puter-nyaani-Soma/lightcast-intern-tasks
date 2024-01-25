# test_multiplication_table.py
import unittest
from print_multiplication_table import multiplication_table

class TestMultiplicationTable(unittest.TestCase):
    def test_table_size_negative(self):
        result = capture_output(lambda: multiplication_table(-5))
        expected_output = (
            "1 x -5 = -5\t\n"
            "2 x -5 = -10\t\n"
            "3 x -5 = -15\t\n"
            "4 x -5 = -20\t\n"
            "5 x -5 = -25\t\n"
            "6 x -5 = -30\t\n"
            "7 x -5 = -35\t\n"
            "8 x -5 = -40\t\n"
            "9 x -5 = -45\t\n"
            "10 x -5 = -50\t\n"
        )
        # print("Expected output")       
        # print(expected_output)
        # print("Actual output")
        # print(result)
        self.assertEqual(result, expected_output)

    def test_table_size_positive(self):
            result = capture_output(lambda: multiplication_table(7))
            expected_output = (
                "1 x 7 = 7\t\n"
                "2 x 7 = 14\t\n"
                "3 x 7 = 21\t\n"
                "4 x 7 = 28\t\n"
                "5 x 7 = 35\t\n"
                "6 x 7 = 42\t\n"
                "7 x 7 = 49\t\n"
                "8 x 7 = 56\t\n"
                "9 x 7 = 63\t\n"
                "10 x 7 = 70\t\n"
            )
            # print("Expected output")       
            # print(expected_output)
            # print("Actual output")
            # print(result)
            self.assertEqual(result, expected_output)
            
    def test_table_size_float(self):
            result = capture_output(lambda: multiplication_table(0.5))
            expected_output = (
            "1 x 0.5 = 0.5\t\n"
            "2 x 0.5 = 1.0\t\n"
            "3 x 0.5 = 1.5\t\n"
            "4 x 0.5 = 2.0\t\n"
            "5 x 0.5 = 2.5\t\n"
            "6 x 0.5 = 3.0\t\n"
            "7 x 0.5 = 3.5\t\n"
            "8 x 0.5 = 4.0\t\n"
            "9 x 0.5 = 4.5\t\n"
            "10 x 0.5 = 5.0\t\n"
        )
            # print("Expected output")       
            # print(expected_output)
            # print("Actual output")
            # print(result)
            self.assertEqual(result, expected_output)
    def test_multiply_with_zero(self):
            result = capture_output(lambda: multiplication_table(0))
            expected_output = "Input 'n' should be a integer.\n"
            # print("Expected output")       
            # print(expected_output)
            # print("Actual output")
            # print(result)
            self.assertEqual(result, expected_output)

    def test_multiply_with_char(self):
            result = capture_output(lambda: multiplication_table('s'))
            expected_output = "Input 'n' should be a integer.\n"
            # print("Expected output")       
            # print(expected_output)
            # print("Actual output")
            # print(result)
            self.assertEqual(result, expected_output)


# Helper function to capture the printed output
def capture_output(func):
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

if __name__ == '__main__':
    unittest.main()
