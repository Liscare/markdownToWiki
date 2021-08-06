import unittest
import cli
import mock


class MyTestCase(unittest.TestCase):
    def test_print_pretty_dict_simple(self):
        expected_result = "Wikipedia  Language Name\n" \
                          "Ejemplo 2  es        \n" \
                          "Example 1  en        \n" \
                          "Exemple 3  fr        \n"
        self.assertEqual(expected_result,
                         cli.print_pretty_dict({"Example 1": "en", "Ejemplo 2": "es", "Exemple 3": "fr"}))

    def test_print_pretty_dict_complex(self):
        expected_result = "Wikipedia  Language Name\n" \
                          "de         German    \n" \
                          "es         Spanish   \n" \
                          "zh-classical Classical Chinese\n"
        self.assertEqual(expected_result,
                         cli.print_pretty_dict({"zh-classical": "Classical Chinese", "es": "Spanish", "de": "German"}))

    def test_choose(self):
        expected_result = "87"
        with mock.patch('builtins.input', side_effect=['1']):
            self.assertEqual(expected_result, cli.choice(("54", "87", "12"), "A question ?"))

    def test_choose_with_3_errors(self):
        expected_result = "54"
        with mock.patch('builtins.input', side_effect=['d', '8', 'hello', '0']):
            self.assertEqual(expected_result, cli.choice(("54", "87", "12"), "A question ?"))


if __name__ == '__main__':
    unittest.main()
