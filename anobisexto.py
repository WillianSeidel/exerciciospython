def verificador_ano_bissexto():
    ano = int(input())
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):        
        print("sim")
    else:
        print("nao")

verificador_ano_bissexto()
