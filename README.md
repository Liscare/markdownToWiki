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

### Available languages

Available languages are determined by Wikipedia, a list is available [here](https://wikistats.wmcloud.org/display.php?t=wp).
Thanks to the project named [listWiki](https://github.com/Liscare/listWiki), the list of available languages is stored in `wiki_list.json`. To print all
languages (sorted by language name), use `python3 main.py bb -al`. 

Some differences between the official list and the result of the command `python3 main.py bb -al` 
can happen. In this case, you can contribute updating the JSON file.


