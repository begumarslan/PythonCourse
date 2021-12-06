import unittest
from linear_regression import *
import pandas as pd
import numpy as np


class TestLinearRegression(unittest.TestCase):

    def test_x_shape(self):
        covariates = pd.DataFrame([[10.0, 20.0, 30.0], [2.0, 4.0, np.nan], [12.0,18.0,24.0], [8.0,12.0,20.0]])
        targets = pd.DataFrame([np.nan, 20.0, 40.0, 15.0])

        covariates_test = covariates.dropna().to_numpy()
        targets_test = targets.dropna().to_numpy()

        beta, standard_error, lower_bound, upper_bound, X_last, y_last = LinearRegression(covariates, targets)

        self.assertEqual(covariates_test.shape[0], X_last.shape[0])


    def test_y_shape(self):

        covariates = pd.DataFrame([[10.0, 20.0, 30.0], [2.0, 4.0, np.nan], [12.0,18.0,24.0], [8.0,12.0,20.0]])
        targets = pd.DataFrame([np.nan, 20.0, 40.0, 15.0])

        covariates_test = covariates.dropna().to_numpy()
        targets_test = targets.dropna().to_numpy()

        beta, standard_error, lower_bound, upper_bound, X_last, y_last = LinearRegression(covariates, targets)

        self.assertEqual(targets_test.shape[0], y_last.shape[0])

    def test_string_error(self):

        covariates = pd.DataFrame([[10.0, 20.0, 30.0], [2.0, 4.0, "xyz"], [12.0,18.0,24.0], [8.0,12.0,20.0]])
        targets = pd.DataFrame([np.nan, 20.0, 40.0, 15.0])

        with self.assertRaises(Exception):
            LinearRegression(covariates, targets)

if __name__ == '__main__':
    unittest.main()
