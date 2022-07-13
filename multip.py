import threading
import multiprocessing
import time

def countdown():
     x = 10000000
     while x > 0:
           x = x - 10


# Implementation 1: Multi-threading
def implementation_1():
     thread_1 = threading.Thread(target=countdown)
     thread_2 = threading.Thread(target=countdown)
     thread_1.start()
     thread_2.start()
     thread_1.join()
     thread_2.join()


# Implementation 2: Run in serial
def implementation_2():
     countdown()
     countdown()


def implementation_3():
    process_1 = multiprocessing.Process(target=countdown)
    process_2 = multiprocessing.Process(target=countdown)
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()


if __name__ == '__main__':
    c_s = time.time()
    implementation_1()
    c_e = time.time()
    print("Implementation 1 time: {}".format(c_e - c_s))
    c_s = time.time()
    implementation_2()
    c_e = time.time()
    print("Implementation 2 time: {}".format(c_e - c_s))
    c_s = time.time()
    implementation_3()
    c_e = time.time()
    print("Implementation 3 time: {}".format(c_e - c_s))
