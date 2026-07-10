a = int(input())
b = int(input())
c = int(input())

if a != b and b != c:
    print('Разносторонний')
elif a == b == c:
    print('Равносторонний')
else:
    print('Равнобедренный')
