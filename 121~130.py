#121.


# user = input("")

# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())


#122.

# score = input("점수:")

# if int(score) >= 81:
#     print("grade is A")
# elif int(score) >=61:
#     print("grade is B")
# elif int(score) >=41:
#     print("grade is C")
# elif int(score) >=21:
#     print("grade is D")
# else:
#     print("grade is E")


#123. 어렵어렵
a = 1167
b = 1.096
c = 1268
d = 171
# 돈1 = "100 달러"
# print(돈1[-2:])
# print(돈.split(" ")[0])
# 돈 = input("입력:")
# if 돈[-2:] =="달러":
#     print("{}원".format(float(돈.split(" ")[0])*float(a)))
# elif 돈[-1] == "엔":
#     print("{}원".format(float(돈.split(" ")[0])*float(b)))
# elif 돈[-2:] == "유로":
#     print("{}원".format(float(돈.split(" ")[0])*float(c)))
# elif 돈[-2:] == "위안":
#     print("{}원".format(float(돈.split(" ")[0])*float(d)))


# #124.
# number_list = []

# num1 = input("input number1:")
# num2 = input("input number2:")
# num3 = input("input number3:")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# number_list.append(num1)
# number_list.append(num2)
# number_list.append(num3)


# print(max(number_list))

#125.

# phone = {"011": "SKT", " 016": "KT", "019": "LGU", "010": "알수없음"}
# print(phone.keys()[1])
# number = input("휴대전화 번호 입력 : ")
# num = number.split("-")[0]
# if num[:3] == '011':
#     com = "SKT"
# elif num[:3] == '016':
#     com = "KT"
# elif num[:3] == '019':
#     com = "LGU"
# elif num[:3] == '010':
#     com = "알수없음"

# print("당신은 {} 사용자입니다.".format(com))
 
 #126.

# 우편번호 = input("우편번호: ")
# 우편번호 = 우편번호[:3]
# if 우편번호 in ["010", "011", "012"]:
#     print("강북구")
# elif 우편번호 in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")


#127.

# number = input("주민등록번호 :")
# sex = number[8]

# if sex in ["1","3"]:
#     print("남자")
# elif sex in ["2","4"]:
#     print("여자")


#128.

# number = input("주민등록번호:")

# region = number[8:10]

# if int(region) <= 8:
#     print("서울")
# else:
#     print("부산")


#129.

number = input("주민등록번호:")
number_list = number.split("-")
front = number_list[0]
back = number_list[1]


계산1 = int(front[0])*2 + int(front[1])*3+int(front[2])*4+int(front[3])*5+int(front[4])*6
+int(front[5])*7

계산2 = int(back[0])*8+int(back[1])*9+int(back[2])*2+int(back[3])*3
+int(back[4])*4+int(back[5])*5

계산3 = (계산1 + 계산2)%11

계산4 = 11 - 계산3

if number[-1] == 계산4:
    print("유효한 주민 등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
