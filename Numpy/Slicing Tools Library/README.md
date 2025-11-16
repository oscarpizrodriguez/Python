# Slicing Tools

**Slicing Tools** is a lightweight Python library that provides a set of helper functions for efficiently slicing and filtering NumPy arrays. It includes utilities for extracting rows, columns, subarrays, and filtering values based on comparison logic, making array manipulation easier and more intuitive.

This module is ideal for beginners learning NumPy indexing or for developers who want small, reusable tools for array handling.

---

## Features

- Extract a **specific row** from a 2D array  
- Extract a **specific column** from a 2D array  
- Create **custom subarrays** with slice ranges  
- Filter array elements **greater than** a chosen value  
- Clean, simple, and ready to integrate into any project  

---

## Tech Stack

**Python 3** – Core programming language  
**NumPy** – Used for array operations and boolean masking  

---

## File Structure

```
slicing_tools.py   # Main module containing slicing functions
```

---

## Installation

1. Ensure Python is installed:

```bash
python --version
```

2. Install NumPy if needed:

```bash
pip install numpy
```

3. Add `slicing_tools.py` to your project folder.

---

## Usage

```python
import numpy as np
import slicing_tools as st

array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row = st.get_row(array, 1)            # → [4 5 6]
column = st.get_column(array, 2)      # → [3 6 9]
sub = st.get_subarray(array, 0, 2, 1, 3)   # → [[2 3],[5 6]]
filtered = st.greater_than(array, 5) # → [6 7 8 9]
```

---

## Function Reference

### `get_row(array, row_index)`
Returns the row at the specified index.

### `get_column(array, column_index)`
Returns the column at the specified index.

### `get_subarray(array, start_row, end_row, start_col, end_col)`
Returns a subarray defined by the provided row and column slice boundaries.

### `greater_than(array, number)`
Returns all array elements greater than the provided number.

---

## License

This library is open-source and available for personal or educational use.