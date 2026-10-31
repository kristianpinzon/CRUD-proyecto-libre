from django import forms
from .models import ArmaDarkSouls, CategoriaArma, VideoDestacado

class ArmaDarkSoulsForm(forms.ModelForm):
    class Meta:
        model = ArmaDarkSouls
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'durabilidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'req_fuerza': forms.NumberInput(attrs={'class': 'form-control'}),
            'req_destreza': forms.NumberInput(attrs={'class': 'form-control'}),
            'req_inteligencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'req_fe': forms.NumberInput(attrs={'class': 'form-control'}),
            'escalado_fuerza': forms.Select(attrs={'class': 'form-control'}),
            'escalado_destreza': forms.Select(attrs={'class': 'form-control'}),
            'escalado_inteligencia': forms.Select(attrs={'class': 'form-control'}),
            'escalado_fe': forms.Select(attrs={'class': 'form-control'}),
            'daño_fisico': forms.NumberInput(attrs={'class': 'form-control'}),
            'daño_magico': forms.NumberInput(attrs={'class': 'form-control'}),
            'daño_fuego': forms.NumberInput(attrs={'class': 'form-control'}),
            'daño_rayo': forms.NumberInput(attrs={'class': 'form-control'}),
            'daño_oscuro': forms.NumberInput(attrs={'class': 'form-control'}),
            'habilidad_especial': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_almas': forms.NumberInput(attrs={'class': 'form-control'}),
            'efecto_pasivo': forms.TextInput(attrs={'class': 'form-control'}),
            'es_arma_de_jefe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }