from logging import exception
from multiprocessing.sharedctypes import Value


def division():
    # # num1=int(input("첫 번째 정수를 입력해주세요:"))
    # # num2=int(input("두 번째 정수를 입력해주세요:"))
    # num1=input("첫 번째 정수를 입력해주세요:")
    # if num1.isdigit():
    #     num2=input("두 번째 정수를 입력해주세요:")
    #     if num2.isdigit()and num2 !="0":
    #         return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.") 
    #     else:
    #         print("숫자로된 정수를 입력하세요.")
    # else:
    #     print("숫자로된 정수를 입력하세요.")

    # try:
    #     num1=input("첫 번째 정수를 입력해주세요:")
    #     num2=input("두 번째 정수를 입력해주세요:")

    #     return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
    # except:
    #     print("0이 아닌 숫자로는 정수를 입력해주세요!!")
    # # 훨씬 편함

    try:
        num1=int(input("첫 번째 정수를 입력해주세요:"))
        num2=int(input("두 번째 정수를 입력해주세요:"))
        result=num1/num2
        # return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
    # except ValueError:
    #     print("숫자로된 정수를 넣어주세요!!")
    # except ZeroDivisionError:
    #     print("제발 0을 입력하지 마세요!!")
    except Exception as e: 
        print(e)
    # else: #try가 참일 때 발생하는데 try에서 이미 리턴값이 있으므로 의미없다
    #     print("정상적으로 나누기 함수가 호출되었습니다")
    # finally:#try가 거짓이여도, 참이고 리턴값 있어도 무조건 발생한다
    #     print("정상적으로 나누기 함수가 호출되었습니다!")
    else:
        print("정상적으로 나누기 함수가 호출되었습니다!")
        return print("{}을 {}로 나눈 값은 {}입니다.".format(num1,num2,result))

division()
# help(KeyboardInterrupt)
#valueError, zerodivisionerror, keyboardinterrupt
