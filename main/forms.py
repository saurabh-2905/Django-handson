from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserData(forms.Form):
	Number = forms.IntegerField(required=True)

	class Meta:
		model = User
		fields = ("Number")

	def save(self, commit=True):
		user = super(UserData, self).save(commit=False)
		user.Number = self.cleaned_data["Number"]
		if commit:
			user.save()
		return user