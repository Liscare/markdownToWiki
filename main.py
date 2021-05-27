import dispatcher

if __name__ == '__main__':
    args = dispatcher.init_args()
    error_in_args = dispatcher.is_error_in_args(args)
    if not error_in_args:
        dispatcher.dispatch(args)
    else:
        print(error_in_args)
