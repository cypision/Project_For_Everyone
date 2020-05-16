# n개의 정수를 가진 배열이 있다.
# 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.
# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다.
# 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.
#
# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.

#input:배열, output:순서변경된배열

input_data=[-1, 1, 3, -2, 2]

def change_array(input):
    m_lst = [x for x in input if x < 0]
    p_lst = [x for x in input if x >= 0]
    # print(m_lst,p_lst)
    rslt = m_lst+p_lst
    return rslt
# list insert 활용
def change_array01(input):
    pass
# change_array01(S)

if __name__ == "__main__":
    print(input_data)
    rslt = change_array(input_data)
    print(rslt)