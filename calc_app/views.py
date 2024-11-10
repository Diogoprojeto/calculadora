from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Exibe a página inicial com o formulário."""
    return render(request, 'calc_app/index.html')

def calcular_emissoes(request):
    """Processa os dados do formulário e calcula as emissões de CO2."""
    if request.method == 'POST':
        # Obtém os valores enviados pelo formulário
        carro_km = float(request.POST.get('carro'))
        frequencia = int(request.POST.get('frequencia'))
        combustivel = request.POST.get('combustivel')

        # Definir fatores de emissão baseados no combustível
        if combustivel == 'gasolina':
            fator_emissao = 2.31  # kg CO2 por litro de gasolina
        elif combustivel == 'etanol':
            fator_emissao = 1.87  # kg CO2 por litro de etanol
        elif combustivel == 'diesel':
            fator_emissao = 2.68  # kg CO2 por litro de diesel
        elif combustivel == 'eletrico':
            fator_emissao = 0.0  # Carro elétrico não gera emissões diretas de CO2
        else:
            fator_emissao = 0
            return render(request, 'calc_app/index.html', {'erro': 'Combustível inválido ou não informado'})

        # Cálculos de emissões
        # Suponhamos que o carro consome 1 litro de combustível a cada 10 km
        consumo = carro_km / 10  # Litros de combustível consumidos por dia
        emissao_diaria = consumo * fator_emissao
        emissao_semanal = emissao_diaria * frequencia
        emissao_mensal = emissao_diaria * frequencia * 4  # Considerando 4 semanas por mês

        # Retorna o resultado para o template
        resultado = {
            'emissao_diaria': emissao_diaria,
            'emissao_semanal': emissao_semanal,
            'emissao_mensal': emissao_mensal,
        }

        return render(request, 'calc_app/index.html', {'resultado': resultado})

    return HttpResponse("Método HTTP não permitido", status=405)
