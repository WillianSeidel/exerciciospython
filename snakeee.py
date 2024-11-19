def snake_path(grid):
    # Dimensões da grade
    rows = len(grid)
    cols = len(grid[0])
    
    # Mapeamento das direções
    directions = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, -1),
        'v': (0, 1),
        'h': None  # 'h' é a cabeça
    }
    
    # Encontre a cabeça da cobra
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 'h':
                head = (x, y)
                break
    
    # Inicializar o caminho
    path = [head]
    current = head

    while True:
        x, y = current
        current_char = grid[y][x]
        
        if current_char == 'h':
            # Início da cobra
            next_pos = (x - 1, y)  # O segmento da cobra está sempre ao lado esquerdo de 'h'
        else:
            # Próxima direção com base no caractere atual
            dx, dy = directions[current_char]
            next_pos = (x + dx, y + dy)
        
        if next_pos in path:
            break  # Terminamos de processar a cobra

        path.append(next_pos)
        current = next_pos

    return path

# Exemplo de uso
grid = [
  " >>>h   ",
  " ^   v ",
  " ^<<< ",
]

print(snake_path(grid))
