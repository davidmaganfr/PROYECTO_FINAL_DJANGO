from django.forms import ModelForm
from .models import Contact

class Contactform(ModelForm):
    class Meta:
        model= Contact
        exclude = ('date', )

