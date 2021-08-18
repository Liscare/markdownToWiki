import wikiFetcher
import mock


class TestWikiFetcher:
    def test_fetch_from_md(self):
        expected_result = ['Danaus genutia', 'Australia', 'forests', 'Sri Lanka', 'south-eastern', 'Kerala']
        with open("./tests/resources/test_1.md") as f:
            file_tmp = f.read()
        with mock.patch('builtins.input', return_value='0'):
            result = wikiFetcher.fetch_from_md("./tests/resources/test_1.md")
            with open("./tests/resources/test_1.md", 'w') as f:
                f.write(file_tmp)
            assert expected_result.sort() == result.sort()
