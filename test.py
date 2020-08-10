import unittest
import fizzbuzz

class FizzBuzzTests(unittest.TestCase):

    def test_fizz(self):
        number = 6

        result = fizzbuzz.get_reply(number)

        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 10

        result = fizzbuzz.get_reply(number)

        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(selfs):
        number = 15

        result = fizzbuzz.get_reply(number)

        self.assertEqual(result,'FizzBuzz')

if __name__ == "__main__":
    unittest.main()