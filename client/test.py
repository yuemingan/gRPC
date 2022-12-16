import unittest
import service.inventory_pb2

from unittest.mock import Mock
from inventory_client import InventoryClient
from get_book_titles import get_book_titles

class TestGetBookTitles(unittest.TestCase):
    def test_get_book_titles_mock(self):
        mock_client = Mock(spec=InventoryClient)
        mock_client.get_book.return_value = inventory_pb2.Book(title="Test")
        titles = get_book_titles(mock_client, ["12345678"])

if __name__ == "__main__":
    unittest.main()

