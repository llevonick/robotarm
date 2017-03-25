from django.forms import ModelForm
from .models import Position

class PositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Position
        fields = ['pos_1', 'pos_2', 'pos_3', 'pos_4', 'pos_5']
