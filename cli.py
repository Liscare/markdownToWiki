def format_choice(choice):
    """
    Default format for choice
    :param choice: The choice
    :return: The formatted choice
    """
    return choice


def create_question(query):
    """
    Create the text for a question about a specific query
    :param query:
    :return: The text of a question
    """
    return f'Choose the Wikipedia article for {query}:'


def choice(choices, question, formatter=format_choice):
    """
    Print a multi-choice with an user interaction.
    :param choices: List of possible choice
    :param question: Question to ask, print at the beginning
    :param formatter: Function to format each possible choice
    :return: The user choice
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
    print(f'You choose : [{answer}] {formatter(choices[answer])}')
    return choices[answer]


def print_pretty_dict(d):
    """
    Create a dictionary like a table in CLI. One line by key.
    The first line (header) is Wikipedia Language Name
    :param d: The dictionary
    :return: A pretty dictionary for your CLI
    """
    d = dict(sorted(d.items(), key=lambda item: item[0]))
    pretty_dict = "{:<10} {:<10}\n".format('Wikipedia', 'Language Name')

    for key, value in d.items():
        pretty_dict += "{:<10} {:<10}\n".format(key, value)
    return pretty_dict
