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
