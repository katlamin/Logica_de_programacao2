'''Crie uma função chamada ordenar_lista 
que recebe uma lista de números e retorna
a lista ordenada em ordem crescente.'''

'''def ordenar_lista (lista):
    return sorted(lista)

numeros = [5, 2, 9, 1, 7]
lista_ordenada = ordenar_lista(numeros)
print(lista_ordenada)  # Saída: [1, 2, 5, 7, 9]'''


#CORREÇÃO THAIS

def ordenar_lista(lista):
    if not lista:
        return []
    
    #ORDENAR A LISTA
    lista_ordenada = sorted(lista)
    
    print(f"Lista ordenada: {lista_ordenada}")

lista1 = [6,9,10,4,3]
ordenar_lista(lista1)