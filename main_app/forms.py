from django.forms import ModelForm
from .models import Dining

class DiningForm(ModelForm):
  class Meta:
    model = Dining
    fields = ['date', 'meal']