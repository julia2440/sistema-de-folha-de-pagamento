"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Heloisa Lima de Oliveira
2 - júlia Vitória dos Santos Azevedo Jesus
"""
import os
os.system("cls||clear")


def calcular_inss(salario):
    if salario <= 1100:
        return salario * 0.075
    elif salario <= 2203.48:
        return salario * 0.09
    elif salario <= 3305.22:
        return salario * 0.12
    elif salario <= 6433.57:
        return salario * 0.14
    else:
        return 854.36

def calcular_irrf(salario, dependentes):
    if salario <= 2259.20:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075 - (189.59 * dependentes)
    elif salario <= 3751.05:
        return salario * 0.15 - (189.59 * dependentes)
    elif salario <= 4664.68:
        return salario * 0.225 - (189.59 * dependentes)
    else:
        return salario * 0.275 - (189.59 * dependentes)

def calcular_salario_liquido(salario, vale_transporte, vale_refeicao, dependentes):
    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario, dependentes)
    
    desconto_vale_transporte = 0.06 * salario if vale_transporte == 's' else 0
    desconto_vale_refeicao = 0.20 * vale_refeicao
    
    total_descontos = inss + irrf + desconto_vale_transporte + desconto_vale_refeicao
    salario_liquido = salario - total_descontos
    
    return salario_liquido

def main():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    
    salario_base = float(input("Digite seu salário base (R$): "))
    vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower()
    vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))
    
    # Considerando que o funcionário tem 1 dependente
    dependentes = 1

    salario_liquido = calcular_salario_liquido(salario_base, vale_transporte, vale_refeicao, dependentes)
    
    print(f"\nSalário líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()
