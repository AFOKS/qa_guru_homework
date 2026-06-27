a = int(input())
b = int(input())
c = int(input())


if a!=b and b!=c:
    print('Разносторонний')
elif a == b == c:
    print('Равносторонний')
else:
    print('Равнобедренный')

# a = int(input())
#
# if a <= 13:
#     print('детство')
# if 14 <= a <= 24:
#     print('молодость')
# if 25 <= a <= 59:
#     print('зрелость')
# if 60 <= a:
#     print('старость')