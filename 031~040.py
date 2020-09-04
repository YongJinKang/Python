#031.
a = "3"
b = "4"
print(a+b)
#34

#032.
print("Hi" * 3)
#HiHiHi

#033.
print('-'*80)

#034.
t1 = 'python'
t2 = 'java'

print((t1+' '+ t2 +' ')*3)

#035.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d"% (name1,age1))
print("이름 : %s 나이 : %d"% (name2, age2))

#036.
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#037.
print(f"이름: {name1} 나이 : {age1}")
print(f"이름: {name2} 나이 : {age2}")

#038.
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

#039.
분기 = "2020/03(E) (IFRS연결)"
나누기 = 분기.split("(")
print(나누기[0])
print(분기[:7])


#040.
data = "    삼성전자    "
data = data.replace("    ", "")
print(data)