#!/usr/bin/env python
import sys
from threading import Thread
import time
import random as rand

def add(self, key, value):
    try:
        self[key].append(value)
    except KeyError:
        self[key] = [value]


def find_person(d, lower_bound, pid):
    for i in range(lower_bound + 1, (list(d.keys())[-1] + 1)):
        if d.get(i) is not None:
            for x in d.get(i):
                if pid in x:
                    for contact in x:
                        if contact not in close_contacts and contact != pid:
                            close_contacts.append(contact)
    return close_contacts


def find_person_thread(d, l, lower_bound, pid):
    for i in range(lower_bound + 1, (list(d.keys())[-1] + 1)):
        if d.get(i) is not None:
            for x in d.get(i):
                if pid in x:
                    for contact in x:
                        if contact not in l and contact != pid:
                            l.append(contact)
    return l


def find_person_powers(d, l, lower_bound, p):
    l.append(p)
    for i in range(lower_bound + 1, list(d.keys())[len(d) - 1] + 1):
        if d.get(i) is not None:
            for x in d.get(i):
                if x in d.get(i):
                    for contact in x:
                        if contact not in l:
                            l.append(contact)
    return l

data = dict()
close_contacts = []
input_data = open(sys.argv[1])
f = input_data.readline().rstrip()

while f:
    f = f.rsplit(" ", 2)
    f = [int(i) for i in f]
    values = [f[0], f[1]]
    add(data, f[2], values)
    f = input_data.readline().rstrip()

answer = ""
while answer != "q":
    answer = input("Type command: t1 for single id query, t2 for multithreading query, t3 for magic power query, q to quit: ")
    sorted_data = dict(sorted(data.items()))
    if answer == "t1":

        person = input("Please enter PID you are searching for: ")
        contact_time = input("Please enter time: ")

        start_stopwatch = time.time()

        find_person(sorted_data, int(contact_time), int(person))
        end_stopwatch = time.time()

        print()
        print(*close_contacts)
        print("Time elapsed: {}".format(end_stopwatch - start_stopwatch))
        close_contacts.clear()

    elif answer == "t2":

        # Split original data set in half (FIRST HALF)
        data_first_half = dict(list(data.items())[:len(data) // 2])

        # Split first halfed data set into quarter (SECOND QUARTER)
        data_second_quarter = dict(list(data_first_half.items())[len(data_first_half) // 2:])

        # Split original data set in half (SECOND HALF)
        data_second_half = dict(list(data.items())[len(data) // 2:])

        # Split second halfed data set into quarter (FOURTH QUARTER)
        data_fourth_quarter = dict(list(data_second_half.items())[len(data_second_half) // 2:])

        # Split first half data set into quarter (FIRST QUARTER)
        data_first_quarter = dict(list(data_first_half.items())[:len(data_first_half) // 2])

        # Split second half data set into quarter (THIRD QUARTER)
        data_third_quarter = dict(list(data_second_half.items())[:len(data_second_half) // 2])

        if __name__ == '__main__':
            print("Randomly selecting person from range 0,50 and contact time from 0,100")
            one = []
            two = []
            four = []
            alltimes = []
            thread = []
            cc = []
            cc1 = []
            cc2 = []
            cc3 = []
            cc4 = []
            cc5 = []
            cc6 = []
            person = 0
            contact_time = 0
            print("Generating table")
            for _ in range(5):
                person = rand.randint(0, 50)
                contact_time = rand.randint(0, 100)
                c_s = time.time()
                find_person_thread(sorted_data, cc, int(contact_time), int(person))
                c_e = time.time()
                cc.clear()
                one.append(c_e - c_s)
                t_1 = Thread(target=find_person_thread, args=(data_first_half, cc1, int(contact_time), int(person)))
                t_2 = Thread(target=find_person_thread, args=(data_second_half, cc2, int(contact_time), int(person)))
                c_s = time.time()
                t_1.start()
                t_2.start()
                t_1.join()
                t_2.join()
                ccf = cc1 + cc2
                c_e = time.time()
                two.append(c_e - c_s)
                ccf.clear()

                t_3 = Thread(target=find_person_thread, args=(data_first_quarter, cc3, int(contact_time), int(person)))
                t_4 = Thread(target=find_person_thread, args=(data_second_quarter, cc4, int(contact_time), int(person)))
                t_5 = Thread(target=find_person_thread, args=(data_third_quarter, cc5, int(contact_time), int(person)))
                t_6 = Thread(target=find_person_thread, args=(data_fourth_quarter, cc6, int(contact_time), int(person)))
                c_s = time.time()
                t_3.start()
                t_4.start()
                t_5.start()
                t_6.start()
                t_3.join()
                t_4.join()
                t_5.join()
                t_6.join()
                ccf = cc3 + cc4 + cc5 + cc6
                c_e = time.time()
                four.append(c_e - c_s)
                cc3.clear()
                cc4.clear()
                cc5.clear()
                cc6.clear()
                ccf.clear()
            print("One Thread \t    Two Threads     \t Four Threads")
            for i in range(len(one)):
                print("{} \t {} \t {}".format(one[i], two[i], four[i]))

    elif answer == "t3":

        powers = []

        start_stopwatch = time.time()

        person = input("Please enter PID you are searching for: ")
        contact_time = input("Please enter time: ")

        find_person_powers(sorted_data, powers, int(contact_time), int(person))

        end_stopwatch = time.time()

        print()
        print("Likely to get powers:")
        print(powers)
        print()
        print("Time elapsed: {}".format(end_stopwatch - start_stopwatch))
        powers.clear()
