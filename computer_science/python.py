# Sprint 2 - Simulação da Lógica Digital em Python



## Objetivo
# Representar em Python o circuito lógico desenvolvido na Sprint 1.

### Equação Lógica

# S = (A AND B) OR (B AND C)

### Entradas
#- A
#- B
#- C

### Saída
#- S

# ENTRADAS
# Digite apenas 0 ou 1


A = int(input("Informe o valor de A (0 ou 1): "))
B = int(input("Informe o valor de B (0 ou 1): "))
C = int(input("Informe o valor de C (0 ou 1): "))

# VALIDAÇÃO DAS ENTRADAS


if A not in [0, 1] or B not in [0, 1] or C not in [0, 1]:
    print("ERRO: Utilize apenas valores 0 ou 1.")

# PORTA 1
# A AND B


porta_1 = A and B

print("Resultado da Porta 1 =", int(porta_1))

# PORTA 2
# B AND C


porta_2 = B and C

print("Resultado da Porta 2 =", int(porta_2))

# SAÍDA FINAL
# (A AND B) OR (B AND C)


S = porta_1 or porta_2

print("Saída Final S =", int(S))

# INTERPRETAÇÃO DO RESULTADO


if S == 1:
    print("Sistema ATIVADO")
else:
    print("Sistema DESATIVADO")

## Explicação do Funcionamento

# 1. As entradas A, B e C recebem valores 0 ou 1.
# 2. A Porta 1 executa a operação lógica AND entre A e B.
# 3. A Porta 2 executa a operação lógica AND entre B e C.
# 4. Os resultados das duas portas são enviados para uma porta OR.
# 5. A saída final S representa o resultado do circuito desenvolvido na Sprint 1.

### Fórmula

# S = (A AND B) OR (B AND C)
