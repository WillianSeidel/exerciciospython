def escolhe_taxi(tf1, vqr1, tf2, vqr2):
    # Convertendo os valores para float
    tf1 = float(tf1)
    vqr1 = float(vqr1)
    tf2 = float(tf2)
    vqr2 = float(vqr2)
    
    # Se as tarifas por quilômetro são iguais
    if vqr1 == vqr2:
        if tf1 == tf2:
            return "Tanto faz"
        else:
            return f"Empresa {1 if tf1 < tf2 else 2}"
    else:
        # Calculando o ponto de equilíbrio da distância
        distancia_equilibrada = (tf2 - tf1) / (vqr1 - vqr2)
        
        # Se a distância equilibrada for negativa, a Empresa 1 é mais barata em qualquer distância
        if distancia_equilibrada < 0:
            return f"Empresa {1 if tf1 < tf2 else 2}"
        
        # Retorna a escolha das empresas dependendo da distância
        return (
            f"Empresa {2 if vqr1 < vqr2 else 1} quando a distância < {distancia_equilibrada:.1f}, "
            f"Tanto faz quando a distância = {distancia_equilibrada:.1f}, "
            f"Empresa {1 if vqr1 < vqr2 else 2} quando a distância > {distancia_equilibrada:.1f}"
        )

# Teste com os valores fornecidos
tf1 = "2.50"
vqr1 = "1.00"
tf2 = "5.00"
vqr2 = "0.75"

resultado = escolhe_taxi(tf1, vqr1, tf2, vqr2)
print(resultado)
