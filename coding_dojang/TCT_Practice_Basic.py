import numpy as np
aa = np.zeros((3,3),int)
# print(aa)

## list 숫자를 string으로 ##
input_data = [432, 123, 556, 113, 556]
input_data2 = [4332, 1823, 5456, 14913, 51156]
print(input_data)
## string으로 바꾸어서, 개별숫자로 보고, 중복을 제거하여, 큰 순서데로 보여라

def main(input_data):
    result = []
    a = [list(str(x)) for x in input_data]
    r1 = []
    for lst in a:
        r1.extend(lst)
    b = set(r1)
    result = sorted(list(b),reverse = True)
    return result

#
## list 형태의 합
# 1) int 에 바로 list() 은 형변환 안됨. 그냥 [ int ] 선언이 먹힘
# 2) list 사이에서, + 가능
input_size = 784
hidden_size_list = [100,100,100,100]
output_size = 10
# all_size_list = [input_size] + hidden_size_list + [output_size] # [784,100,100,100,100,10]
all_size_list = [input_size] + hidden_size_list + [output_size]
# print(all_size_list)

def sample01():
    ## list reverse
    #1) list.sort() : return 값 없음. self
    vowels = ['ea', 'a', 'uc', 'ofdf', 'iae']
    print("before_sort():{}".format(vowels))
    # vowels.sort()
    # print("after_sort():{}".format(vowels))
    #2) list.sort() parameter by key. key에는 function만 가능
    # vowels.sort(key=len,reverse=True)
    # print("after_sort_bykey():{}".format(vowels))
    #3) python inner function sorted() : return 값이 있음
    # rslt = sorted(vowels , reverse= False)
    rslt = sorted(map(lambda  s : s+'kiss',vowels), reverse= False)
    print(rslt)
    print()

def sample02():
    ## range로 list만들기
    input_data = 5
    n = input_data
    num_lst = []
    for i in range(0,n*n,n):
        tmp_lst = list(range(i,i+n))
        num_lst.append(tmp_lst)
    print(num_lst)
    print()

def sample03():
    ## dict type sorting
    adict = {'d':1, 'b':5, 'a':2, 'e':12}
    # lst = list(adict.values())

    for key,val in sorted(adict.items(), key = lambda item : item[1], reverse=True):
        print(key,val)
    rslt = sorted(adict.items(), key = lambda item : item[1], reverse=True)
    print(dict(rslt))
    print()

if __name__ == "__main__":
    # result = main(input_data2)
    # print("result : {}".format(result))
    # print("sample01=="*30)
    # sample01()
    # print("sample02=="*30)
    # sample02()
    print("sample03==" * 30)
    sample03()

