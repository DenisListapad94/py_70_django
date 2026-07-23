import unittest
import random

from src.task_manager.queue import Queue, EmptyQueueError


class TestQueue(unittest.TestCase):

    def setUp(self):
        strategy = "FIFO"
        self.queue = Queue(strategy)


    def test_no_exist_strategy(self):
        with self.assertRaises(TypeError):
            queue = Queue("FIFA")


    def test_add_item_to_queue(self):
        item_1 = 5
        self.queue.add(item_1)
        item = self.queue.storage[0]
        self.assertEqual(item_1,item)


    def test_add_and_get_item_from_queue(self):
        item_1 = 5
        self.queue.add(item_1)
        item = self.queue.remove()
        self.assertEqual(item_1,item)


    def test_add_and_get_multi_value_from_queue(self):
        item_1 = 5
        item_2 = 4
        item_3 = 3
        self.queue.add(item_1)
        self.queue.add(item_2)
        self.queue.add(item_3)
        item = self.queue.remove()
        self.assertEqual(item_1,item)
        item = self.queue.remove()
        self.assertEqual(item_2,item)
        item = self.queue.remove()
        self.assertEqual(item_3,item)

    def test_add_many_random_items(self):
        item_1 = 5
        self.queue.add(item_1)
        for _ in range(10):
            self.queue.add(random.randint(10,20))
        item = self.queue.remove()
        self.assertEqual(item_1,item)

    def test_get_item_from_empty_queue(self):
        with self.assertRaises(EmptyQueueError):
            self.queue.remove()



if __name__ == '__main__':
    unittest.main()