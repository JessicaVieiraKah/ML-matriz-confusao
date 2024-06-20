# Definir os valores da matriz de confusão
VP = 50
VN = 35
FP = 5
FN = 10

# Calcular as métricas
def calcular_acuracia(VP, VN, FP, FN):
    return (VP + VN) / (VP + VN + FP + FN)

def calcular_sensibilidade(VP, FN):
    return VP / (VP + FN)

def calcular_especificidade(VN, FP):
    return VN / (VN + FP)

def calcular_precisao(VP, FP):
    return VP / (VP + FP)

def calcular_f_score(precisao, sensibilidade):
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Calcular cada métrica
acuracia = calcular_acuracia(VP, VN, FP, FN)
sensibilidade = calcular_sensibilidade(VP, FN)
especificidade = calcular_especificidade(VN, FP)
precisao = calcular_precisao(VP, FP)
f_score = calcular_f_score(precisao, sensibilidade)

# Exibir os resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Sensibilidade: {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F-Score: {f_score:.2f}")
