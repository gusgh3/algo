import sys
sys.stdin = open('input.txt')

T = int(input())

print(T)

for tc in range(1, t+1):
    char = input()

    if char.islower():
        print(f'{tc} {char}는 소문자입니다')
    else:
        print(f'{tc} {char}는 대문자입니다')
