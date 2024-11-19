
altura = 4
largura = 2

def calcula_total_leds(altura, largura):
    
    if altura <= 0 or largura <= 0:
        return 0
    else:   
        linhasAltura = altura + 1
        linhasLargura = largura + 1
        total = linhasAltura * linhasLargura
        return total
    
total = calcula_total_leds(altura, largura)
if total == 0:
    print("Digito inválido")
else:
    print(f"O total é {total}")

