import dispatcher


if __name__ == '__main__':
    args = dispatcher.init_args()
    wiki_fetcher = dispatcher.init_wiki(args)
    wiki_fetcher.fetch_from_md(args.input[0])
