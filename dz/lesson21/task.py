import unittest
from ts import with_index  

class TestWithIndex(unittest.TestCase):

    def test_basic_usage(self):
        data = ["a", "b", "c"]
        result = list(with_index(data))
        expected = [(0, "a"), (1, "b"), (2, "c")]
        self.assertEqual(result, expected)

    def test_custom_start(self):
        data = ["x", "y"]
        result = list(with_index(data, start=5))
        expected = [(5, "x"), (6, "y")]
        self.assertEqual(result, expected)

    def test_empty_iterable(self):
        data = []
        result = list(with_index(data))
        self.assertEqual(result, [])

    def test_non_list_iterable(self):
        data = "hello"
        result = list(with_index(data))
        expected = [(0, "h"), (1, "e"), (2, "l"), (3, "l"), (4, "o")]
        self.assertEqual(result, expected)

    def test_negative_start(self):
        data = [10, 20]
        result = list(with_index(data, start=-2))
        expected = [(-2, 10), (-1, 20)]
        self.assertEqual(result, expected)

    def test_generator_input(self):
        gen = (x*x for x in range(3))  
        result = list(with_index(gen))
        expected = [(0, 0), (1, 1), (2, 4)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
