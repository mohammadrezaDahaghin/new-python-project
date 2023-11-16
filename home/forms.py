from django import forms
from .models import Todo
class TodoCreateForm(forms.Form):
    title=forms.CharField(label='عنوان',required=False)
    body=forms.CharField(label='توضیحات')
    created=forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields=('title','body','created')