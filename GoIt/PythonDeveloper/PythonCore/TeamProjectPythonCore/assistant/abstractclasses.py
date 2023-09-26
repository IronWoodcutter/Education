from abc import ABC, abstractmethod
from collections import UserDict


class AbstractFields(ABC):
    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    @property
    def value(self):
        pass

    @abstractmethod
    @value.setter
    def value(self, value):
        pass


class AbstractNotebook(ABC, UserDict):
    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def edit_record(self, title, new_note):
        pass

    @abstractmethod
    def remove_record(self, title):
        pass
