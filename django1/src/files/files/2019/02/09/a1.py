'''
def defaultfun(a,b,c,d,e,f=20,g=10):
    pass

def func(a=5,b=10,*args, **kwarges):
    pass
def print_info(**kwarges):#딕셔너리 타입
    print(kwarges)

    
def sum(*args):#튜플 타입
    print (args)
    isum = 0
    for i in args:
        isum += i

    return isum

print(sum())
print(sum(10,20,30,40,55,123,1255,))
a=[1,2,3,4,5,6,7,8,]
print(sum(*a))

print_info(name='아무개', age=99)
diction={'name':'홍길동','age':28}
print_info(**diction)

def add(a,b):
    return a+b

def dec(a,b):
    return b-a

diction={'a':5, 'b':100}
print('add()', add(**diction))
print('dec()', dec(**diction))
'''
#클래스 : 변수 + 함수 묶음
#클래스를 통해서 객체를 생성할 수 있음
#객체는 독립적인 데이터를 가지고 있어서 객체들간에 충돌이 일어나지 않는다.
class Cookie():
    pass #이 부분이 미완성일지언정 계속 진행 시킬 수 있다.
#객체생성 : 클래스이름()
a = Cookie()
b = Cookie()
print('a에 저장된 쿠키객체 : ', a)
print('b에 저장된 쿠키객체 : ', b)

#__name__ 변수의 값으로 해당파일이 실행된건지 임포트에 의해 실행된건지 확인할수 있다.

if __name__ == '__main__' : #테스트용 코드를 분리할 수 있음

    a = Family()
    b = Family()
    print(a.lastname, b.lastname)
    Family.lastname = "이" #클래스.클래스변수 = 값 > 
