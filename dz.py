# Задача 1

def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


for i in odd_nums(15):
    print(i)

# Задача 3

from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

res = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(res))
print(*islice(res, 9))
print(list(islice(res, 3)))

# Задача 4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

more_then = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]

print(more_then)

# Задача 5

my_dict = {i: 0 for i in src}

for i in src:
    my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])
