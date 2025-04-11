basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 중복 제거됨

print('orange' in basket)  # True
print('crabgrass' in basket)  # False

# 집합 연산
a = set('abracadabra')
b = set('alacazam')

print("a 집합:", a)  # 유일한 글자들
print("a - b 차집합:", a - b)
print("a | b 합집합:", a | b)
print("a & b 교집합:", a & b)
print("a ^ b 여집합:", a ^ b)
