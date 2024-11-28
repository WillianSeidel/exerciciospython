from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    direcao = { '<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1), 'h': None}
    cabeca = None
    for y, linha in enumerate(grid):
      for x, letra in enumerate(linha):
        if letra == 'h':
          cabeca = (x, y)
          break
        if cabeca:
          break
    caminho = [cabeca]
    posicao = cabeca
    
    while True:
      x, y = posicao
      posicao_cabeca = grid[y][x]
      
      if posicao_cabeca == 'h':
        prox_x, prox_y = x - 1, y
      else:
        dire_x, dire_y = direcao[posicao_cabeca]
        prox_x, prox_y = x + dire_x, y + dire_y
      
      proximo_pos = (prox_x, prox_y)
      
      if proximo_pos in caminho or not (0 <= prox_y < len(grid)) or not (0 <= prox_x < len(grid[0])):
        break
      caminho.append(proximo_pos)
      atual = proximo_pos   
    return caminho
grid = [
" >>h   ",
" ^   v ",
" ^<<<< ",
]
for linha in grid:
  print(linha)
find_snake_on_grid(grid)