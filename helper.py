import requests
from lxml import html


def extract_comments(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    comments = tree.xpath('//comment()')

    new_comments = []

    for comment in comments:
        new_comment = comment.text
        new_comment = new_comment.replace("<!--", "")
        new_comment = new_comment.replace("-->", "")
        new_comments.append(new_comment)

    return new_comments


def extract_links(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    links = tree.xpath('//a/@href')

    return links


def get_body(url):
    page = requests.get(url)
    return page.text
