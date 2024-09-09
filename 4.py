#Cria um dicionário de valores contendo cada número pré-definido.
df = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


def calculadora_de_porcentagem(df): #Recebe o data_Frame/dicionário como parâmetor
    valores = df.values() #Retorna todos os valores da chave do DF
    valores_lista = list(valores) #Os valores tornam-se arrays.
    cem_porcento = sum(valores_lista) #Define 100% como a soma dos fatores

    porcentagens = []  #Cria um array vazio para concatenação
    for valor in valores_lista: #Para cada valor na lista de valores
        porcentagem = (valor * 100) / cem_porcento #Realiza um cálculo de regra de três simples
        porcentagens.append(porcentagem) #Concatena ao array vazio as porcentagens

    print (porcentagens) #Printa cada valor do array

#Chamando a função
calculadora_de_porcentagem(df)
