## 숫자로 들어온 값의 각자리수를 더하고, 이후 원래 숫자를 또 더하여 리턴하라
## 91 -> 101 : 9 + 1 + 91
def find_generator(input):
    str01 = str(input)
    num = 0
    for i in str01:
        num = num+int(i)
    num = num+int(input)
    return num

# 좀 더 간단하게 아래와 같이 수정
find_g = lambda x : x  + sum([int(n) for n in str(x)])

# r_01 = [find_g(inx) for inx in range(5000)]
# s_01 = set(r_01)
# s_02 = set([n for n in range(1,5001)])
#
# r_02 = list(s_02-s_01)
# result = sum(r_02)
# print(result)


find_g = lambda x : x  + sum([int(n) for n in str(x)])
out_01 = find_generator(91)
out_02 = find_g(91)
print(out_01,"n","--------",out_02)

# if __name__ == "__main__":
#     print(S1)
#     # print(max(S1))
#     # rslt = find_short_pair(S2)
#     rslt = short_dis_pair(S1)
#     # print(rslt)