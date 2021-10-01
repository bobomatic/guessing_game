import unittest
import main

class TestGame(unittest.TestCase):
    def test_main(self):
        pass

    def test_run_guess_incorrect(self):
        """[this enters an incorrect string int]"""
        test_answer = 5
        test_guess = '7'
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False) # could use assertFalse

    def test_run_guess_correct(self):
        test_answer = 7
        test_guess = '7'
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, True)

    def test_run_guess_OOR_minus(self):
        test_answer = -6
        test_guess = '7'
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False)

    def test_run_guess_zero(self):
        test_answer = 7
        test_guess = '0'
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False)

    def test_run_guess_non_decimal(self):
        test_answer = 7
        test_guess = 'asfasfh'
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False)

    def test_run_guess_empty(self):
        test_answer = 7
        test_guess = ''
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False)

    def test_run_guess_OOR_plus(self):
        test_answer = 12
        test_guess = ''
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False)

    def test_run_guess_list(self):
        test_answer = 7
        test_guess = '[1,2,3]'
        guess_is_correct, message = main.run_guess(test_guess, test_answer)
        self.assertEqual(guess_is_correct, False)

if __name__ == '__main__':
    unittest.main()