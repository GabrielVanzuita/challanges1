#Lógica do Loop:
#Para cada caractere no alcace (tamanho(do texto) comece a partir do índice -1 (
#(primeiro caractere ao contrário), o range percorre a partir da direção do -1 até o 0, sem
#contar o -1, e -1 como parâmetro de movimentação
#   (Imaginando a reta dos números racionais, o range percorre o valor ao contrário
#   até chegar no -1).
def reverter_string(texto): #Recebe o texto string como parâmetro
    string_reversa = "" #Cria uma string vazia que será concatenada
    for i in range(len(texto) - 1, -1, -1):
        string_reversa += texto[i] #Concatena o texto na string vaziao criada
    print(string_reversa) #Printa a string_reversa

#Função na prática
texto = "Target"
reverter_string(texto)


