import numpy as np

def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

p = np.array([0.1, 0.2, 0.3, 0.4])
q = np.array([0.25, 0, 0.25, 0.25])

kl_div = kl_divergence(p, q)

print('KL散度 =', kl_div)
