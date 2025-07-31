'''Desenvolver um programa para ajudar o setor
 de RH a analisar os salários dos colaboradores 
 de empresa
 
 Crie uma função chamada analisa-salarios() que 
 receba uma quantidade variável de salários (númetos reais)
 *A função de realizar as análises
 *Calcular a média salarial
 *Identificar o menor salário e o maior salário 
 *Contar quantos colaboradores ganham acima da média salarial
 *Calcular o total pago em salários'''

    #Correção Thais
def analisa_salarios(*salarios):
    if not salarios:
         return"Nenhum salário foi informado."
        
    #calcular a média salarial
    media_salarial = sum(salarios)/ len (salarios)

    #Identificação do menor e maior salário
    menor_salario = min(salarios)
    maior_salario = max(salarios)
    
    #Contar quantos colaboradores ganham acima da média salarial
    acima_media = 0
    for salario in salarios:
        if salario > media_salarial:
            acima_media +=1
    
    #total pago do salário

    total_pago = sum(salarios)

    #Retornar resultados
    return {
         "media_salarial": media_salarial,
         "menor_salario": menor_salario,
         "maior_salario": maior_salario,
         "colaboradores_acima_media": acima_media,
         "total_pago": total_pago
         }

print(analisa_salarios(1500,2000,2200,1800,3000,3500))
