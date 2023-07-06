import csv
import random
from typing import TypeVar, Optional

from pydantic import BaseModel, Field

T = TypeVar('T', bound='ImagesDao')


class Image(BaseModel):
    """Датакласс картинки"""
    image_url: str  # путь к картинке
    shows: int  # необходимое количество показов
    categories: set[str] = Field(max_length=10)  # категории картинки


class ImagesDao:
    """
    Класс, отвечающий загрузку данных из файла и
    отдачу картинки по категориям
    """
    images = list()  # type: list[Image]

    @classmethod
    def load(cls, file_path: str) -> T:
        """
        Заполняет список картинок из файла.

        :param file_path: путь до csv файла
        :return: инстанс классa с заполненными данными
        """
        result = cls()
        with open(file_path) as csv_file:
            image_reader = csv.reader(csv_file, delimiter=';')
            for row in image_reader:
                img = Image(image_url=row[0], shows=row[1], categories=row[2:])
                result.images.append(img)
        return result

    def get_image_by_categories(self, categories: list) -> Optional[str]:
        """
        Находит картинку по категории из данных csv файла.

        Уменьшает вероятность выдачи одной и той же картинки несколько раз подряд,
        в случае, когда подходящие картинки уже исчерпали свой лимит и вернет ничего
        :param categories: категории, по которым ищем картинку
        :return: image_url (имя) картинки
        """
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

    def get_random_image(self) -> Optional[str]:
        """Получаем случайную картинку."""
        # уменьшаем вероятность выдачи одной и той же картинки
        random.shuffle(self.images)

        for image in self.images:
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
