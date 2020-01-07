from django import forms

class FeedItemForm(forms.Form):
    description = forms.CharField()
    