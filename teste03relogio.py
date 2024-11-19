def test_11_03(time_: str) -> str:
  desenho = {
    '0': ["  _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"]
  }
  
  linhas = ["","","",""]
  
  for busca in time_:
    if busca == ':':
      for i in range (3):
        if i > 0:
          linhas[i] += " . "
        else:
          linhas[i] += "  "
    else:
      n_desenho = desenho[busca]
      for i in range (3):
        linhas[i] += n_desenho[i] + " "
  if time_[0] == '0':
    for i in range(3):
      linhas[i] = linhas[i][1:]
      
  return linhas
      
hora = "11:03"
display = test_11_03(hora)
for linha in display:
  print(linha)