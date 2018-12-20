from django.db import models

# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=255, null= False, blank= False )
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def total_votos(self):
        choices = self.choices.all()
        soma = 0

        for choice in choices:
            print(choice.votes)
            soma = sum(choice.votes)

        return soma


class Choice(models.Model):

    choice_text = models.CharField(max_length=255, null=False, blank= False)
    votes = models.IntegerField(default=0, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE ,null=True, blank= False, related_name="choices")

    def __str__(self):
        return self.choice_text

    def votar(self):

        self.votes += 1
        self.save()



