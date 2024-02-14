
chave = input("Digite a base de sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": 
        senha = senha + "!"
    elif letra in "Bb": 
        senha = senha + "11"
    elif letra in "Cc": 
        senha = senha + "12"
    elif letra in "Dd": 
        senha = senha + "13"    
    elif letra in "Ee": 
        senha = senha + "@"
    elif letra in "Ff": 
        enha = senha + "15"
    elif letra in "Gg": 
        senha = senha + "16"
    elif letra in "Hh": 
        senha = senha + "17"
    elif letra in "Ii":
        senha = senha + "#"
    elif letra in "Jj":
        senha = senha + "19"
    elif letra in "Kk":
        senha = senha + "20"
    elif letra in "Ll":
        senha = senha + "21"
    elif letra in "Mm":
        senha = senha + "22"
    elif letra in "Nn":
        senha = senha + "23"
    elif letra in "Oo":
        senha = senha + "$"
    elif letra in "Pp":
        senha = senha + "24"
    elif letra in "Qq":
        senha = senha + "25"
    elif letra in "Rr":
        senha = senha + "26"
    elif letra in "Ss":
        senha = senha + "27"
    elif letra in "Tt":
        senha = senha + "28"
    elif letra in "Vv":
        senha = senha + "29"
    elif letra in "Ww":
        senha = senha + "30"
    elif letra in "Xx":
        senha = senha + "31"
    elif letra in "Yy":
        senha = senha + "32"
    elif letra in "Zz":
        senha = senha + "33"
    

    else: senha = senha + letra
print(senha)


def exportar_senhas_para_txt(senhas, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for senha in senhas:
                arquivo.write(senha + '\n')
        print("Senhas exportadas com sucesso para", nome_arquivo)
    except Exception as e:
        print("Erro ao exportar senhas:", str(e))
