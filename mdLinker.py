def replace_links(file_name, links):
    """
    Replace all word in links by a markdown link according to its link

    :param links: Dict of your words/links (example : {"word": "a link", "Framasoft":"https://framasoft.org/en/"})
    :param file_name: File name of your markdown file
    :return: None
    """

    with open(file_name, 'r+') as file:
        content = file.read()
        for word, link in links.items():
            content = content.replace(word + " ", generate_link(word, link))
        file.write(content)


def replace_in_md(file_content, words_links):
    """
    Replace '[myWord]()' by '[myWord](wikiLink)' when myWord exists into words_links parameter

    :param file_content: Content of your markdown file
    :param words_links: Dict of each word and it link (example: {myWord: wikiLink})
    :return: File content with links
    """
    result = file_content
    for word, link in words_links.items():
        result = result.replace(f'[{word}]()', generate_link(word, link))
    return result


def generate_link(word, link):
    """
    Return a str like a markdown link

    :return: str (example: [python](https://en.wikipedia.org/wiki/Python_(programming_language)))
    """

    return f'[{word}]({link})'
