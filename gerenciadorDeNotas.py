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

# Função com list comprehension para filtrar alunos que tiveram média maior que 6
def filtrar_aprovados(alunos):
    # Filtra alunos com média maior ou igual a 7, calculando a média com a função lambda
    return [aluno for aluno in alunos if calcular_media(aluno['notas']) >= 7]

alunos = [
    {'nome': 'Brenda', 'notas': [8, 5, 9]},
    {'nome': 'Wescley', 'notas': [6, 7, 5]},
    {'nome': 'Kayque', 'notas': [7, 7, 7]}
]

aprovados = filtrar_aprovados(alunos)
alunosEsperados = [{'nome': 'Brenda', 'notas': [8, 5, 9]}, {'nome': 'Kayque', 'notas': [7, 7, 7]}]
print("Segundo teste OK") if aprovados == alunosEsperados else print("Segundo teste Falhou")
#Fim do teste