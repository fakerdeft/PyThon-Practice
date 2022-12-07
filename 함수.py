# def add(text1,text2):
#     '''성과 이름을 입력받아서 합쳐져 출력
#     args
#         text1: 성
#         text2: 이름
#     '''
#     text=text1+text2
#     return text

# print(add("홍","길동"))


# 끝말잇기 함수 만들기
# def game(text):
#     while True:
#         print(text)
#         text1 = input(f"{text}에 이어서 입력해주세요:")
#         if text[-1] == text1[0]:
#             text = text1
#         else:
#             print("끝말이 이어지지 않았습니다")
#             break

# game("홍길동")

# 지역변수(Local Variable), 전역변수(Globaal Variable)

# 지역변수
# def jeju_potato():
#     potato="고구마"
#     print(potato)

# jeju_potato()

# potato="감자"

# def jeju_potato():

#     potato="고구마"
#     print(potato)

# print(potato)
# jeju_potato()

# 기본 매개변수
# def add(num1,num2=20,num3=30):
    # return num1+num2+num3
# print(add(num1=20,num3=2))

# a,b=20,40
# def add(num1=a,num2=b):
#     return num1+num2
# a, b = 5,10
# print(add(a,b))

# 가변 매개변수
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(10,20,30,40)

# 키워드 매개변수
# 키워드=특정값 형태로 {"키워드":"특정값"}
# def star_player(**kwargs):
#     for i,j in kwargs.items():
#         if "페이커" in kwargs.values():
#             print("저는 T1팬이라 페이커를 좋아했어요")
#         else:
#             print(f"{i}는 역시 {j}이지")
# star_player(축구="손흥민")


# 최댓값 최솟값 구하는 함수
# sol1
# def max_min_search(*args):
#         num=[*args]
#         num.sort()
#         print(f"최댓값:{num[-1]}, 최솟값:{num[0]}")

# max_min_search(15,30,4,60,7,80,32)

# sol2
# def max_min_search(*args):
#     return max(args),min(args)

# print(max_min_search(15,30,4,60,7,80,32))
