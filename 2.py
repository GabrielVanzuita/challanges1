def fibonacci(n, testes): #Número inicial, quantidade de testes
    sequencia = [] #Array vazia para armazenar os valores
    a, b = 0, 1 #A = 0, B = 1
    while len(sequencia) < testes: #Enquanto o tamanho da tentativa/sequência (loop)
        sequencia.append(a)        #for menor que testes, sequencia escreva na sequência
        a, b = b, a + b            #atualiza os valores de a e b, a partir de B, sendo o proximo "a", b+a
    if n in sequencia:             #se a entrada N estiver na sequencia:
        print(f"{n} é Fibonacci")  #É fibonacci
    else:                          #Caso contrário
        print(f"{n} não é Fibonacci") #Não é Fibonacci.

#Chamando a funçao
n = 0
testes = 0
fibonacci(n, testes)
