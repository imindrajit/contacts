from django import forms
from contact_list.models import Contact

class ContactForm(forms.ModelForm):

	name = forms.CharField(min_length=3, max_length=20)
	phone_number = forms.CharField(min_length=10, max_length=13)
	class Meta:
		model = Contact



