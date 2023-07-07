import os
import unittest

from models.images import ImagesDao, Image

DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


class TestImagesDao(unittest.TestCase):
    def test_load(self):
        """Загрузка csv файла"""
        dao = ImagesDao().load(file_path=os.path.join(DATA_FOLDER, 'images.csv'))
        self.assertEqual(len(dao.images), 4)

    def test_get_image_by_categories(self):
        """Изображение по категории."""
        dao = ImagesDao().load(file_path=os.path.join(DATA_FOLDER, 'images.csv'))
        category_show = 'show'

        # по категории нашлась картинка
        image_url = dao.get_image_by_categories(categories=[category_show])
        self.assertIsNotNone(image_url)

        for image in dao.images:
            if category_show in image.categories:
                cnt_shows = image.shows

        # проверяем, что счетчик показов уменьшился
        self.assertEqual(cnt_shows, 3299)

        category_flight = 'flight'
        # исчерпали количество показов
        image_url = dao.get_image_by_categories(categories=[category_flight])
        self.assertIsNone(image_url)

    def test_get_random_image(self):
        """Случайная картинка"""
        dao = ImagesDao().load(file_path=os.path.join(DATA_FOLDER, 'images.csv'))
        image_url = dao.get_random_image()
        self.assertIsNotNone(image_url)


if __name__ == '__main__':
    unittest.main()
