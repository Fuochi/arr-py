from typing import List
from devopsarr.adapter import RestAdapter
from devopsarr.models import ArrModel


class Tag(ArrModel):
    label: str
    id: int


class TagClient():
    base_path = '/tag/'

    def __init__(self, adapter: RestAdapter):
        self._adapter = adapter
        self._id = 0

    # list all tags
    def list(self) -> List[Tag]:
        response = self._adapter.get(self.base_path)
        return [Tag(**datum) for datum in response.data]

    # get a single tag
    def get(self) -> Tag:
        response = self._adapter.get(f'{self.base_path}{self.id}/')
        return Tag(**response.data)

    # create a single tag
    def create(self) -> Tag:
        tag = Tag(label=self.label, id=self.id)
        response = self._adapter.post(f'{self.base_path}', data=tag.dict(by_alias=True))
        return Tag(**response.data)

    # update an existing tag
    def update(self) -> Tag:
        tag = Tag(label=self.label, id=self.id)
        response = self._adapter.put(f'{self.base_path}{tag.id}/', data=tag.dict(by_alias=True))
        return Tag(**response.data)

    # delete an existing tag
    def delete(self):
        self._adapter.delete(f'{self.base_path}{self.id}/')

    @property
    def label(self):
        """Retrieve tag label.
        :rtype: string or ``NoneType``.
        :returns: The tag or ``None`` if tag has not been loaded.
        """
        return self._label

    @label.setter
    def label(self, value):
        """Set tag label.
        :type value: string.
        :param value: The tag.
        """
        self._label = value

    @property
    def id(self):
        """Retrieve tag ID.
        :rtype: int or ``NoneType``.
        :returns: The tag ID or ``None`` if tag has not been loaded.
        """
        return self._id

    @id.setter
    def id(self, id):
        """Set tag ID.
        :type id: int.
        :param id: The tag ID.
        """
        self._id = id
