from pydantic import BaseModel

class User(BaseModel):
    name: str

    def __str__(self):
        return "User<name={}>".format(self.name)
