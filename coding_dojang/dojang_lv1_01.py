# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

#기본적으로 sorting 된 상태에서는 앞,뒤의 배열의 차이만 고려하면 된다.
def short_dis_pair(input):
    dis_out_01 = []
    lst = list(input)
    lst.sort()
    min_value = max(input)
    for n in range(len(lst)-1):
        diff = lst[n+1]-lst[n]
        if diff < min_value :
            dis_out_01.append((lst[n],lst[n+1]))
            min_value = min(dis_out_01)
    # final_inx = dis_out_01.index(min_value)
    # result = (lst[final_inx],lst[final_inx+1])
    result = dis_out_01[-1]
    # print(result)
    return result

S1 = (1, 3, 4, 8, 13, 17, 20, 22)
S2 = (3, 5, 1, 7, 14, 20, 33)
# short_dis_pair(S2)

#문제에 대해 관점을 달리 했다.
#결국 최소거리를 가지는 list값을 찾으면 되니깐, 가장작은수와 2번째로 작은수를 찾는다
#이 경우는 sorting여부와 관계없이 찾을 수 있다.
def shortest(input):
    lst = list(input)
    lst.sort()
    min_lst = []
    for n in range(0,len(lst)-1):
        min_lst.append((abs(lst[n]-lst[n+1]),lst[n],lst[n+1]))
    min_lst.sort(key=lambda x : x[0],reverse=False)
    result = (min_lst[0][1],min_lst[0][2])
    return result

# shortest(S1)

    # result_list = []
    # for i in range(len(data)-1):
    #     result_list.append(lst[i+1] - lst[i])   # 거리를 차례로 계산해 리스트에 저장
    # index = result_list.index(min(result_list)) # 가장 짧은 길이의 인덱스
    # return (lst[index], lst[index+1])   # 인풋 데이터 리스트에서 대응하는 값을 리턴한다

def short_dis_pair(input):
    dis_out_01 = []
    lst = list(input)
    lst.sort()
    for n in range(len(lst)-1):
        dis_out_01.append(lst[n+1]-lst[n])
    min_value = min(dis_out_01)
    final_inx = dis_out_01.index(min_value)
    result = (lst[final_inx],lst[final_inx+1])
    return result

# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

def find_short_pair(input_data):
    from itertools import combinations
    lst = list(input_data)
    alst = list(combinations(lst,2))

    min_val = max(input_data)
    min_comb = None
    for tup in alst:
        a = abs(tup[0]-tup[1])
        if min_val > a:
            min_val = a
            min_comb = tup
    print(min_val,min_comb)
    result = None
    return result ## tuple type 2 element

if __name__ == "__main__":
    print(S1)
    # print(max(S1))
    # rslt = find_short_pair(S2)
    rslt = shortest(S1)
    print(rslt)