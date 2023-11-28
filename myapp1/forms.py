from django import forms
class CreateContactForm(forms.Form):
 formID = forms.IntegerField(label='ID')
 name = forms.CharField(label='Name')
 gender = forms.CharField(label='Gender')
 address = forms.CharField(label='Address')
 profession = forms.CharField(label='Profession')
 telephone = forms.IntegerField(label='Telephone')
 email = forms.CharField(label='Email')
 birthday = forms.DateTimeField(label='Birthday')