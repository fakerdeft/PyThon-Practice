'''numbers=[0,1,2,3,4,5,6,7]
print(numbers[0])
print(numbers[3:5])
print(numbers[1:])
print(numbers[-3:-1])
list_lan=['java','C']
print(list_lan[0][0:2])
list_lan[1]='C++'
print(list_lan)
list_lan[1:3]=['C#','python3']
print(list_lan)

list_lang=["java","c","python","go"]

list_lang.append("Ruby")
print(list_lang)
list_x=[1,2,3]
list_lang.extend(list_x)
print(list_lang)
list_lang.insert(0,"R")
print(list_lang)

print(list_lang.pop())

list_lang.remove("python")
print(list_lang)

del list_lang[1]
print(list_lang)

num=[500,60,100,20,3000]

num.sort()
print(num)

num.sort(reverse=True)
print(num)

name=["T","A","K"]
name.sort()
print(name)
name.sort(reverse=True)
print(name)

print(ord("A"))
print(ord("a"))
print(ord("ㄱ"))
print(ord("ㅎ"))
print(chr(66))
print(chr(98))

print(50 not in num)
print('c'in list_lang)

aa=[[10,20,30],[1,2,3]]
print(aa[0])

print(aa[0][1])
print(aa[1][0:2])'''

'''numbers=1,2,3,(4,5,6)
print(numbers.index(3))
n1,n2,n3,n4=numbers
print(n1,n2,n3,n4)
n1,n2,*n3=numbers
print(n1,n2,n3)

numberss=1,2,3,4,5
print(numberss)
print(id(numberss))
numberss+=5,6
print(numberss)
print(id(numberss))

p={
    'name':'김개똥',
    'phone':'010-1010-2020'
}
print(p['name'],p['phone'])

b={
    'daniel pink':['파는 것이 인간이다.','인제 할 것인가'],
    'eric shidt':'새로운 디지털 시대'
}
print(b['daniel pink'])

bb={1:'one',True:'True'
}
print(bb[1])

coffe={'java':2000,'ame':1500,'latte':3000}
coffe['java']=3000
print(coffe) 
coffe['moca']=4000
print(coffe) 


w={'월','화','수'}
w.add(False)
print(w)
w.update({123})
print(w)

a={1,2,3,4,5}
b={3,4,5,6,7}
print(a|b)
print(a&b)
print(a-b)

a.remove(True)
print(a)'''


