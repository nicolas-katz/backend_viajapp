class Plan:

    def __init__(self, id, title, price, popular, description, img):
        self.id = id
        self.title = title
        self.price = price
        self.popular = popular
        self.description = description
        self.img = img

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'popular': self.popular,
            'description': self.description,
            'img': self.img
        }

