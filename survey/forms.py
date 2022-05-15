from django import forms
from .models import *

##custom login form
class LoginForm(forms.ModelForm):
    class Meta:
        pass

## form for SA to create/edit Survey
class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = (
            "name",    
        )
        labels = {
            'name': 'Name your survey',
        }
        help_texts = {
            'name': 'required',
        }
## form for SP to send survey response
class ResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = (
            "about_you",
            "salary",
            "gender",
        )
        labels = {
            'about_you': 'Tell us About Yourself',
            'salary': 'Salary',
            'gender': 'Gender'
        }
        help_texts = {
            'about_you': 'required',
            'salary': 'required',
            'gender': 'required',
        }