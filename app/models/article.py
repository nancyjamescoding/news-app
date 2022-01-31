from turtle import tiltangle


class Article:
    def __init__(self, title, description, url_to_image, published_at, url, content):
        self.title =  title
        self.description = description
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
        self.url = url