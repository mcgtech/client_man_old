from django import forms
from .models import Client, Note
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import TabHolder, Tab

class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper

class ClientForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    helper.layout = Layout(
        TabHolder(
            Tab(
                'Basic Information',
                'title',
                'first_name',
                'middle_name',
                'last_name',
                'known_as'
            ),
            Tab(
                'Contact',
                'dob',
                'sex'
            )
        )
    )
    #helper.form_method = 'POST'
    #helper.add_input(Submit('login', 'login', css_class='btn-primary'))
    class Meta:
        model = Client
        fields = ('title', 'first_name', 'middle_name', 'last_name', 'known_as', 'dob', 'sex')
        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),}

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note', 'created_date', )

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()
