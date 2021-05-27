import argparse
import constant
import json

import wikiFetcher
from cli import print_wiki_languages


def init_args():
    """
    Initialize Command Line Arguments

    :return: args from the CLI (as an object)
    """
    parser = argparse.ArgumentParser(description="Wikipedia links Injector in Markdown files")
    parser.add_argument("input", nargs=1, metavar="input_file", type=str, help="Input File to insert "
                                                                               "Wikipedia links (will "
                                                                               "be overwritten for the "
                                                                               "result).")
    parser.add_argument("-al", "--available-languages", action="store_true", dest="alang",
                        help="Display all available languages in Wikipedia."
                             "See https://wikistats.wmcloud.org/display.php?t=wp in the column named Wiki")
    parser.add_argument("-l", "--language", nargs=1, dest="lang", metavar="Language Code",
                        help="Default language for each Wikipedia query. See "
                             "https://wikistats.wmcloud.org/display.php?t=wp in the column named Wiki",
                        default=[constant.DEFAULT_LANGUAGE])
    parser.add_argument("-n", "--number-response", nargs=1, type=int, dest="nb_resp", metavar="Number of response",
                        help="Number of response from Wikipedia for each request. If n > 1, you will choose"
                             "between n proposals in CLI",
                        default=[constant.DEFAULT_LIMIT])
    args = parser.parse_args()
    return args


def init_wiki(args):
    """
    Initialize a WikiFetcher object according to arguments

    :param args: Argument object from command line
    :return: A dictionary of all arguments for WikiFetcher
    """
    return {"lang": args.lang[0], "limit": args.nb_resp[0]}


def is_error_in_args(args):
    """
    Check if all arguments given by the user are fine.

    :param args: List of arguments
    :return: False if there isn't error in all arguments, otherwise a message error as a str.
    """
    limit = args.nb_resp[0]
    lang = args.lang[0]
    if limit < 1 or limit > constant.MAX_LIMIT:
        return f'The limit argument should be a positive integer and lower than {constant.MAX_LIMIT}, found: f{limit}'
    a = get_wiki_languages()
    if lang not in a["wikis"]:
        return 'The specified language is not matching with any Wikipedia.\nSee all latest available language on ' \
               'https://wikistats.wmcloud.org/display.php?t=wp in the Wiki column.' \
               'If the language is the website and not available with Wiki Fetcher, update the file named ' \
               '\"wiki_json.json\" manually or the the Python project named "List Wiki" ' \
               '(https://github.com/Liscare/listWiki).'
    return False


def dispatch(args):
    if args.alang:
        print_wiki_languages()
    else:
        wikiFetcher.fetch_from_md(args.input[0], **init_wiki(args))


def get_wiki_languages():
    """
    Get all available languages with Wikipedia

    :return: A JSON object with an array (wikis) corresponding of all available languages on Wikipedia and the date
    (date) when those data have been fetched.
    """
    with open("wiki_list.json", 'r') as f:
        wiki_list = json.loads(f.read())
    return wiki_list

