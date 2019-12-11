'''
@Autor: Paulo https://github.com/alpdias
'''
# Função para separa milhares de acordo com padrão do local.
def milhares(numero=0):
    """
    -> Função para tratar o número separando por milhares no padrão do local.
    :param numero: Número para ser formatado.
    :return: Número formatado.
    """
    import locale # Biblioteca de localidade de padrões.
    locale.setlocale(locale.LC_ALL, "pt-BR") # Defini o padrão a ser utilizado.
    return (locale.format_string("%.2f", numero, grouping=True, monetary=True)) # Mostra a variável formatada no padrão escolhido.

x = 1000
y = 2000.56
z = x + y
print(f'{milhares(z)}')
