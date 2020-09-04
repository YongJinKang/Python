#051.
movie_rank = ["닥터 스트레인지","스플릿","럭키"]

#052.
movie_rank.append("배트맨")

print(movie_rank)

#053.
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)


#054.
movie_rank = ['닥터 스트레인지',' 슈퍼맨','스플릿','럭키','배트맨']
del movie_rank[3]

print(movie_rank)

#055.
movie_rank = ["닥터 스트레인지","슈퍼맨","스플릿","배트맨"]
del movie_rank[2] ,movie_rank[-1]
print(movie_rank)

#056.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python","Go","C#"]

langs = []
for i in lang1:
    langs.append(i)
for j in lang2:
    langs.append(j)

print(langs)

#or
lang = lang1 + lang2
print(lang)


#057.
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)

nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
# max:  7
# min:  1

M = max(nums);m = min(nums)
print(f"max: {M}\rmin: {m}")

#058.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059.
cook = ["피자", "김밥", "만두", "양념치킨", 
"족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수",
"김치전"] 


print(len(cook)) # len()함수 [매개변수 : 리스트]


#060.
nums = [1, 2, 3, 4, 5]


average  = sum(nums) / len(nums)

print(average)

