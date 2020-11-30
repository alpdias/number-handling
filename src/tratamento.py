'''
@Autor: Paulo https://github.com/alpdias
'''

# biblioteca de localidade por padrao
import locale 

def tratamento(numero=0):
    
    """
    -> Função para tratar o número de acordo com o padrão do local\
    \n:param numero: Número para ser formatado\
    \n:return: Número formatado\
    """
    
    locale.setlocale(locale.LC_MONETARY, "pt-BR") # definiçoes
    
    return locale.currency(numero, grouping=True) # mostra a variavel formatada no padrao escolhido

    """
    parametros do metodo:
    
    locale.LC_MONETARY -> catergoria a ser utilizada (no caso valores monetarios)
    
    "pt-BR" -> formato do local a ser utilizado (em sistemas UNIX pode ser achado o locale com o comando "locale -a")
    
    grouping=True -> agrupar o valor por casas decimais
    """

    
print('')

x = 1000
y = 2000.56
z = x + y

print(f'{tratamento(z)}') # Resultado formatado no padrão 'pt-BR'

print('')
