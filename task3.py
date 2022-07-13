#!/usr/bin/env python
import sys
import time


def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend({list_of_values})
    return sample_dict


def find_person_powers(d, l, lower_bound, p):
    l.append(p)
    for i in range(lower_bound, list(d.keys())[len(d) - 1] + 1):
        if d.get(i) is not None:
            for x in l:
                if x in d.get(i):
                    for contact in d.get(i):
                        if contact not in l:
                            l.append(contact)
    return l


data = dict()
powers = []
input_data = sys.stdin.readline().rstrip()

while input_data:
    input_data = input_data.rsplit(" ", 2)
    input_data = [int(i) for i in input_data]
    add_values_in_dict(data, input_data[2], input_data[0])
    add_values_in_dict(data, input_data[2], input_data[1])
    input_data = sys.stdin.readline().rstrip()


sorted_data = dict((sorted(data.items())))

start_stopwatch = time.time()

find_person_powers(sorted_data, powers, int(sys.argv[2]), int(sys.argv[1]))

end_stopwatch = time.time()

print()
print("Likely to get powers:")
print(powers)
print()
print("Time elapsed: {}".format(end_stopwatch - start_stopwatch))
