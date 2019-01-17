import random

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1
cnt = 0
print("[타자 게임] 준비되면 enter!")
input()

q = random.choice(w)
while n <= 5:
    print("*문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(w)
    else:
        print("오타! 다시 도전!")
        cnt = cnt + 1

print("맞은 수 : ", 5 - cnt)
print("오타 수 : ", cnt)
