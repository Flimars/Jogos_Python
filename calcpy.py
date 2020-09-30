
# Desfinindo a função calculadora.
def calculadora_py():

# Escolha para entrada do operador algébrico.
        operador = input('''        
    Escoha operação desejada: 
    + para Adição
    - para Subtração
    / para Divisão
    * para Multiplicação
    ''')
# Recebendo dados de entrada do usuário.
        a = int(input('Digite o primeiro número: '))
        b = int(input('Digite o segundo número: '))

# Adição
        if(operador == '+'):
            soma = a + b
            print('{} + {} = '.format(a,b))
            print(soma)

# Subtração
        elif(operador == '-'):
            subtração = a - b
            print('{} + {} = '.format(a,b))
            print(subtração)

# Multiplicação
        elif(operador == '*'):
            multip = a * b
            print('{} + {} = '.format(a,b))
            print(multip)

# Divisão
        elif(operador == '/'):
            divisão = float(a / b)
            print('{} + {} = '.format(a,b))
            print(divisão)
# Menssagem de Erro.
        else:
            print('ERRO: Operador digitado é inválido!')

    def repetir():

# Receber dados do usuário.
        repet_calc = input('''
        Você quer calcular novamente?
        Digite S para SIM ou N para NÃO.
        ''')  
# Se digitar S, execute a função calculadora_py():
            if(repet_calc.upper() == 'S'):
                calculadora_py()

            elif(repet_calc.upper() == 'N'):    
                print('Obrigado! Até logo!')

        # Se usuário digitar outra tecla, execute novamente
            else:
                repetir()    

        calculadora_py()
