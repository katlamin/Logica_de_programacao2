
'''Crie uma função estado_luz (status) que recebe uma string com
o estado da luz: "ligado", "desligado", "piscando". 
Use match-case para retornar as seguintes mensagens:
"Luz ligada" para "on"
"Luz apagada" para "off"
"Luz piscando" para "blnk"
se for qualquer outro valor, "Estado desconhecido"
'''

def EstadoLuz(luz):
 match luz:
        case "ligado":
            return"ON"
     
        case "desligado":
            return"OFF"
     
        case "piscando":
            return"BLINK"
        case _: 
            return"A lampada queimou!"


estado_luz= input("Como está a luz?:  ")


resultado= EstadoLuz(estado_luz)
print(resultado)
