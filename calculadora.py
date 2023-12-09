print('-'*40)
print('BEM VINDO À NOSSA CALCULADORA PYTHON')
print('-'*40)
n1 = float(input('Digite um número: '))
op = input('Qual operação deseja realizar (+, -, /, x)? ')
n2 = float(input('Digite o segundo número: '))

if op == '+':
    resultado = n1 + n2
    print('O resultado de {} {} {} = {}'.format(n1, op, n2, resultado))
elif op == '-':
    resultado = n1 - n2
    print('O resultado de {} {} {} = {}'.format(n1, op, n2, resultado))
elif op == '/':
    resultado = n1 / n2
    print('O resultado de {} {} {} = {}.'.format(n1, op, n2, resultado))
elif op == 'x':
    resultado = n1 * n2
    print('O resultado de {} {} {} = {}'.format(n1, op, n2, resultado))

print('Operação finalizada!')