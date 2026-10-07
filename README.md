# Mean, Variance & Standard Deviation Calculator

A Python and NumPy project by **Junot Cacoq**, developed for the freeCodeCamp Data Analysis with Python curriculum.

The calculator takes nine numbers, reshapes them into a 3 × 3 matrix, and computes descriptive statistics across columns, across rows, and for the entire matrix.

## Statistics

| Dictionary key | Calculation |
| --- | --- |
| `mean` | Arithmetic mean |
| `variance` | Population variance (`ddof=0`) |
| `standard deviation` | Population standard deviation (`ddof=0`) |
| `max` | Maximum value |
| `min` | Minimum value |
| `sum` | Sum of values |

## Installation

Install Python 3 and Git, then run:

```bash
git clone https://github.com/junot10-cpu/fcc-mean-variance-std-calculator.git
cd fcc-mean-variance-std-calculator
python3 -m pip install -r requirements.txt
```

## Usage

Run the included example:

```bash
python3 mean_var_std.py
```

Or call the function from Python:

```python
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

The input is reshaped into:

```text
0  1  2
3  4  5
6  7  8
```

## Output format

Each statistic contains three entries:

1. A list of results for the three columns (`axis=0`).
2. A list of results for the three rows (`axis=1`).
3. A single result for all nine values.

For example, the mean and sum for `[0, 1, 2, 3, 4, 5, 6, 7, 8]` are:

```python
{
    'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
    'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

The full dictionary also includes variance, standard deviation, maximum, and minimum.

If the input does not contain exactly nine numbers, `calculate()` raises `ValueError("List must contain nine numbers.")`. Importing the module does not print anything.

## Project files

| File | Purpose |
| --- | --- |
| `mean_var_std.py` | The `calculate()` function. |
| `main.py` | Shows an example result and runs the tests. |
| `test_module.py` | Six learning tests: three data sets, two input-validation errors and a silent-import check. |
| `requirements.txt` | Python dependencies (`numpy`). |

## Run the tests

```bash
python3 main.py
```

or only the tests:

```bash
python3 -m unittest test_module -v
```

These are custom learning tests, not the official freeCodeCamp test suite.

## Skills practiced

- Reshaping NumPy arrays.
- Applying reductions along different axes.
- Returning Python lists and scalars from NumPy calculations.
- Structuring results with dictionaries.
- Managing source code with Git and GitHub.

## Project reference

[freeCodeCamp — Mean-Variance-Standard Deviation Calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

## Author

**Junot Cacoq** · [GitHub profile](https://github.com/junot10-cpu)
