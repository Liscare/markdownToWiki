import dispatcher
import wikiFetcher


if __name__ == '__main__':
    args = dispatcher.init_args()
    if len(args.input) == 1:
        wikiFetcher.fetch_from_md(args.input[0])
