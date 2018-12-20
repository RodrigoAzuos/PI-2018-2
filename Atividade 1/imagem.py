import os 
import requests

imagem = open("/home/rodrigo/Área de Trabalho/imagem.jpg", "wb")
r = requests.get(input())

print(r.headers)

imagem.write(r.content)
imagem.close()
