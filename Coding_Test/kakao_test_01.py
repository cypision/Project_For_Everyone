## Kakao Test01
## source = https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/
## input param
str_a = "aabbaccc" ## return 7 (unit 1)
str_b = "ababcdcdababcdcd" ## return 9 (unit 8)
str_c = "abcabcdede"

# unit 별로 잘랐을때, 나오는 값 구하기
unit = 2
def clipping(arr,k):
    length = len(arr)
    a1 = int(length/k)
    print(length,"a1:",a1)
    for i in range(0,length,k):
        # print(i)
        print(arr[i:i+k])
    pass

rslt = clipping(str_a,unit)
print(rslt)