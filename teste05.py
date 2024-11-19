from itertools import product
from typing import List

# Mapeamento de Código Morse para letras

def possibilities(signals: str) -> List[str]:
    # Gera todas as combinações possíveis substituindo '?' por '.' e '-'
    MORSE_MAP = {
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



    possible_signals = [
        "".join(combination)
        for combination in product(*[[".", "-"] if char == "?" else [char] for char in signals])
    ]
    
    # Obtém as letras correspondentes a cada combinação possível
    result = []
    for signal in possible_signals:
        if signal in MORSE_MAP:
            result.extend(MORSE_MAP[signal])
    
    # Remove duplicatas e retorna em ordem
    return sorted(set(result))

# Exemplos de uso
print(possibilities("."))    # ["E"]
print(possibilities("-"))    # ["T"]
print(possibilities("-.") )  # ["N"]
print(possibilities("..."))  # ["S"]
print(possibilities("..-"))  # ["U"]
print(possibilities("?"))    # ["E", "T"]
print(possibilities(".?"))   # ["I", "A"]
print(possibilities("?-?"))  # ["R", "W", "G", "O"]
