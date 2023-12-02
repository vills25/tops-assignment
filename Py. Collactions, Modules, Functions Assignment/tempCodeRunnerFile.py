from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

counter_d1 = Counter(d1)
counter_d2 = Counter(d2)

combined_counter = counter_d1 + counter_d2

print(combined_counter)