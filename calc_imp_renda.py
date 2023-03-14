primeiro_caso = 1903.98

segundo_caso = 2826.65
irpf_seg_caso = 142.80

terceiro_caso = 3751.05
irpf_terc_caso = 354.80

quarto_caso = 4664.68
irpf_quarto_caso = 636.13

quinto_caso = 4664.68
irpf_quinto_caso = 869.36

name = str(input("Insira o nome do colaborador:"))
salario = float(input("Insira o valor do salário bruto do colaborador:"))

if salario <= primeiro_caso:
    print(f"O colaborador {name} está isento do impostos.")
elif salario <= segundo_caso:
    print(
        f"O colaborador {name} deverá pagar R${irpf_seg_caso} de imposto e receberá R${salario - irpf_seg_caso} de salário líquido.")
elif salario <= terceiro_caso:
    print(
        f"O colaborador {name} deverá pagar R${irpf_terc_caso} de imposto e receberá R${salario - irpf_terc_caso} de salário líquido.")
elif salario <= quarto_caso:
    print(
        f"O colaborador {name} deverá pagar R${irpf_quarto_caso} de imposto e receberá R${salario - irpf_quarto_caso} de salário líquido.")
else:
    print(
        f"O colaborador {name} deverá pagar R${irpf_quinto_caso} de imposto e receberá R${salario - irpf_quinto_caso} de salário líquido.")
