
# 🔴 Código ineficiente (sem estrutura adequada)


# Busca ineficiente em uma lista não ordenada (O(n))
lista = [10, 23, 45, 70, 11, 15, 9]

def busca_ineficiente(valor):
    for item in lista:
        if item == valor:
            return True
    return False

print(busca_ineficiente(70))  # Demora mais à medida que a lista cresce



# ✅ Código otimizado usando dicionário (estrutura adequada)


# Busca eficiente usando um dicionário (O(1))
dados = {10: True, 23: True, 45: True, 70: True, 11: True, 15: True, 9: True}

def busca_eficiente(valor):
    return valor in dados

print(busca_eficiente(70))  # Muito mais rápido