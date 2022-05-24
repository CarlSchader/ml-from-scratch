import numpy as np

def run(x, w, b):
    return np.dot(w,x) + b;

def loss(y, yh):
    sum = 0
    for i in range(len(y)):
        sum += (yh[i] - y)*(yh[i] - y)
    return sum / len(y)

# def grad_descent(w, b, ):
