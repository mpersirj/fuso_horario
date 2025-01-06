#Importação dos módulos e bibliotecas
from datetime import datetime
import pytz

# Dicionário com as cidades e seus fusos horários
cidades = {
    "Nova Iorque/USA": "America/New_York",
    "Rio de Janeiro/BRA": "America/Sao_Paulo",
    "Londres/ING": "Europe/London",
    "Paris/FRA": "Europe/Paris",
    "Dubai/EAU": "Asia/Dubai",
    "Tóquio/JPA": "Asia/Tokyo",
    "Sidney/AUS": "Australia/Sydney",
}

#Função para obter horário atual
def obter_hora_atual(cidade, timezone):
    fuso_horario = pytz.timezone(timezone)
    hora_local = datetime.now(fuso_horario)
    return hora_local

# Exibir a hora atual em cada cidade
print("Hora atual nas cidades:")
print("="*40)
for cidade, fuso in cidades.items():
    hora = obter_hora_atual(cidade, fuso)
    print(f"{cidade}: {hora.strftime('%Y-%m-%d %H:%M:%S')}")

# Função para calcular diferença entre duas cidades
def calcular_diferenca_horarios(cidade1, cidade2):
    fuso1 = pytz.timezone(cidades[cidade1])
    fuso2 = pytz.timezone(cidades[cidade2])
    
    agora = datetime.now()
    hora1 = fuso1.localize(agora)
    hora2 = fuso2.localize(agora)
    
    diferenca = (hora1 - hora2).total_seconds() / 3600  # Converter para horas
    return abs(diferenca)

# Exemplo: Diferença entre Nova Iorque e Rio de Janeiro
cidade1 = "Nova Iorque/USA"
cidade2 = "Rio de Janeiro/BRA"
diferenca = calcular_diferenca_horarios(cidade1, cidade2)
print("\nDiferença de horário:")
print(f"A diferença entre {cidade1} e {cidade2} é de {diferenca:.2f} horas.")
