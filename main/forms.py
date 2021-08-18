from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=64, label="", widget=forms.TextInput(attrs={"placeholder": "Name"})
    )
    email = forms.EmailField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Email"})
    )
    subject = forms.CharField(
        max_length=128,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Subject"}),
    )
    message = forms.CharField(
        label="", widget=forms.Textarea(attrs={"placeholder": "Message"})
    )
