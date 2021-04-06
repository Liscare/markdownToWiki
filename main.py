import wikiFetcher

if __name__ == '__main__':
    wikiFetcher = wikiFetcher.WikiFetcher()
    print(wikiFetcher.fetch_from_json("words.json"))

