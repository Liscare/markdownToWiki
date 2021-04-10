# Introduction
Simple script inserting Wikipedia links in your markdown document

This project is written in Python 3 and it is still in development.

# Usages
See `main.py` for usage.

## Replace words from a JSON list
You need a JSON file with all word whom you want to replace
by a markdown link through the Wikipedia page.

Each word will be replaced by a markdown link: 
`This project is written in Python` will be `This project is written in [Python](https://en.wikipedia.org/wiki/Python)` if the word 
`Python` is in your JSON file and `https://en.wikipedia.org/wiki/Python` is the corresponding Wikipedia link for this word.

You also need a file (in this example named `yourFile.md`) where you want to replace those words.
    
    import wikiFetcher

    if __name__ == '__main__':
        urls = wikiFetcher.WikiFetcher().fetch_from_json("yourWords.json")
        mdLinker.replace_links("yourFile.md", urls)

### JSON file
Your JSON file should be formatted like:

    {
      "words": [
        "yourWord1",
        "yourWord2",
        "yourWord3",
        "yourWord4"
      ]
    }

## Replace empty link in a markdown file

You also need a file (in this example named `yourFile.md`) where you want to replace all empty links. 
`[Python]()` will be replaced by `[Python](https://en.wikipedia.org/wiki/Python)`

    import wikiFetcher

    if __name__ == '__main__':
        wikiFetcher.WikiFetcher().fetch_from_md("yourFile.md")



