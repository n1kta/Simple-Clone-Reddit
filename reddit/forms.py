from django.forms import ModelForm
from django.forms import Textarea

from .models import ArticlesModel, LinkModel, CommentsModel


class ArticlesForm(ModelForm):
    class Meta:
        model = ArticlesModel
        fields = ['title', 'description', 'group']


class LinkForm(ModelForm):
    class Meta:
        model = LinkModel
        fields = ['subbeddit']


class CommentsForm(ModelForm):
    class Meta:
        model = CommentsModel
        widgets = {
            'text': Textarea(attrs={'class': "form-control", 'id': "exampleFormControlTextarea1", 'rows': "3", 'placeholder': "Comments here..."}),
        }
        fields = ['text']