from typing import List

def possibilities(signals: str) -> List[str]:
  DICSINAL = {
  "": ["E", "T"],
  ".": ["E"],
  "-": ["T"],
  "..": ["I"],
  ".-": ["A"],
  "-.": ["N"],
  "--": ["M"],
  "...": ["S"],
  "..-": ["U"],
  ".-.": ["R"],
  ".--": ["W"],
  "-..": ["D"],
  "-.-": ["K"],
  "--.": ["G"],
  "---": ["O"]
}
  def generate_combinations(current_string, index):
        if index == len(signals):
            if current_string in DICSINAL:
                return DICSINAL[current_string]
            return []

        if signals[index] == '?':
            return generate_combinations(current_string + ".", index + 1) + \
                   generate_combinations(current_string + "-", index + 1)
        else:
            return generate_combinations(current_string + signals[index], index + 1)
  return generate_combinations("", 0)


print(possibilities("."))
print(possibilities("-"))
print(possibilities("-."))
print(possibilities("..."))
print(possibilities("..-"))
print(possibilities("?"))
print(possibilities(".?"))   
print(possibilities("?-?")) 


#adicionaria set e o sorted para melhorar o código ordando a lista