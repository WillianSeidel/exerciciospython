gastos_joao = [300, 500, 100, 200]
gastos_pedro = [300, 500, 100, 200]

#Primeiro preciso somar cada lista e segundo comparar o maior e imprimir

total_gasto_joao = sum(gastos_joao)
total_gasto_pedro = sum(gastos_pedro)

if total_gasto_joao > total_gasto_pedro:
    print("Joao gastou mais")
elif total_gasto_joao < total_gasto_pedro:
    print("Pedro gastou mais")
else:
    print("os dois gastaram igual")



willian = [10, 20, 50, 100, 500]
julia = [11, 20, 50, 100, 500]

#primeiro preciso somar a lista e armazenar em uma variavel e depois preciso comparar a lista.
total_willian = sum(willian)
total_julia = sum(julia)

if total_willian > total_julia:
    print("Willian GASTOU MAIS")
elif total_willian < total_julia:
    print("Julia GASTOU MAIS")
else:
    print("gastaram igual")