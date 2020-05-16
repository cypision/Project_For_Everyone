##


input_Data =  [547, 12, 456, 2345, 724 , 343]
######################################
data = [list(str(s)) for s in input_Data]
rslt = []
for lst in data :
    flag = 0
    for idx in range(1,len(lst)):
        a = int(lst[idx])-int(lst[idx-1])
        if a == 1:
            flag += 1
        if flag == (len(lst)-1):
            rslt.append(lst)
last_rslt  = []
for lst_st in rslt:
    a = ""
    for ch in lst_st:
        a += ch
    last_rslt.append(int(a))
print(last_rslt)

max_int = 0
for val in last_rslt:
    if val > max_int :
        max_int = val
min_int = max_int
for val in last_rslt:
    if val < min_int :
        min_int = val
print(max_int,min_int)