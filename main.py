"""Run the calculator example and the learning tests."""
import unittest
from pathlib import Path

from mean_var_std import calculate


if __name__ == '__main__':
    # Run the calculator and display its results.
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    # Discover and run the tests in test_module.py.
    print('\nRunning tests...', flush=True)
    suite = unittest.defaultTestLoader.discover(
        str(Path(__file__).resolve().parent), pattern='test_module.py'
    )
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if outcome.wasSuccessful() else 1)
