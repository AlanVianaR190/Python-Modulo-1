#cores no PYTHON
texto_vermelho = "\033[91mTexto em vermelho!\033[0m"
print(texto_vermelho)

texto_verde = "\033[92mTexto em verde!\033[0m"
print(texto_verde)

texto_amarelo = "\033[93mTexto em amarelo!\033[0m"
print(texto_amarelo)


#textos em vermelho, verde & amarelo
text_red = lambda text:f"\033[91m{text}\033[0m"

text_gre = lambda text:f"\033[92m{text}\033[0m"

text_yel = lambda text:f"\033[93m{text}\033[0m"
