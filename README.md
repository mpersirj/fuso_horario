# Horário Global em Python

Esse projeto foi desenvolvido após os estudos no curso da DIO sobre "Lidando com Data, Hora e Fuso Horário no Python". O objetivo desse código é obter a hora atual em várias cidades ao redor do mundo e calcular a diferença de horário entre duas cidades específicas.

## Funcionalidades

1. **Importação dos módulos e bibliotecas:**
   - O código utiliza as bibliotecas `datetime` e `pytz` para manipulação de data, hora e fuso horário.

2. **Dicionário com as cidades e seus fusos horários:**
   - Um dicionário (`cidades`) mapeia o nome das cidades aos seus respectivos fusos horários.

3. **Função para obter horário atual:**
   - A função `obter_hora_atual(cidade, timezone)` recebe uma cidade e seu fuso horário, e retorna a hora local dessa cidade.

4. **Exibir a hora atual em cada cidade:**
   - Um loop itera sobre o dicionário de cidades, utilizando a função `obter_hora_atual` para exibir a hora atual em cada cidade.

5. **Função para calcular a diferença entre duas cidades:**
   - A função `calcular_diferenca_horarios(cidade1, cidade2)` calcula a diferença de horário (em horas) entre duas cidades.

6. **Exemplo de uso:**
   - O código calcula e exibe a diferença de horário entre Nova Iorque (EUA) e Rio de Janeiro (Brasil).
