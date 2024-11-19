dicionario = {
    '0': "abcdef",
    '1': "bc",
    '2': "abdeg",
    '3': "abcdg",
    '4': "bcfg",
    '5': "acdfg",
    '6': "acdefg",
    '7': "abc",
    '8': "abcdefg",
    '9': "abcdfg",
    ':': "g"  # Representa os dois pontos

}

# Função para construir um display de sete segmentos
def draw_segmented_display(time_str):
    # Linhas do display
    line1, line2, line3, line4, line5 = "", "", "", "", ""

    for char in time_str:
        segments = dicionario[char]
        
        # Linha 1: Topo (a)
        line1 += " " + ("--" if 'a' in segments else "  ") + "  "
        
        # Linha 2: Superior esquerdo (f) e direito (b)
        line2 += ("|" if 'f' in segments else " ") + "  " + ("|" if 'b' in segments else " ") + "  "
        
        # Linha 3: Meio (g)
        line3 += " " + ("--" if 'g' in segments else "  ") + "  "
        
        # Linha 4: Inferior esquerdo (e) e direito (c)
        line4 += ("|" if 'e' in segments else " ") + "  " + ("|" if 'c' in segments else " ") + "  "
        
        # Linha 5: Base (d)
        line5 += " " + ("--" if 'd' in segments else "  ") + "  "
    
    # Imprimir as linhas do display
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

# Exemplo: mostrar o horário "13:03"
draw_segmented_display("13:03")
