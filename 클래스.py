# # 객체이름=클래스이름()
# class BreadMold:
#     category="크림빵"  # 속성 = 일반적인 변수
#     def make_bread(self):
#         print("빵을 만들어 냅니다.")

# bread=BreadMold()
# bread_choco=BreadMold()
# #참조연산자 .format()
# i=bread.price=3000
# j=bread.category
# bread_choco.category="초코크림빵"
# print(f"{j}의 가격은 {i}입니다.")
# print(bread_choco.category)

# bread.make_bread()


# #int(),str(),float(),bool(),tuple().....type()
# #class
# number=1
# # 1=데이터 int 인스턴스(객체)
# a=1.0
# text="a"
# numbers=(1,2,3,4,5)

# print(type(number))
# print(type(text))
# print(type(numbers))
# print(isinstance(number,int))
# print(isinstance(a,int))

# # id()=객체의 주소값을 반환
# text1=12345
# text2="12345"
# print(id(text1),id(text2))
# print(id(text1),id(int(text2)))


# #__init__ 생성자 메소드
# #__del__ 소멸자 메소드
# class BreadMold:
#     category="빵"

#     def __init__(self,category,price):
#         self.category=category
#         self.price=price
#         print("빵을 만들었습니다.")
    
#     def __str__(self):
#         return "{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price)

#     def to_string(self):
#         return "{}의 가격은 {}원 입니다.".format(bread2.category, bread2.price)

#     def __del__(self):
#         print("빵이 없어졌습니다.")

# bread1=BreadMold("붕어빵",3000)
# bread2=BreadMold("잉어빵",4000)
# print(bread1)
# print(bread2.to_string())

# # #dir() 이름공간에 있는 모든 속성을 리스트로 반환
# print(dir(bread1))



# # super, 부모
# # sub, 자식
# # 상속
# class ParentRestaurant:
#     def __init__(self, name, menu, recipe):
#         self.name=name
#         self.menu=menu
#         self.recipe=recipe

#     def __str__(self):
#         return "가게이름:{}, 가게의 메뉴:{}, 메뉴의 조리법:{}".format(self.name,self.menu,self.recipe)

#     def __del__(self):
#         pass

# class ChildRestaurant(ParentRestaurant):
#     price=20000 #재정의(오버라이드)
#     marketing="온라인 마케팅" #재정의x
#     def __init__(self, name, menu, recipe, marketing):
#         ParentRestaurant.__init__(self,name,menu,recipe)
#         self.marketing=marketing

#     def __str__(self):
#         return super().__str__()+", 마케팅 방법:{}".format(self.marketing)

# restaurant_info=ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다.","온라인")
# print(restaurant_info)

# # issubclass(a,b)-> b가 a의 하위클래스인가?
# print(issubclass(ChildRestaurant, ParentRestaurant)) 
# print(issubclass(ParentRestaurant, ChildRestaurant))

def add(num1, num2):
    print(num1+num2)

def sub(num1, num2):
    print(num1-num2)

def times(num1,num2):
    print(num1*num2)

def dev(num1, num2):
    print(num1/num2)