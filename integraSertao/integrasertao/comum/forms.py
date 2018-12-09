from comum.models import Post
from django.forms import ModelForm,Textarea, DateInput, TextInput

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'resumo', 'palavras_chave','coautor','area_tematica', 'tipo', 'arquivo', 'foto')
        widgets = {
            'resumo': Textarea(attrs={'cols': 80, 'rows': 10}),
            'palavras_chave': TextInput(attrs={'cols': 60, 'rows': 1}),
        }


    def clean(self):

        cleaned_data = super().clean()
        resumo = cleaned_data.get("resumo")
        palavras_chave = cleaned_data.get("palavras_chave")

        palavras_chave_split = palavras_chave.split(';')
        resumo_split = resumo.split(' ')

        if resumo and palavras_chave:
            if len(palavras_chave_split) > 5 or len(palavras_chave_split) < 3:
                msg = "O número de palavras chave deve ser maior que 3 e menor que 5!"
                self.add_error('palavras_chave', msg)

            if len(resumo_split) > 450:
                msg = "A Quantidade de palavras ns resumo deve ser igual ou inferior a 450 palavras"
                self.add_error('resumo', msg)


