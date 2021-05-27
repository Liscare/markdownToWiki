import dispatcher


def format_choice(choice):
    return choice


def choice(choices, question, formatter=format_choice):
    """

    :param choices:
    :param question:
    :param formatter:
    :return:
    """
    print(question)
    for num in range(len(choices)):
        print(f'[{num}] {formatter(choices[num])}')
    answer = -1
    while 0 > answer or answer > len(choices):
        try:
            answer = int(input())
        except ValueError:
            print("You should give an integer. Try again...")
            continue
    return choices[answer]


def print_wiki_languages():
    print_pretty_dict(dispatcher.get_wiki_languages()["wikis"])


def print_pretty_dict(d):
    d = dict(sorted(d.items(), key=lambda item: item[0]))
    print("{:<10} {:<10}".format('Wikipedia', 'Language Name'))

    for key, value in d.items():
        print("{:<10} {:<10}".format(key, value))
