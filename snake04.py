from typing import List

def find_snake_on_grid(grade: List[str]) -> List[List[int]]:
    # Movimentos representados por caracteres
    movimentos = {
        '>': (1, 0),  # Direita
        '<': (-1, 0),  # Esquerda
        '^': (0, -1),  # Cima
        'v': (0, 1),  # Baixo
        'h': (0, 0)   # Cabeça
    }
    
    # Encontrar a cabeça da cobra ('h')
    x_atual, y_atual = -1, -1
    for y, linha in enumerate(grade):
        for x, char in enumerate(linha):
            if char == 'h':
                x_atual, y_atual = x, y
                break
        if x_atual != -1 and y_atual != -1:
            break
    
    # Verificar se a cabeça foi encontrada
    #if x_atual == -1 or y_atual == -1:
        #raise ValueError("Cabeça da cobra ('h') não encontrada na grade.")
    
    # Inicia o caminho com a posição da cabeça
    caminho = [[x_atual, y_atual]]
    
    while True:
        # Direção atual
        direcao = grade[y_atual][x_atual]
        
        # Verifica se a direção é válida
        if direcao not in movimentos:
            break
        
        # Movimento atual
        dx, dy = movimentos[direcao]
        x_prox, y_prox = x_atual - dx, y_atual - dy
        
        # Verifica se a próxima posição é válida
        if not (0 <= x_prox < len(grade[0]) and 0 <= y_prox < len(grade)):
            break
        
        # Verifica se a próxima posição contém parte da cobra
        prox_direcao = grade[y_prox][x_prox]
        if prox_direcao not in movimentos or [x_prox, y_prox] in caminho:
            break
        
        # Adiciona a próxima posição ao caminho
        caminho.append([x_prox, y_prox])
        
        # Atualiza a posição atual
        x_atual, y_atual = x_prox, y_prox
    
    return caminho


# Teste com a grade fornecida
grade = [
    " >>h   ",
    " ^   v ",
    " ^<<<< ",
]

resultado = find_snake_on_grid(grade)
print("Caminho encontrado:", resultado)
