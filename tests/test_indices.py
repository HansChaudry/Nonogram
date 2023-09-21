import pytest
from Indices import arrangement

TEST_BOARD = [
    [0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
]

columns = []
rows = []


def test_arragement():
    arrangement(col_list=columns, row_list=rows, cellMAP=TEST_BOARD)
    assert columns == [[3], [2, 2], [1, 1], [2, 2], [1, 2]]
    assert rows == [[1, 2], [3], [1], [2, 2], [5]]
