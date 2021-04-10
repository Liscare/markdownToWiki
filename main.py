import wikiFetcher
import mdLinker

# Example of usage
if __name__ == '__main__':
    # Replace word by markdown link
    urls = wikiFetcher.fetch_from_json("test/words.json")
    mdLinker.replace_links("test/example.md", urls)
    # Insert wikipedia link into empty link
    wikiFetcher.fetch_from_md("test/example.md")

