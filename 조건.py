
'''text=input("첫번째 수:")
text2=input("두번째 수:")
print(text+text2)
print(int(text)+int(text2))

st=int(input("정수 입력:"))

if st % 2==1:
    print("입력하신 정수는 홀수입니다.")
else:
    print("입력하신 정수는 짝수입니다.")'''

'''
n = input("주민번호 입력:")
s = int(n[7])
if s % 2 == 0:
    print("여성입니다.")
else:
    print("남성입니다.")
''''''
l=input("점심메뉴를 골라주세요(제육덮밥, 돈까스, 김밥):")

if l=="제육덮밥":
    print("제육덮밥을 먹는다")
elif l=="돈까스":
    print("돈까스를 먹는다")
elif l=="김밥":
    print("김밥을 먹는다")
else:
    print("점심을 굶는다")'''

'''
nb=int(input("정수를 입력해주세요:"))
if nb %3 ==0 or nb %2==0:
    if nb%3==0 and nb %2!=0:
        print("3의 배수입니다.")
    elif nb%3==0 and nb %2==0:
        print("3의 배수이면서 짝수입니다.")
    else:
        print("짝수입니다.")
else:
    print("3의배수도 짝수도 아닙니다.")'''





'''a=input("웹사이트 주소를 입력해주세요:")
b=a.split(".")

if b[-1]=="kr":
    print("한국")
elif b[-1]=="uk":
    print("영국")
elif b[-1]=="com":
    print("기업")
elif b[-1]=="org":
    print("기관")
else:
    print("알 수 없음")'''




'''num=1
while num<=5:
    num+=1
    print(num)
else:
    print("값이 {}이상이므로 종료합니다.".format(num))'''



'''fruits=["apple","banana","apple","banana","melon"]
print(fruits)

fruit = input("빼낼 과일 입력:")
while fruit in fruits:
    fruits.remove(fruit)
print(fruits)
print("{}를 모두 제거했습니다.".format(fruit))'''

'''
# 최솟값 최댓값 입력
min_n=int(input("최솟값 입력:"))
max_n=int(input("최댓값 입력:"))
# 홀짝 리스트
odd_list=[]
even_list=[]
# 제어변수에 최솟값 할당
num=min_n

# 최솟값이 최댓값보다 작을 경우 실행
if min_n<max_n:
    while num <= max_n: # 제어변수가 최댓값이 될 때까지 반복 실행
        if num %2 == 0: # 짝수 판별
            even_list.append(num)    # 짝수를 짝수 리스트에 요소로 추가
        else: # 홀수 판별
            odd_list.append(num)     # 홀수를 홀수 리스트에 요소로 추가
        num += 1
    print("{}부터 {}까지의 홀수는 {}입니다.".format(min_n,max_n,odd_list))
    print("{}부터 {}까지의 짝수는 {}입니다.".format(min_n,max_n,even_list))

else: # 최솟값이 최댓값보다 크거나 같을 경우
    print("최댓값 {}이 최솟값 {}보다 크지 않습니다.".format(max_n,min_n))'''


'''n=list(range(0,10,2)) 
print(n)'''


# for i in range(1,10+1):
#     print(i)


# for i in "일이삼사오":
    # print(i)


# fruits=["사과","딸기","바나나"]
# for i in fruits:
    # print("과일 바구니에 {}가 들어있습니다.".format(i))


# 1부터 30까지의 수 중에서 3의 배수들의 합을 구하시오.
# 3의 배수는 어떻게 구하면 될까요?
# 짝수 % 2 == 0
# / 2 == 2의 배수와 같다.
# sum=0
# for i in range(3, 30+1,3):
#     print("{} + {} = ".format(sum,i),end="")
#     sum += i
# print(sum)


# coffee={"ame":2000,"latte":3000,"java":2500}
# for i in coffee.keys():
#     print(i)


# fruits=["apple","sb","banana"]
# for i,j in enumerate(fruits):
#     print(f"{i+1}번째 과일은 {j}입니다.")


# list_2nd=[[1,2,3],["a","b","c"]]
# for i in list_2nd:
#     for j in i:
#         print(j)


# for i in range(1,3):
#     for j in range(1,3):
#         print(f"첫 번째 for문의 반복 {i}번, \
#         \t두 번째 for문의 반복 {j}번")


# print("1단부터 9단까지 구구단 출력")
# for i in range(1,9+1):
#     for j in range(1,9+1):
#         print(f"{i} X {j} = {i*j}",end="\t")
# print()


# list_3rd=[[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]]
# c1=0
# c2=0
# c3=0
# for i in list_3rd:
#     c1 += 1
#     print(f"i의 {c1}번째 반복입니다.")
#     print(i)
#     for j in i:
#         c2 += 1 
#         print(f"j의 {c2}번째 반복입니다.")
#         print(j)
#         for k in j:
#             c3 += 1
#             print(f"k의 {c3}번째 반복입니다.")
#             print(k)
# print(f"i는 {c1}번 반복, j는 {c2}번 반복, k는 {c3}번 반복")            


# i = 0
# while True:
#     print(f"{i}번째 반복입니다.")
#     i += 1
#     if i > 10:
#         break


# sum = 0 
# while True:
#     num = int(input("정수를 입력하세요(0입력시 종료):"))
#     if num == 0:
#         break
#     sum += num
#     print(f"현재 정수의 합은 {sum}입니다.")
# print("반복문이 종료되었습니다.")


# numbers = [10,200,30,400,50]
# for i in numbers:
#     if i < 200:
#         continue
#     print(f"{i}는 200이상의 숫자입니다.")


# numbers = [[1,2,3],[10,20,30]]
# for i in numbers:
#     print(i)
#     for j in i:
#         print(j)
#         break


# menu = {"icea":3000,"a":2500,"icel":4000,"l":3500,"ice":8000}

# print("차가운 메뉴")
# for i,j in menu.items():
#     if i[0:3] == "ice":
#         print(f"제품명:{i} 가격:{j}")
# print("뜨거운 메뉴")
# for i,j in menu.items():
#     if i[0:3] != "ice":
#         print(f"제품명:{i} 가격:{j}")
