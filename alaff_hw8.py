from typing import Tuple, List, Dict
import numpy as np

def Create_Poisson_problem_nzA(n: int) -> Tuple[List, List, List]:
    # constructs Poisson matrix in sparse form
    num_rows = n**2
    value = []
    row_idx = []
    col_idx = []
    for i in range(num_rows):
        val = [-1, -1, 4, -1, -1]
        indices = [i-n, i-1, i, i+1, i+n]
        value_sub = []
        indices_sub = []
        for idx, val in zip(indices, val):
            if 0 <= idx <= n**2 -1 :
                value_sub.append(val)
                indices_sub.append(idx)
        # Now we have values
        number_of_values_in_row = len(value_sub)
        row_idx_sub = [i]*number_of_values_in_row # This are the row indices of all
        col_idx_sub = indices_sub # This is where this row data starts
        value += value_sub
        row_idx += row_idx_sub
        col_idx += col_idx_sub
    return value, row_idx, col_idx

def construct_matrix_from_crs(values: List[int], row_idx: List[int], col_idx: List[int]) -> List[List[int]]:
    max_row = row_idx[-1]
    max_col = max(col_idx)
    matrix = np.zeros((max_row+1, max_col+1))
    for row, col, val in zip(row_idx, col_idx, values):
        matrix[row][col] = val
    return matrix

def SparseMvMult(values: List[int], row_idx: List[int], col_idx: List[int], x: List[int]) -> List[int]:
    """
    Implements sparse matrix multiplication
    :param values:
    :param row_idx:
    :param col_idx:
    :param x:
    :return:
    """
    num_rows = row_idx[-1]
    vals = []
    itr = 0
    for row in range(num_rows+1):
        row_value = 0

        while (itr < len(values)) and (row_idx[itr] == row) :
            col_number = col_idx[itr]
            val = values[itr]
            row_value += val * x[col_number]
            # print("num", row, itr, val, x[col_number], row_value)
            itr += 1
        vals.append(row_value)
    return vals


n = 2
x = [1, 2, 3, 4]
values, row_idx, col_idx = Create_Poisson_problem_nzA(2)
print(construct_matrix_from_crs(values=values, row_idx=row_idx, col_idx=col_idx))
result = SparseMvMult(values=values, row_idx=row_idx, col_idx=col_idx, x=x)
print(f"Result of multiplying Poisson matrix for n = {n} with vector {x} using Sparse Mv Mult = {result}")