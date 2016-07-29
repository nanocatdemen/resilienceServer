from django import forms

from .models import Paper


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'doi', 'abstract']
    # Form widgets for text area
    def clean_doi(self):
        doi = self.cleaned_data.get('doi')
        if not '/' in doi:
            raise forms.ValidationError('Please use slash')
        return doi
