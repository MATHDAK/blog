class Post:
    def __init__(self, post_id, author, date, title, subtitle, body):
        self.author=author
        self.date=date
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body