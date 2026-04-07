import numpy as np

def generate_data(size):
    data = np.random.randint(1, 10000, size)
    return data.tolist()