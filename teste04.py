def escolher_empresa(TF1: str, VQR1: str, TF2: str, VQR2: str) -> str:
    # Converter os valores recebidos de string para float
    TF1, VQR1, TF2, VQR2 = map(float, (TF1, VQR1, TF2, VQR2))

    # Se os valores por quilômetro são iguais
    if VQR1 == VQR2:
        if TF1 < TF2:
            return "Empresa 1"
        elif TF1 > TF2:
            return "Empresa 2"
        else:
            return "Tanto faz"
    
    # Calcular o ponto de igualdade (se existe)
    if VQR1 != VQR2:
        N = (TF2 - TF1) / (VQR1 - VQR2)
        if N > 0:
            if VQR1 < VQR2:
                return f"Empresa 1 quando a distância < {N:.1f}, Tanto faz quando a distância = {N:.1f}, Empresa 2 quando a distância > {N:.1f}"
            else:
                return f"Empresa 2 quando a distância < {N:.1f}, Tanto faz quando a distância = {N:.1f}, Empresa 1 quando a distância > {N:.1f}"
    
    # Caso não exista um ponto de igualdade
    if VQR1 < VQR2:
        return "Empresa 1"
    else:
        return "Empresa 2"

# Exemplo de uso
TF1 = "2.50"
VQR1 = "1.00"
TF2 = "5.00"
VQR2 = "0.75"

resultado = escolher_empresa(TF1, VQR1, TF2, VQR2)
print(resultado)
