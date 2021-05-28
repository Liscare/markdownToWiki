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



