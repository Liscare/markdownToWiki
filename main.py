import dispatcher
import wikiFetcher

if __name__ == '__main__':
    args = dispatcher.init_args()
    wikiFetcher.fetch_from_md(args.input[0], **dispatcher.init_wiki(args))
