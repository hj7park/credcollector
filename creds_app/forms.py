from django.forms import ModelForm
from .models import URL,Cred


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ['url']