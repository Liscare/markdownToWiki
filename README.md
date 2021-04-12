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
        urls = wikiFetcher.fetch_from_json("yourWords.json")
        mdLinker.replace_links("yourFile.md", urls)

### JSON file
Your JSON file should be formatted like:

    {
      "wikiwords":
      [
        {
          "words": [
            "Kerala",
            "unpalatability",
            "python"
          ]
        },
        {
          "language": {
            "indicator": true,
            "code": "fr"
          },
          "words": [
            "Grèce"
          ]
        }
      ]
    }

`indicator` (`false` by default) and `code` (`en` by default) are optionals.

#### Meaning

- `wikiwords`: All your data
- `words`: List of words that you want to fetch its Wikipedia page
- `indicator`: (optional) If you want to display the language near the word like "[Python [FR]](https://fr.wikipedia.org/wiki/Python_(langage))". `False` by default
- `code`: (optional) Language code for the Wikipedia URL. See the column "Wiki" in the [list of Wikipedias](https://wikistats.wmcloud.org/display.php?t=wp). `en` (English) by default


## Replace empty link in a markdown file

You also need a file (in this example named `yourFile.md`) where you want to replace all empty links. 
`[Python]()` will be replaced by `[Python](https://en.wikipedia.org/wiki/Python)`

    import wikiFetcher

    if __name__ == '__main__':
        wikiFetcher.fetch_from_md("yourFile.md")



