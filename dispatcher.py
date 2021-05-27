import argparse
import constant


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
    limit = args.nb_resp[0]
    if limit < 1 or limit > constant.MAX_LIMIT:
        return f'The limit argument should be a positive integer and lower than {constant.MAX_LIMIT}, found: f{limit}'
    return False
