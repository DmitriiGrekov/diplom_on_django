from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='Имя')
    to = forms.EmailField(label='Ваша почта')
    comments = forms.CharField(required=False,
                               widget=forms.Textarea, label='Комментарий')
