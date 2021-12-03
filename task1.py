def odd_nums_gen(num):
    for n in range(1, num + 1, 2):
        yield n


odd_to_nums = odd_nums_gen(15)
print(next(odd_to_nums))
print(next(odd_to_nums))
print(next(odd_to_nums))