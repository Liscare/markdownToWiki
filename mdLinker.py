def replace_links(file_name, links):
    with open(file_name, 'r+') as file:
        content = file.read()
        print(content)
        for word, link in links.items():
            content = content.replace(word + " ", generate_link(word, link))
        file.write(content)


def generate_link(word, link):
    return f'[{word}]({link})'
