from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre/s", max_length=120)
    edad = forms.IntegerField(label="Edad")
    activo = forms.BooleanField(label="Activo", required=False)
    TIPO_IVA = (
        (1, "Cons. final"),
        (2, "Resp. inscripto"),
        (3, "Monotributo"),
        (4, "Exento")
    )
    tipo_iva = forms.ChoiceField(label="Tipo de Iva", choices=TIPO_IVA)
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento",
                                       #input_formats=["%d/%m/%Y"]
                                       widget=forms.DateInput(attrs={"type": "date"})
                                       )


class LocalidadForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=120)
    cp = forms.CharField(label="Cód Postal", max_length=10)
    provincia = forms.CharField(label="Provincia", max_length=120)