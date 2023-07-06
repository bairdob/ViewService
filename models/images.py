import csv
import random
from typing import TypeVar

from pydantic import BaseModel, Field

T = TypeVar('T', bound='ImagesDao')


class Image(BaseModel):
    image_url: str  # путь к картинке
    shows: int  # необходимое количество показов
    categories: set[str] = Field(max_length=10)  # категории картинки


class ImagesDao:
    images = list()  # type: list[Image]

    @classmethod
    def load(cls, file_path: str) -> T:
        result = cls()
        with open(file_path) as csv_file:
            image_reader = csv.reader(csv_file, delimiter=';')
            for row in image_reader:
                img = Image(image_url=row[0], shows=row[1], categories=row[2:])
                result.images.append(img)
        return result

    def get_image_by_categories(self, categories: list):
        # уменьшаем вероятность выдачи одной и той же картинки
        random.shuffle(self.images)

        for image in self.images:
            if set(categories).intersection(image.categories)\
                    and image.shows != 0:
                image.shows -= 1
                if image.shows == 0:
                    self.images.pop(0)
                return image.image_url
        return None


if __name__ == '__main__':
    categories = ['flight', 'airplane']
    img = Image(image_url='image1.jpg', shows=500, categories=categories)

    data = ImagesDao.load(file_path='/Users/bair/ViewService/data/images.csv')
    for image in data.images:
        print(image)

    # ImagesDao().get_image_by_categories(categories=['show'])
    ImagesDao().get_image_by_categories(categories=['show'])
    ImagesDao().get_image_by_categories(categories=['tv'])
    data.get_image_by_categories(categories=['tv'])
