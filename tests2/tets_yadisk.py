import unittest
import requests
from main import create_directory, headers_YD, token


class TestDocs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_create_directory1(self):
        response = requests.put(f'https://cloud-api.yandex.net:443/v1/disk/resources?path=%2FPhoto10',
                                headers=headers_YD)
        self.assertEqual(response.status_code, 201)

    def test_create_directory2(self):
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources?path=%2FPhoto_VK',
                                headers=headers_YD)
        self.assertEqual(response.status_code, 409)

    def test_create_directory3(self):
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources?path=%2FPhoto_32',
                                headers=headers_YD)
        self.assertFalse(response.status_code == 409)

    def test_create_directory4(self):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F',
                                headers=headers_YD)
        dir_info = response.json()['_embedded']['items']
        list_dir = [dir['name'] for dir in dir_info]
        self.assertIn('Photo_VK', list_dir)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()
