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
        """
        This should take in data (pd.DataFrame) in the raw cleaned data from a data pipeline,
         and restructure the data in way that is suitable for the specific strategy
        :return: restructured data, most likely a pd.DataFrame, with the content otherwise unchanged
        """
        pass

    @abstractmethod
    def strategy_runner(
        self,
    ):
        """
        This should be the function that calls the method of generating the strategy signals, the execution points,
        and the threshold adjusted trade entries and exit points.
        Kept as one function for generalization of the sub-runner for the strategy
        :return: Trade execution points with the position of each trade specified in buy sell signs (+/-);
         the index should be a DatetimeIndex type and the columns, should include named multilevels
        """
        pass
    
    
if __name__ == '__main__':
    breakpoint()