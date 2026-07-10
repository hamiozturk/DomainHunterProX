from abc import ABC, abstractmethod


class BaseExporter(ABC):

    @abstractmethod
    def export(self, domains, filename):
        """
        Domain listesini belirtilen dosyaya aktarır.
        """
        pass