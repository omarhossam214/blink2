from django import forms
from login.models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['city', 'address', 'call', 'note']
        labels = {
            'city': 'City',
            'address': 'Address',
            'call': 'Call upon arrival',
            'note': 'Delivery notes (optional)'
        }
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3})
        }