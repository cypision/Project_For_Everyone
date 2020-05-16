# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.
# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌



names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
input_data = names
# print(lst.count("이유덕"))

# 1)김씨와 이씨는 각각 몇 명 인가요?
def def01(input):
    name_lst = input.split(",")
    name_lst_1st = [name[0] for name in name_lst]
    kim_cnt = name_lst_1st.count("김")
    lee_cnt = name_lst_1st.count("이")
    rslt = (kim_cnt,lee_cnt)
    # find_family_name = lambda x : x[0]
    # dic = {"김":[find_family_name(n) for n in lst ].count("김") , "이":[find_family_name(n) for n in lst ].count("이")}
    return rslt

# 2)"이재영"이란 이름이 몇 번 반복되나요?
def def02(input):
    name_lst = input.split(",")
    name_count = name_lst.count("이재영")
    rslt = name_count
    return rslt

# 3)중복을 제거한 이름을 출력하세요.
def def03(input):
    name_lst = input.split(",")
    del_dup_name = set(name_lst)
    rslt = list(del_dup_name)
    return rslt

# 4)중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
def def04(input):
    name_lst = input.split(",")
    del_dup_name = list(set(name_lst))
    del_dup_name.sort(reverse=False)
    return del_dup_name

if __name__ == "__main__":
    print("before using function {}".format(input_data))
    rslt01 = def01(input_data)
    rslt02 = def02(input_data)
    rslt03 = def03(input_data)
    rslt04 = def04(input_data)
    print("after using function : ",'\n',rslt01,'\n',rslt02,'\n',rslt03,'\n',rslt04)