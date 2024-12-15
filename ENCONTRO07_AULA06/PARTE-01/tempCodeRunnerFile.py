import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Padrão (linear)
q1_linear = np.quantile(data, 0.25)  # método padrão
# Weibull
q1_weibull = np.quantile(data, 0.25, method='weibull')

print(f"1º Quartil (linear): {q1_linear}")
print(f"1º Quartil (Weibull): {q1_weibull}")