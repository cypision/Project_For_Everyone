
"""
input
로직: str index 이용해서 바꾸어 주기할
output : 맨 앞글자가 함수실행시마다 맨 뒤로 감

"""

input_data = "안녕하세요. 내 이름은 홍길동입니다."

def shuffle_01(input_data):
    a = input_data
    b = list(a)
    first_str = b[0]
    b.remove(first_str)
    b.extend(first_str)
    c = "".join(b)
    # print(len(c))
    return c
        

if __name__ == "__main__":
    print("before using function : ",input_data)
    for i in range(len(input_data)):
        rslt = shuffle_01(input_data)
        input_data = rslt
    rslt = input_data
    print("after using function : ",rslt)