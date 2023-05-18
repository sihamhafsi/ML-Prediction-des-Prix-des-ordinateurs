from django.forms import ModelForm


from .models import Algorithme


class PredictForm(ModelForm):
    class Meta:
        model = Algorithme
        fields = "__all__" 