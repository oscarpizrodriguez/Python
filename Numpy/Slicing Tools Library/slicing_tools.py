import numpy as np

def get_row(array, row_index):
    return array[row_index, :]

def get_column(array, column_index):
    return array[:, column_index]

def get_subarray(array, start_row, end_row, start_col, end_col):
    return array[start_row:end_row, start_col:end_col]

def greater_than(array, number):
    mask = array > number
    return array[mask]