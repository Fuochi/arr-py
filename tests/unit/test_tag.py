from unittest import TestCase
from unittest.mock import MagicMock
from devopsarr.base_services import tag
from devopsarr.adapter import Result


class TestSonarr(TestCase):
    def setUp(self) -> None:
        self.adapter = MagicMock()
        self.tag = tag.TagClient(self.adapter)

    def test_get_tags(self):
        self.tag._adapter.get.return_value = Result(200, headers={}, data=[{'id': 1, 'label': "test"}])
        result = self.tag.list()
        self.assertIsInstance(result[0], tag.Tag)

    def test_get_tag(self):
        self.tag._adapter.get.return_value = Result(200, headers={}, data={'id': 1, 'label': "test"})
        self.tag.id = 1
        result = self.tag.get()
        self.assertIsInstance(result, tag.Tag)

    def test_create_tag(self):
        self.tag._adapter.put.return_value = Result(200, headers={}, data={'id': 1, 'label': "test"})
        self.tag.label = "test"
        result = self.tag.update()
        self.assertIsInstance(result, tag.Tag)

    def test_update_tag(self):
        self.tag._adapter.put.return_value = Result(200, headers={}, data={'id': 1, 'label': "test"})
        self.tag.label = "test"
        self.tag.id = 1
        result = self.tag.update()
        self.assertIsInstance(result, tag.Tag)

    def test_delete_tag(self):
        self.tag._adapter.put.return_value = Result(200, headers={}, data={})
        self.tag.id = 1
        self.tag.delete()
