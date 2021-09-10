from django import forms

FORM_CHOICES =(
    ('Pedido','Pedido'),
    ('Reporte','Reportar película caída'),
)

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su email', 'class':'bg-dark text-light m-2'}))
    asunto = forms.ChoiceField(widget=forms.Select(attrs={'class': 'bg-dark text-light m-2'}),choices=FORM_CHOICES)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Detalle aquí su pedido o reporte', 'class':'bg-dark text-light m-2'}),max_length=250)

