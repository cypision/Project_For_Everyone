
## array 는 order by 되어 있다고 가정 정렬된 숫자 존재
# input
arr01 = [1,3,2]
arr02 = [3,1,2]
arr03 = [4,3,1,2]

def check(array):
    max_arr = max(array)
    t01 = [i for i in range(1,max_arr+1)]
    rslt = []
    if array[0] != 1:
        for i in range(0,len(array)-1):
            if (array[i+1]-array[i] == -1):
                rslt.append(True)
            else:
                rslt.append(False)
    else:
        return rslt

print(check(arr03))
# print(len(arr03))
