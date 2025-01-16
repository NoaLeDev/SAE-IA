import numpy as np
import pandas as pd

class DfTimeSeriesSlidingWindow:
    """
    Class used to generate input and output data from a time series, based on the Sliding Window algorithm.
    """
    
    def __init__(self, df:pd.DataFrame, i_size:int, o_size:int, value_column:str="value"):
        self.df = df
        self.i_size = i_size
        self.o_size = o_size
        self.value_column = value_column

    def steps_count(self) -> int:
        return len(self.df) - self.i_size - self.o_size

    def iterate(self):
        vals = self.df[self.value_column].to_numpy(copy=False)
        i_size = self.i_size
        o_size = self.o_size
        for i in range(self.steps_count()):
            yield (vals[i:i+i_size], vals[i+i_size, i+i_size+o_size])

    def to_matrices(self) -> tuple[np.ndarray, np.ndarray]:
        vals = self.df[self.value_column].to_numpy(copy=False)
        s_count = self.steps_count()
        strides = (vals.itemsize, vals.itemsize)
        X = np.lib.stride_tricks.as_strided(vals[:-self.o_size], (s_count, self.i_size), strides)
        Y = np.lib.stride_tricks.as_strided(vals[self.i_size:], (s_count, self.o_size), strides)
        return X, Y