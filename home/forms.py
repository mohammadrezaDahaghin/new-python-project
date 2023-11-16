from django import forms

class TodoCreateForm(forms.Form):
    title=forms.CharField(label='عنوان',required=False)
    body=forms.CharField(label='توضیحات')
    created=forms.DateTimeField()