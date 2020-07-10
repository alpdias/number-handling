'''
@Autor: Paulo https://github.com/alpdias
'''

# Utilizando o método 'locale' para tratar números de acordo com padrão do local
def tratamento(numero=0):
    """
    -> Função para tratar o número separando por milhares no padrão do local
    :param numero: Número para ser formatado
    :return: Número formatado
    """
    import locale # Biblioteca de localidade por padrão
    locale.setlocale(locale.LC_MONETARY, "pt-BR") # Definições
    return locale.currency(numero, grouping=True) # Mostra a variável formatada no padrão escolhido
    '''
    Parâmetros do metodo:
    locale.LC_MONETARY -> Recebe a catergoria a ser utilizada (no caso valores monetários)
    "pt-BR" -> Recebe o formato do local a ser utilizado (em sistemas UNIX pode ser achado o locale com o comando "locale -a")
    grouping=True -> Agrupar o valor por casas decimais
    '''

    
print('')
x = 1000
y = 2000.56
z = x + y
print(f'{tratamento(z)}') # Resultado formatado no padrão 'pt-BR'
print('')
