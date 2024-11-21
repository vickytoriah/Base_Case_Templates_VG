import abc
from abc import ABC, abstractmethod

class StrategyBaseClass(ABC):
    """
    Base Class for Strategy Classes to streamline multiple strategies;
     into one execution and backtesting model.
    """
    @abstractmethod
    def data_restructuring(
        self,
    ):
        pass

    @abstractmethod
    def strategy_runner(
        self,
    ):
        pass
    
    
if __name__ == '__main__':
    breakpoint()