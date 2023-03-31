# forms.py
from django import forms
from .models import Professor,Rating

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name']
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'user_id': forms.HiddenInput()
        }
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['user_id'] = self.instance.user_id  # set user_id field to current user's ID
        cleaned_data.pop('user_id', None)  # remove 'user_id' key from cleaned_data
        return cleaned_data