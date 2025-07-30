def dia_da_semana(numdia):
    match numdia:
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
            return"Dia inválido"


print(dia_da_semana ("5"))
print(dia_da_semana("10"))
