from django import forms
from privatebeta.models import InviteRequest
from uni_form.helper import FormHelper
from uni_form.layout import *

class InviteRequestForm(forms.ModelForm):


	class Meta:
		model = InviteRequest
		fields = ['first_name', 'last_name', 'email']

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'id-inviteRequest'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'privatebeta_invite'

		self.helper.layout = Layout(
			Div('first_name', 'last_name', css='ctrlHolder'),
			Div('email'),
			ButtonHolder(
				Submit('submit', 'Submit', css_class='small black button radius')
				#Submit('submit', 'Submit', css_class='primaryAction')
			)
		)


		return super(InviteRequestForm, self).__init__(*args, **kwargs)