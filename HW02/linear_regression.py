import pandas as pd
import numpy as np
import scipy.stats as stats

def LinearRegression(covariates,targets):

    #Creating arrays
    covariates = covariates.dropna().to_numpy()
    targets = targets.dropna().to_numpy()
    targets = targets.reshape(-1,1)


    #Dimensions
    n = covariates.shape[0]
    k = covariates.shape[1]

    #Vector of ones should be created for intercept values
    ones = np.ones((n,1))

    #Appending vector of ones to X
    covariates = np.concatenate((ones, covariates), axis=1)

    #Calculating beta
    beta = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(covariates),covariates)),np.transpose(covariates)),targets)
    beta = beta.reshape(-1,1)

    #Calculating predictions
    y_hat = np.matmul(covariates,beta)
    y_hat = y_hat.reshape(-1,1)

    #Calculating errors
    e = np.subtract(targets, y_hat)

    #Calculating variance
    variance = float(np.matmul(np.transpose(e),e) / (n - k - 1)) #Since the intercept terms not included in degrees of freedom, k* = k+1

    #Calculating variance of beta
    var_beta = np.diag(np.multiply(variance, np.linalg.inv(np.matmul(np.transpose(covariates),covariates))))
    var_beta = var_beta.reshape(-1,1)

    #Calculating errors of beta
    standard_error = np.sqrt(var_beta)
    standard_error = standard_error.reshape(-1,1)

    #Calculating lower and upper bound for credible interval of 95%
    t = stats.t.ppf((1+0.95)/2., (covariates.shape[0] - covariates.shape[1]-1))

    lower_bound = np.subtract(beta, t*standard_error)
    upper_bound = np.add(beta, t*standard_error)

    return beta, standard_error, lower_bound, upper_bound, covariates, targets
