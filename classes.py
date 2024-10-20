from dataclasses import dataclass
from pydantic import BaseModel

class Book0():
    def __init__(self,name,genre,year):
        self.name : str = name
        self.genre : str = genre
        self.year : int = year
    def info(self) -> str:
        return f"name = {self.name}; book genre = {self.genre}; year = {self.year}"

    def __str__(self) -> str:
        return self.info()
class Book_BaseModel(BaseModel):
    name : str
    genre : str
    year : int
@dataclass
class Dataclass_Book:
    name : str
    genre : str
    year : int

book0 = Book0(12324,'joke', 2010)
print(book0.info())
print(book0)

# book1 = Book_BaseModel(name = '1213',\
#              genre = 'historical',\
#              year = 1984)
# print(book1)

# book2 = Dataclass_Book('abc','classical',2014)
# print(book2)
