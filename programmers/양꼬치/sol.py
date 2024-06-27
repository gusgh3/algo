def solution(n, k):
    answer = 0

# n : 양꼬치 몇인분 / k : 음료수

food_price = n * 12000

if n >= 10:
   service = n // 10
   drnik_price = (k - service) * 2000
else:
    drnik_price = k * 2000

answer = food_price + drnik_price
return answer

print(solution(10,3))