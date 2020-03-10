from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Contact, Customer


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address', 'position', 'sex', 'sbu', 'status']

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwags)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('position', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sex', css_class='form-group col-md-4 mb-0'),
                Column('sbu', css_class='form-group col-md-4 mb-0'),
                Column('status', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'ADD CONTACT')
        )


class CustomerForm(forms.Form):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'position', 'sex', 'sbu', 'company']

    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwags)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('position', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sex', css_class='form-group col-md-4 mb-0'),
                Column('sbu', css_class='form-group col-md-4 mb-0'),
                Column('company', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'ADD CONTACT')
        )
