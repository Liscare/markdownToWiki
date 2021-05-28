# Introduction
Simple script inserting Wikipedia links in your markdown document

This project is written in Python 3 and it is still in development.

# Usages
See `main.py` for usage.

## Replace empty link in a markdown file

You also need a file (in this example named `yourFile.md`) where you want to replace all empty links. 
`[Python]()` will be replaced by `[Python](https://en.wikipedia.org/wiki/Python)`

    import wikiFetcher

    if __name__ == '__main__':
        wikiFetcher.fetch_from_md("yourFile.md")

## Command Line Interface

You can use this library via the CLI like:

    python3 main.py yourFile.md -l es -n 5

This command will fill all empty links in your Markdown file. For each word, you will be able to choose
between 5 possibility form the Spanish Wikipedia.

Use `python3 main.py -h` for usage.


