def caminho_da_cobra(grade):
    # Mapeamento das direções
    direcoes = {
        '>': (1, 0),  # Direita
        '<': (-1, 0), # Esquerda
        '^': (0, -1), # Cima
        'v': (0, 1),  # Baixo
        'h': None     # Cabeça
    }

    # Encontrar a cabeça da cobra
    print("Procurando a cabeça da cobra na grade...")
    for y, linha in enumerate(grade):
        for x, caractere in enumerate(linha):
            if caractere == 'h':
                cabeca = (x, y)
                print(f"Cabeça encontrada em: {cabeca}")
                break
    
    # Inicializar o caminho com a cabeça
    caminho = [cabeca]
    atual = cabeca

    print("Rastreando o corpo da cobra...")
    while True:
        x, y = atual
        caractere_atual = grade[y][x]

        if caractere_atual == 'h':
            # Para 'h', procuramos à esquerda para encontrar o próximo segmento
            proximo_x, proximo_y = x - 1, y
        else:
            # Usar a direção indicada pelo caractere atual
            dx, dy = direcoes[caractere_atual]
            proximo_x, proximo_y = x + dx, y + dy

        proximo_pos = (proximo_x, proximo_y)

        # Verificar se chegamos ao final da cobra
        if proximo_pos in caminho or not (0 <= proximo_y < len(grade)) or not (0 <= proximo_x < len(grade[0])):
            print("Chegamos ao final da cobra.")
            break

        # Adicionar o próximo segmento ao caminho
        caminho.append(proximo_pos)
        atual = proximo_pos
        print(f"Segmento adicionado: {proximo_pos}")

    print("Caminho completo da cobra:")
    print(caminho)
    return caminho
 
# Exemplo de uso
grade = [
  " >>h   ",
  " ^   v ",
  " ^<<<< ",
]

print("Grade recebida:")
for linha in grade:
    print(linha)

caminho_da_cobra(grade)
