# 리스트list
odd=[1,2,3,4,5,6]
print(type(odd))

odd1=[1,3,"문자",[3,4,5]]

print(odd1[3][0])
#리스트 인덱싱, 슬라이싱
# a= [1,2,3]
#list의 a의 첫번쨰 값
#a[0]
#b = a[0] + a[2]
#print(b)
#print(a[-2])


a = "HEELO"
print(a[0:3])

a= [1,2,3,4,[1,2,3]]
print(a[-1][1:])

#리스트 연산(더하기, 곱하기, 길이구하기)
b=[1,2,12,13,14,15]
print(a+b)
print(b*3)
b1 = b * 3
#print(len(b1))

#리스트 수정, 삭제
k= [1,2,3]
k[1]=5
print(k)

del k[2]
print(k)
#List 추가
add1=3,4,5
k.append(add1)
print(k)

c= [5,3,18,20,1]
c.reverse()
print(c)

#리스트 안에 20이 위치하는 값
print(c.index(20))


#두번째자리에 4를 넣는다
c.insert(2,4)
c.append(2)
print(c)

#첫번째 값 지우기
c.remove(3)
print(c)

c.pop()
print(c)

c.pop(2)
print(c)

d=[1,2,3,3,3,3,2,5]
print(d.count(3))

d.extend(["사과","바나나"])
print(d)
# extend사용시, 대괄호 잊지 말것

#tuple
a=(1,2,3)
b=3,4,5
print(type(a),type(b))



#tuple의 값을 하나만 수정, 빼고, extend
#하지만 tuple끼리 더하고 빼고 연산은 가능

c=a+b
print(c)
print(c*4)

print(len(c))

#Dictionary
#사과와 바나나는 키 1000,5000은 밸류값

과일 = {"사과" : 1000, "바나나" : 5000}
print(과일)

person = {"name" : "김말이", "age" : 4}
person["birth"] = 123193
print(person)

del person["age"]
print(person)

grade = {"pey":10, "juliet": 99,"pey":20}
print(grade['pey'])
# 중복된 값을 입력하면 앞의 값이 무시됨
#리스트 넣으면 오류남

person = {"name":"김말이","age":4}

print(person.keys())
print(person.values())

print(person.items())

print(person.get("name"))

#"age"값이 person안에 있는지 없는지 확인하는 법
print("dog"in person)

person.clear()
print(person)

print(person)








