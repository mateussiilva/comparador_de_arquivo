
# from pprint import pprint as print


arquivo_base = "base.txt"
arquivo_teste = "teste.txt"


# def ler_linhas_file(nome_arquivo:str) -> list:
    
    
with open(arquivo_base,"r") as file:
    linhas = list(map(
        lambda t: t.rstrip("\n"),
        file.readlines()
    ))
    # linhas = file.readlines()
    
    
for linha in linhas:
    two_point = linha.rfind(":")
    if two_point != -1:
        print(linha) 
    
    
# print(linhas)