import numpy as np
from scipy.stats import multivariate_normal


def multivariate_normal_log(x, mean, cov):
    n = len(mean)
    x = np.squeeze(x)
    mean = np.squeeze(mean)
    constant = -0.5 * n * np.log(2 * np.pi) - 0.5 * np.log(np.linalg.det(cov))
    exponent = -0.5 * np.matmul(np.matmul((x - mean).T, np.linalg.inv(cov)), (x - mean))
    logpdf = constant + exponent
    return logpdf



x = np.array([1, 2])
mean = np.array([0, 0])
covariance = np.array([[1, 0.5], [0.5, 1]])
log_density_values = multivariate_normal_log(x, mean, covariance)
scipy_log_density = multivariate_normal(mean=mean, cov=covariance).logpdf(x)

logpdf = multivariate_normal_log(x, mean, covariance)
print("Log:", logpdf)
print("Diff in eff: ")
print(np.max(np.abs(log_density_values - scipy_log_density)))