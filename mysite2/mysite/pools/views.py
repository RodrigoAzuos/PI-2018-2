from django.shortcuts import render
from pools.models import  Question

# Create your views here.

def index(requests):
    questoes = Question.objects.order_by("-pub_date")
    return render(requests, "index.html", {"questoes": questoes})

def get_question(requests, question_id):
    questao = Question.objects.get(pk=question_id)
    return render(requests, "question.html", {"questao":questao})

def results(requests, question_id):

    questao = Question.objects.get(pk=question_id)
    return render(requests, "results.html", {"questao": questao})

def vote(requests,question_id):

    questao = Question.objects.get(pk=question_id)

    if questao.closed:
        return render(requests, "results.html", {"questao": questao, "mensagem": "Questão fechada"})
    else:
        choices = questao.chices.all()

        for choice in choices:
            choice.votar()

    return render(requests, "results.html", {"questao": questao, "mensagem": "voto computado"})


def manage(requests,question_id):
    pass
