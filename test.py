from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    sum = 0
    for i in range(x):
        sum += i**3
    return sum

if __name__ == '__main__':
    pool = Pool(processes=16)              # start 4 worker processes

    # print "[0, 1, 4,..., 81]"
    print pool.map(f, range(10000000, 10000016))
