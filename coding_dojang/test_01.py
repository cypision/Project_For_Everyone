def d_fn(n): return (n + sum([int(x) for x in str(n)]))

S = set(range(5000))
Z = set([d_fn(n) for n in range(5000)])
# print(sum(S-Z))
print(Z)

# a = [i for i in range(10)]
# print(sum(a))

# S=(1, 3, 4, 8, 13, 17, 20)
a = [1, 3, 4, 8, 13, 17, 20]
# print(type(A))


my_list = ['apple', 'banana', 'grapes', 'pear']
# for c, value in enumerate(S):
#     # c+"list" = 77
#     print(c, value)

a_slice = a
# a_slice[0] = 99
# b = 99
print(max(a))


