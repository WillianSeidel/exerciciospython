def horario (time_str):
   
    desenho = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"]
    }

    linhas = ["", "", ""]

    for char in time_str:
        if char == ':':
            for i in range(3):
                if i > 0:
                    linhas[i] += " . "
                else:
                    linhas[i] += "  "
        else:
            n_desenho = desenho[char]
            for i in range(3):
                linhas[i] += n_desenho[i] + " "

    # Remover espaços à esquerda do zero inicial (se houver)
    if time_str[0] == '0':
        for i in range(3):
            linhas[i] = linhas[i][1:]

    return linhas


hora = "11:03"
display = horario(hora)
for line in display:
    print(line)

