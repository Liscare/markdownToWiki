import wikiFetcher
import mdLinker

if __name__ == '__main__':
    wikiFetcher = wikiFetcher.WikiFetcher()
    urls = wikiFetcher.fetch_from_json("words.json")
    mdLinker.replace_links("test/example.md", urls)

