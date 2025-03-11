# Função lambda para calcular a média de um aluno
calcular_media = lambda notas: round(sum(notas) / len(notas),2)

# Caso de teste Função Lambda
aluno_1 = [{
        'nome': 'Brenda',
        'notas': [8,5,9]
    }]

resultado1 = calcular_media(aluno_1[0].get('notas'))
resultadoEsperado = 7.33
print("Primeiro teste OK") if resultado1 == resultadoEsperado else print("Primeiro teste Falhou")

#Fim do teste