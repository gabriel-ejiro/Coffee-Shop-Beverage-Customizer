class Beverage(ABC):
    def __init__(self, size='medium'):
        self.size = size.lower()

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass

    def get_size_multiplier(self):
        if self.size == 'small':
            return 0.9
        elif self.size == 'large':
            return 1.3
        else:
            return 1.0
