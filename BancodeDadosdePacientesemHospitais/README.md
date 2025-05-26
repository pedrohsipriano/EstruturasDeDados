# Sistema de Gerenciamento de Pacientes

## Contexto

Este projeto simula um sistema de gerenciamento de pacientes em um ambiente de emergência médica. Ele é capaz de:

- Cadastrar pacientes com prioridade médica.
- Ordenar os pacientes com base na urgência e no tempo de chegada.
- Atender pacientes de forma justa e baseada em regras médicas predefinidas.
- Buscar pacientes por prioridade e/ou data de admissão usando busca binária eficiente.

---

## Classes Presentes e Onde São Usadas

### `Paciente`

A única classe presente no código é a `Paciente`, que representa cada indivíduo na fila de atendimento. A classe encapsula os dados de cada paciente, sendo utilizada em toda a lógica do sistema.

```python
class Paciente:
    def __init__(self, id_paciente, nome_completo, prioridade_medica, data_admissao):
        self.id_paciente = id_paciente
        self.nome_completo = nome_completo
        self.prioridade_medica = prioridade_medica
        self.data_admissao = data_admissao

    def __str__(self):
        return f"{self.nome_completo} | Prioridade: {self.prioridade_medica} | Admissão: {self.data_admissao.strftime('%d/%m/%Y %H:%M')}"
````

Ela é utilizada para criar a lista de pacientes, ordenar, exibir e realizar a busca binária.

---

## Ordenação e Busca: Como e Por Que São Utilizadas

### Ordenação

A lista de pacientes é ordenada considerando dois critérios principais:

1. **Prioridade médica:** Quanto menor o número, maior a urgência.
2. **Data de admissão:** Em caso de empate na prioridade, quem chegou antes é atendido primeiro.

Exemplo de criação e ordenação da lista:

```python
pacientes = [
    Paciente("001", "Ana Souza", 2, datetime(2024, 5, 20, 9, 15)),
    Paciente("002", "Carlos Lima", 1, datetime(2024, 5, 20, 9, 10)),
    Paciente("003", "Beatriz Castro", 2, datetime(2024, 5, 20, 8, 55))
]

ordenar_pacientes(pacientes)
```

Após a ordenação, a lista será:

1. Carlos Lima (prioridade 1)
2. Beatriz Castro (prioridade 2, chegou antes)
3. Ana Souza (prioridade 2, chegou depois)

### Busca Binária

A busca é feita com base na prioridade (e opcionalmente na data). Como a lista já está ordenada, isso permite uma **busca binária eficiente**:

```python
pacientes_encontrados = buscar_pacientes_binaria(pacientes, prioridade=2)
```

Isso retornará todos os pacientes com prioridade 2.

---

## Explicação: Como o Insertion Sort Foi Utilizado e Adaptado

O algoritmo de ordenação utilizado é o **Insertion Sort**, adaptado para comparar dois critérios:

```python
def ordenar_pacientes(pacientes):
    for i in range(1, len(pacientes)):
        atual = pacientes[i]
        j = i - 1
        while j >= 0 and (
            (atual.prioridade_medica < pacientes[j].prioridade_medica) or
            (atual.prioridade_medica == pacientes[j].prioridade_medica and atual.data_admissao < pacientes[j].data_admissao)
        ):
            pacientes[j + 1] = pacientes[j]
            j -= 1
        pacientes[j + 1] = atual
```

### Exemplo de funcionamento:

Com os seguintes pacientes:

* João (prioridade 3, 9h)
* Maria (prioridade 1, 8h)
* Lucas (prioridade 1, 10h)

A ordenação correta será:

1. Maria
2. Lucas
3. João

Ou seja, respeita a prioridade **e** a hora de chegada em caso de empate.

---

## Por Que Foi Uma Boa Escolha Usar Insertion Sort

O uso do Insertion Sort foi estratégico pelas seguintes razões:

* ✅ **Simplicidade:** Fácil de implementar e de entender.
* ✅ **Estabilidade:** Pacientes com mesma prioridade e hora continuam na ordem original.
* ✅ **Personalizável:** Adaptável para múltiplos critérios de ordenação (prioridade e data).
* ✅ **Eficiente em listas pequenas:** Ideal para o contexto hospitalar com um número razoável de pacientes por dia.

---

## Execução

Ao rodar o script:

1. Os pacientes são cadastrados com dados fictícios.
2. A lista original é exibida.
3. A função `ordenar_pacientes` organiza os pacientes.
4. O sistema simula o atendimento dos pacientes com base na ordem.
5. Uma busca por prioridade específica é feita e os resultados são mostrados.

Exemplo de saída:

```
Lista de Pacientes:
Carlos Lima | Prioridade: 1 | Admissão: 20/05/2024 09:10
Beatriz Castro | Prioridade: 2 | Admissão: 20/05/2024 08:55
Ana Souza | Prioridade: 2 | Admissão: 20/05/2024 09:15

Paciente atendido: Carlos Lima
Paciente atendido: Beatriz Castro
Paciente atendido: Ana Souza

Busca por prioridade 2:
Beatriz Castro | Prioridade: 2 | Admissão: 20/05/2024 08:55
Ana Souza | Prioridade: 2 | Admissão: 20/05/2024 09:15
```

---

## Conclusão

Este sistema demonstra de forma clara e funcional como aplicar conceitos de estruturas de dados (insertion sort, busca binária) e orientação a objetos para resolver problemas do mundo real, como o gerenciamento de pacientes em um pronto-socorro.