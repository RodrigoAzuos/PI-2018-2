from bs4 import BeautifulSoup
import requests
import re
import requests_cache

def obter_pagina(link,links):
    html = " "
    try:
        if permitido(link,links):
            response = requests.get(link)
            print("Baixando: %s" %link)
            links.append(link)
            html = BeautifulSoup(response.text, 'html5lib')
    except ConnectionResetError:
            print("Erro de conexão")
    except:
        print("Impossivel baixar")

    return html


def obter_links(html):   
    
    links = []
    try:
        for link in html.find_all('a'):
            try:
                if link["href"].find("http") != -1:
                     links.append(link.get("href"))
            except:
                continue
    except AttributeError:
        print("Pagina não possue links")

    return links

def permitido(link,links):
    if len(links) == 0 or link not in links:
        return True
    return False


def busca(chave, link, profundidade, lista_links):
    
    html = obter_pagina(link,lista_links)
    links = obter_links(html)        
    
    inicio = []
    fim = []
        
    try: 
        for m in re.finditer('(.{1,64})(%s)(.{1,64})' % chave.upper(), html.text.upper()):
            inicio.append(m.start())
            fim.append(m.end())
        
    except AttributeError as error:
        print(error)
    finally:
        pass

    if(len(inicio) > 0):
        print("Ocorrenciar encontradas: ")
        for i in range(len(inicio)):
             print("{0:^20}".format(html.text[inicio[i]:fim[i]]))
          
    if profundidade != 0:               
        for link in links:
            busca(chave,link,profundidade -1, lista_links)       


def main():
    requests_cache.install_cache('cache_sites')

    links = []
    try:
        busca(input("Digite a palavra a ser buscada: "), input("Digite o site "), int(input("Digite a profundidade da busca: ")), links)    
    except ValueError:
        print("Digite um número válido para profundidade")
    

    print("Quantidade de sites visitados: %s" % len(links))

if __name__ == '__main__':
    main()