from django.shortcuts import render

def index(request):
    return render(request, 'calc_app/index.html')

def calcular_emissoes(request):
    if request.method == 'POST':
        # Obtendo os dados do formulário
        km_por_dia = float(request.POST.get('carro', 0))  # km por dia
        frequencia = int(request.POST.get('frequencia', 0))  # vezes por semana
        combustivel = request.POST.get('combustivel')  # tipo de combustível

        # Fatores de emissão em kg de CO2 por km
        fatores_emissao = {
            'gasolina': 2.31,
            'etanol': 1.93,
            'diesel': 2.68,
            'eletrico': 0.00,
        }

        if combustivel in fatores_emissao:
            # Calculando as emissões de CO2
            emissao_diaria = km_por_dia * fatores_emissao[combustivel]
            emissao_semanal = emissao_diaria * frequencia
            emissao_mensal = emissao_semanal * 4  # considerando 4 semanas em um mês

            resultado = {
                'emissao_diaria': emissao_diaria,
                'emissao_semanal': emissao_semanal,
                'emissao_mensal': emissao_mensal,
            }
        else:
            resultado = None  # Para caso de combustível inválido

        return render(request, 'calc_app/index.html', {'resultado': resultado})

    return render(request, 'calc_app/index.html')  # Para GET
