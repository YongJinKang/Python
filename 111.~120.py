#111.
# user  = input("입력 :")
# print(user*2)

# #112.
# user = input("숫자를 입력하세요: ")
# print(10 + int(user))


# #113.
# user = input("입력:")
# if int(user) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

#114.

# user = input("입력:")
# if int(user) > 255:
#    print(255)
# else:
#     print(int(user) + 20)


#115.
# user = input("입력:")
# num = int(user) - 20
# if num <0:
#     print(0)
# elif num > 255:
#     print(255)

# else :
#     print(num)

#116.

# time = input("현재시간:")

# if time[-2:] =='00':
#     print("정각 입니다.")

# else:
#     print("정각이 아닙니다.")

#117.

# fruit = ["사과", "포도", "홍시"]

# user = input("과일:")

# if str(user) in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

#118.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# company = input("회사명:")

# if company in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

#119.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# delicious = input("제가 좋아하는 계절은: ")

# if delicious in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

#120.

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

delicious = input("좋아하는 과일은?: ")

if delicious in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
