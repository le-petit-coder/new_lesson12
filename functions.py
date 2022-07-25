import json


def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    full_list = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            full_list.append(post)
    return full_list


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'a', encoding='utf-8'):
        json.dumps(posts)
    return post



