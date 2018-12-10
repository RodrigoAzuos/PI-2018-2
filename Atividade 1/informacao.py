import requests

r = requests.get('http://google.com')

print("status code: %d" %r.status_code)
print("Cavbeçalho: \n	 %s " %r.headers)
print("Tamanho do conteudo: %s" %r.headers['Content-Length'])