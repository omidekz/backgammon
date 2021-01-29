class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "User<name={}>".format(self.name)
