import re # Regular Expression - RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 digitos + - (opcional) + 3 digitos

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]") #Coloca a ? depois de um elemento que pode aparecer uma ou nenhuma vez (opcional)
#padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}") #Coloca {} para definir a quantidade
#padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") #Coloca o intervalo para diminuir
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # Coloca que aparece de {0,1} ou seja, de zero a uma vez
busca = padrao.search(endereco) #Retorna o objeto Match (ou None)
if busca:
    cep = busca.group() #Retorna a string encontrada no padrão definido
    print(cep)
