# Mapeamento de segmentos para cada caractere
CONSTNUMEROS = {
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
   # ':':,
}

# Função para construir o display
def mostrarhorario(time_str):
    # Estrutura do display: cada índice corresponde a uma linha
    lines = ["", "", "", "", ""]

    for i in time_str:
        display = CONSTNUMEROS[i]
        # Montar as linhas do display para cada caractere
        lines[0] += f" {'_' if 'a' in display else '  '}  "
        lines[1] += f"{'|' if 'f' in display else ' '} '.' {'|' if 'b' in display else ' '}  "
        lines[2] += f" {'_' if 'g' in display else '  '}  "
        lines[3] += f"{'|' if 'e' in display else ' '} '.' {'|' if 'c' in display else ' '}  "
        lines[4] += f" {'_' if 'd' in display else '  '}  "
    
    # Imprimir o display
    print(lines[0])
    print(lines[1])
    print(lines[2])
    print(lines[3])
    print(lines[4])

# Exemplo: mostrar o horário "13:03"
mostrarhorario("11:03")
