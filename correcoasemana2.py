def dia_da_semana(numero):
 match numero:
        case "1" :
            return"Segunda-feira"
        case "2" :
            return"Terça-feira"
        case "3" :
            return"Quarta-feira"
        case "4" :
            return"Quinta-feira"
        case "5" :
            return"Sexta-feira"
        case "6" :
            return"Sábado"
        case "7" :
            return"Domingo"
        case _: 
            return"Dia inválido!"

#FORA DA FUNÇÃO!
entrada= input("Digite um número de 1 a 7 para o dia da semana: ")

#chamar a função com o valor de entrada
resultado= dia_da_semana(entrada)
print(resultado)
