import locale # Biblioteca de localidade de padrões.
locale.setlocale(locale.LC_ALL, "pt-BR") # Defini o padrão a ser utilizado.
numero = 89000000 # Variável com um número.
print(locale.format_string("%.2f", numero, grouping=True, monetary=True)) # Mostra a variável formatada no padrão escolhido.
