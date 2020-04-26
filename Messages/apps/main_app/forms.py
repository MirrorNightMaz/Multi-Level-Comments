from django import forms
from .models import Messages


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['content']
        error_messages = {
            'content': {'required': '留言不得为空！'},
        }