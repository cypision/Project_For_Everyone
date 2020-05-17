"""
input : 숫자
output : , 를 찍어서 숫자로 표시함
ex> 12523 입력하면 12,543 으로 출력
"""

num_int = 48434546
# num_int = 9843444687

def make_comma(input):
    str_lst = list(str(input))
    reverse_str_lst = list(reversed(str_lst))
    # print(reverse_str_lst)
    comma_rsl = []
    for i in range(len(reverse_str_lst)):
        # print(reverse_str_lst[i])
        if i % 3 ==2:
            comma_rsl.append(reverse_str_lst[i])
            comma_rsl.append(",")
        else:
            comma_rsl.append(reverse_str_lst[i])
    # print(comma_rsl)
    comma_rsl.reverse()
    rslt = "".join(comma_rsl)
    return rslt

def make_comma_origin(input):
    a = list(str(input))
    # print(list(reversed(a))) ## 값만 그대로 뒤집는건 여러 방법이 존재함
    # a.reverse() ## 값만 그대로 뒤집는건 여러 방법이 존재함

    rever_a = [x for x in a[::-1]] ## 값만 그대로 뒤집는건 여러 방법이 존재함
    # print(rever_a,"what?????????")
    new_rever_a = []
    for i in range(0,len(rever_a),3):
        # print(rever_a[i:i+3])
        new_rever_a.append(rever_a[i:i+3])

    rslt = []
    for lst in new_rever_a:
        rslt.extend(lst)
        rslt.extend(",")
    rslt.pop()
    rslt.reverse()
    last_rslt = "".join(rslt)
    # print(last_rslt)

    return last_rslt

if __name__ == "__main__":
    print(num_int)
    print("="*100)
    rslt = make_comma(num_int)
    print(rslt)


