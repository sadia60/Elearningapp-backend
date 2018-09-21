from django import forms

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterationForm(forms.Form):
    Fullname = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = Post
    #     fields = ('title', 'text',)