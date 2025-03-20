s = int(input())

for i in range(s+1):
    print(" " * (s-i) , end ="")
    for j in range(i):
        print(chr(65+j) , end = " ")
    print()
    
s = i

while i > 0 :
    print(" " * (s-i) , end =" ")
    for j in range(i-1):
        print(chr(65+j) , end = " ")
    print()
    i -=1
