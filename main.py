import random as r
aL = 10000000#염기 전체 길이
primerL = 6#프라이머 길이
a = []
primer1 = []#1번 프라이머
primer2 = []#2번 프라이머

#프라이머, 염기 만들기
for i in range(primerL):
    a.append(r.randint(1,4))
    primer1.append(a[i])
    primer2.append(r.randint(1,4))

print(primer1)
print(primer2)
for i in range(aL-primerL-primerL):
    a.append(r.randint(1,4))
for i in range(primerL):
    a.append(primer2[i])
#print(a)
print()
#끝
LL  = 0
find = 0
k = 0
I = 0
for i in range(aL):
    if(a[i] == primer1[0]):
        for j in range(primerL):
            if j == primerL-1:
                find = 1
                k = 0
                l = []
                while find == 1:
                    l.append(a[i+k])
                    if(a[i+k] == primer2[0]):
                        for j in range(primerL):
                            if primerL-1 == j:
                                find = 0
                            elif a[i+k+j] != primer2[j]:
                                break
                            l.append(a[i+j+k])
                    k += 1  
                print("\na")
                LL +=1
            elif i+j == aL-1:
                break
            elif a[i+j] != primer1[j]:
                break
print()
print(LL)
##결과 : 프라이머 2개, 나오는 부산물 수
