from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import requests

# Create your views here.

def get_token(request):

    body = {'email': 'rodrigoesilvasouza@gmail.com',
            'password': 'Dani9698'}

    url = 'https://api.inthegra.strans.teresina.pi.gov.br/v1/signin'
    #
    headers = {"Content-Type": "application/json",
               "Accept-Language": "en",
               "Date": "Wed, 19 Dec 2018 19:46:12 GMT",
               "X-Api-Key": "73f9879b59504bdfb60e13aface78c08"}

    token = requests.post(url, json=body, headers=headers).json()['token']

    return token


def get_linhas(request):

    url = 'https://api.inthegra.strans.teresina.pi.gov.br/v1/linhas'
    token = get_token(request)



    headers = {"X-Auth-Token": token,
               "Accept-Language": "en",
               "Date": "Wed, 19 Dec 2018 19:46:12 GMT",
               "X-Api-Key": "73f9879b59504bdfb60e13aface78c08"}

    linhas = requests.get(url, headers=headers).json()

    paginator = Paginator(linhas, 15)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        linhas = paginator.page(page)
    except (EmptyPage, InvalidPage):
        linhas = paginator.page(paginator.num_pages)

    return render(request, "linhas.html", {'linhas': linhas})

def get_linha(request, linha):

    token = get_token(request)

    headers = {"X-Auth-Token": token,
               "Accept-Language": "en",
               "Date": "Wed, 19 Dec 2018 19:46:12 GMT",
               "X-Api-Key": "73f9879b59504bdfb60e13aface78c08"}

    url = 'https://api.inthegra.strans.teresina.pi.gov.br/v1/linhas?busca=%s'%linha
    linha_especifica = requests.get(url, headers=headers).json()
    paginator = Paginator(linha_especifica, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        linha_especifica = paginator.page(page)
    except (EmptyPage, InvalidPage):
        linha_especifica = paginator.page(paginator.num_pages)

    return  render(request, 'linhas.html', {'linhas':linha_especifica})

def get_veiculo(request, num_linha):

    token = get_token(request)

    headers = {"X-Auth-Token": token,
               "Accept-Language": "en",
               "Date": "Thu, 20 Dec 2018 13:21:28 GMT",
               "X-Api-Key": "73f9879b59504bdfb60e13aface78c08"}

    url = 'https://api.inthegra.strans.teresina.pi.gov.br/v1/veiculosLinha?busca=%s' % num_linha

    veiculo = requests.get(url, headers=headers)

    return render(request, 'linhas.html', {'linhas': veiculo})
