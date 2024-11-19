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

    # Função personalizada para gerar combinações
    def gerar_combinacoes(signal):
        if not signal:
            return [""]
        primeiro = [".", "-"] if signal[0] == "?" else [signal[0]]
        restante = gerar_combinacoes(signal[1:])
        return [p + r for p in primeiro for r in restante]

    # Gera todas as combinações possíveis
    combinacao_signals = gerar_combinacoes(signals)
    
    # Obtém as letras correspondentes a cada combinação possível
    result = []
    for signal in combinacao_signals:
        if signal in DICSINAL:
            result.extend(DICSINAL[signal])
    
    return set(result)

# Exemplos de uso
print(possibilities("."))    # ["E"]
print(possibilities("-"))    # ["T"]
print(possibilities("-.") )  # ["N"]
print(possibilities("..."))  # ["S"]
print(possibilities("..-"))  # ["U"]
print(possibilities("?"))    # ["E", "T"]
print(possibilities(".?"))   # ["I", "A"]
print(possibilities("?-?"))  # ["R", "W", "G", "O"]
