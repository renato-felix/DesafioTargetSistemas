n = int(input('Informe um número para saber se pertence à sequência de Fibonacci '))
t1 = int(0)
t2 = int(1)
t3 = 0
print(t1, t2, end=' ')

while t3 < n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end=' ')

if n == t3:
    print('\nEsse número pertence à sequência de Fibonacci')
else:
    print('\nEsse número não pertence à sequência de Fibonacci')