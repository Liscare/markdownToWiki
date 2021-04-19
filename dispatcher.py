import argparse


def init_args():
    """
    Initialize Command Line Arguments

    :return: args from the CLI (as an object)
    """
    parser = argparse.ArgumentParser(description="Wikipedia links Injector in Markdown files")
    parser.add_argument("input", nargs=1, metavar="num", type=str, help="File")
    args = parser.parse_args()
    return args
