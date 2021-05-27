import dispatcher
import wikiFetcher

if __name__ == '__main__':
    args = dispatcher.init_args()
    error_in_args = dispatcher.is_error_in_args(args)
    if not error_in_args:
        wikiFetcher.fetch_from_md(args.input[0], **dispatcher.init_wiki(args))
    else:
        print(error_in_args)
