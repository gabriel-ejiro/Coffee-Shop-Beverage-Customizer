class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def calories(self) -> int:
        pass
