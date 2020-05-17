## 양의 정수값을 2진법으로 변환해서 나타내라
## 24 -> 11000
## recursive function define
def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    # print(num)
    print(num % 2, end='')

def tobinary(num):
    denomi_rslt = [num]
    binary_lst = []
    print(denomi_rslt)
    while True:
        if denomi_rslt[-1] < 2:
            break
        else:
            a = denomi_rslt[-1]//2
            b = denomi_rslt[-1]%2
            denomi_rslt.append(a)
            binary_lst.append(b)
    last_mok = denomi_rslt[-1]
    binary_lst.append(last_mok)
    binary_lst.reverse()
    rslt = "".join([str(x) for x in binary_lst])
    # print(denomi_rslt)
    # print(binary_lst)
    # print(rslt)
    print(int(rslt))

# Driver Code
if __name__ == '__main__':
    # decimal value
    # dec_val = 24
    dec_val = 65498131
    # Calling function
    DecimalToBinary(dec_val)
    tobinary(dec_val)