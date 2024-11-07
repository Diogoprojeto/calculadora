document.getElementById('carbono-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Coleta os dados do formulário
    const kmPorDia = parseFloat(event.target.carro.value);
    const frequencia = parseInt(event.target.frequencia.value);
    const combustivel = event.target.combustivel.value;

    // Fatores de emissão em kg de CO2 por km
    const fatoresEmissao = {
        gasolina: 2.31, // kg CO2 por km
        etanol: 1.93,   // kg CO2 por km
        diesel: 2.68,   // kg CO2 por km
        eletrico: 0.00  // kg CO2 por km
    };

    // Calcula as emissões de CO2
    const emissaoDiaria = kmPorDia * fatoresEmissao[combustivel];
    const emissaoSemanal = emissaoDiaria * frequencia;
    const emissaoMensal = emissaoSemanal * 4; // Aproximando para 4 semanas

    // Mostra o resultado
    const resultadoElement = document.getElementById('resultado');
    const emissaoTexto = `Emissões diárias: ${emissaoDiaria.toFixed(2)} kg CO2<br>
                          Emissões semanais: ${emissaoSemanal.toFixed(2)} kg CO2<br>
                          Emissões mensais: ${emissaoMensal.toFixed(2)} kg CO2`;
    
    document.getElementById('emissoes').innerHTML = emissaoTexto;
    resultadoElement.style.display = 'block';
});
