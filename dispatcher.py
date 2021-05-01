import argparse
import constant
import wikiFetcher


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
    args = parser.parse_args()
    return args


def init_wiki(args):
    """
    Initialize a WikiFetcher object according to arguments

    :param args: Argument object from command line
    :return: An initialized WikiFetcher object
    """
    kargs = {"lang": args.lang[0]}
    wiki_fetcher = wikiFetcher.WikiFetcher(**kargs)
    return wiki_fetcher
