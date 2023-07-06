import csv
from typing import TypeVar

from pydantic import BaseModel, Field

T = TypeVar('T', bound='ImagesDao')


class Image(BaseModel):
    image_url: str  # путь к картинке
    shows: int  # необходимое количество показов
    categories: list[str] = Field(max_length=10)  # категории картинки


class ImagesDao:
    images = list()  # type: list[Image]

    @classmethod
    def load(cls, file_path: str) -> T:
        with open(file_path) as csv_file:
            image_reader = csv.reader(csv_file, delimiter=';')
            for row in image_reader:
                img = Image(image_url=row[0], shows=row[1], categories=row[2:])
                cls.images.append(img)
        return cls


if __name__ == '__main__':
    categories = ['flight', 'airplane']
    img = Image(image_url='image1.jpg', shows=500, categories=categories)

    data = ImagesDao.load(file_path='/Users/bair/ViewService/data/images.csv')
    for image in data.images:
        print(image)
