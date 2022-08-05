import re

def check_author(author):  # verifica se as condições do Autor conferem
    if(re.search(r'\W+', author)):  # verifica a existência de caracteres não alfanuméricos
        return False
    if(not(re.search(r'^[a-zA-Z]', author))):   # verifica se a primeira letra não é um caracter alfabético
        return False
    if(len(re.findall(r'[0-9]', author))>len(re.findall(r'[a-zA-Z]', author))):  # verifica se a quantidade de chars numéricos é maior que os alfabéticos
        return False
    #print("Autor OK")  # debug
    return True  # se nenhuma condição false for encontrada, retorna-se true

def check_password(password):
    if(not(re.search(r'^[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}\.[A-F0-9]{2}$', password))):  # verifica se o elemento está fora do formato e se existem caracteres diferentes de [A-F0-9.]
        return False
    if(re.search(r'[A-F]{2}|0{2}|1{2}|2{2}|3{2}|4{2}|5{2}|6{2}|7{2}|8{2}|9{2}', password)):  # verifica a existência de duas letras ou números duplicados em uma dupla
        return False
    #print("Senha OK")  # debug
    return True  # se nenhuma condição false for encontrada, retorna-se true

def check_ip(ip):
    if(not(re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', ip))):  # verifica se o elemento está fora do formato, se existem caracteres não numéricos e se está no range [0-255]
        return False
    numbers = ip.split(".")  # separa os números do ip e armazena numa lista
    for i in range(len(numbers)):  # percorre a lista de números do ip
        if(int(numbers[i])>255):  # verifica se os números do ip são maiores que 255
            return False
    #print("IP OK")  # debug
    return True

def check_email(email):
    if(not(re.search(r'^[a-zA-Z].*@.*\..*', email))):  # verifica se o email começa com letra, possui um @ e . após @
        return False
    #print("Email OK")  # debug
    return True

def check_trans(trans):
    if(not(re.search(r'^pull$|^push$|^stash$|^fork$|^pop$', trans))):  # verifica se a transação possui alguma string além de pull,push,stash,fork,pop
        return False
    #print("Trans OK")  # debug
    return True

def check_repo(repo):
    if(not(re.search(r'^[_a-z0-9]+$', repo))):  # verifica se a string repositório se encaixa no formato
        return False
    #print("Repo OK")  # debug
    return True

def check_hash(hash):
    if(not(re.search(r'^[0-9a-f]{32}$', hash))):  # verifica se a string repositório se encaixa no formato
        return False
    #print("Hash OK")  # debug
    return True

request = input()  # recebe a linha de transação
elements = request.split(" ")  # separa a linha de transação em elementos
if(check_author(elements[0]) and check_password(elements[1]) and check_ip(elements[2]) and check_email(elements[3]) and check_trans(elements[4]) and check_repo(elements[5]) and check_hash(elements[6])):  # verifica se todas as condições dos elementos são True e retorna a condição da transação
    print("True")
else:
    print("False")
