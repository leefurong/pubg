# coding=utf-8
import unittest
from flattern import flattern


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def test_empty_dict(self):
        self.assertEqual(flattern({}), {}, 'Should return empty dict if input is empty')

    def test_not_dict(self):
        self.assertEqual(flattern(None), None, 'Should return None if input is None')
        self.assertEqual(flattern([1, 2]), [1, 2], 'should return same thing for list input')
        self.assertEqual(flattern("hi"), 'hi', 'Should return same string if input is a string')
        self.assertEqual(flattern(12), 12, 'Should return the same digit if input is digit')
        self.assertEqual(flattern(True), True, 'Should return the same boolean if input is boolean')

    def test_simple_dict(self):
        self.assertEqual(
            flattern({
                'name': 'lifurong',
                'age': 12, 
                'fans': ['yuanfeng', 'wuyifan']
            }), {
                'name': 'lifurong',
                'age': 12,
                'fans': ['yuanfeng', 'wuyifan']
            })
    
    def test_recursive(self):
        self.assertEqual(
            flattern({
                'name': 'lifurong',
                'enemy': {
                    'name': 'pretty woman',
                    'age': 18,
                    'friend':{
                        'name': 'yuanfeng'
                    }
                },
                'age': 12
            }), {
                'name': 'lifurong',
                'enemy.name': 'pretty woman',
                'enemy.age': 18,
                'enemy.friend.name': 'yuanfeng',
                'age': 12
            }
        )


if __name__ == '__main__':
    unittest.main()