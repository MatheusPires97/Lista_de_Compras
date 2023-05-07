# Calculadora simples 

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = None
    num_1_float = 0
    num_2_float = 0

# Aqui utilizei o try e o except para mudar o valor das variaveis,
# por mais que possa ser considerado uma má pratica. 
# Futuramente atualizarei essa seção.

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

# Aqui utilizei algumas condições para caso os valores imputados sejam invalidos.

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Invalido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador.')
        continue

    # Calculo e o resultado de cada operador escolhido.

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)

    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)

    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)

    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)

    else:
        print('Não deveria ter chegado até aqui')

# Após operação realizada é mostrado a opção de sair do programa se desejar.

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break