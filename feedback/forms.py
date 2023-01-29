from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'First name:',
            'surname': 'Last name:',
            'feedback': 'Feedback:',

        }
        error_messages = {
            'name': {
                'min_length': 'Field Name is to short',
                'max_length': 'Field Name is to long',
                'required': 'Field Name is an empty',
            },
            'surname': {
                'min_length': 'Field Surname is to short',
                'max_length': 'Field Surname is to long',
                'required': 'Field Surname is an empty',
            },
            'feedback': {
                'min_length': 'Field Feedback is to short',
                'max_length': 'Field Feedback is to long',
                'required': 'Field Feedback is an empty',
            },

        }









