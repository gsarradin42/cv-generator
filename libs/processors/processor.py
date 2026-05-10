from abc import ABC, abstractmethod


class Processor(ABC):
    def __init__(self, file, i18n):
        self.i18n = i18n
        self.file

    @abstractmethod
    def load_file(str):
        pass

    @abstractmethod
    def process():
        pass
