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

# Closure para armazenar e recuperar notas de um aluno específico
def criar_closure_notas(notas_iniciais):
    notas = notas_iniciais.copy()  # Armazena as notas do aluno

    def adicionar_nota(nova_nota):
        nonlocal notas  # Permite modificar a variável `notas` do escopo externo
        notas.append(nova_nota)

    def obter_notas():
        return notas

    # Retorna um dicionário com as funções do closure
    return {
        'adicionar_nota': adicionar_nota,
        'obter_notas': obter_notas
    }

# Exemplo de uso do closure
aluno_brenda = criar_closure_notas(aluno_1[0].get('notas'))

# Adicionando uma nova nota
aluno_brenda['adicionar_nota'](7)

# Recuperando as notas
notas_brenda = aluno_brenda['obter_notas']()

# Verificando se as notas foram adicionadas corretamente
notas_esperadas = [8, 5, 9, 7]
print("Terceiro teste OK") if notas_brenda == notas_esperadas else print("Terceiro teste Falhou")

# Função de alta ordem que aplica uma operação para todos os alunos
def aplicar_funcao_a_todos(alunos, funcao):
    return [funcao(aluno['notas']) for aluno in alunos]

# Aplicar a função calcular_media a todos os alunos
medias = aplicar_funcao_a_todos(alunos, calcular_media)

# Verificar se as médias foram calculadas corretamente
medias_esperadas = [7.33, 6.0, 7.0]
print("Quarto teste OK") if medias == medias_esperadas else print("Quarto teste Falhou")