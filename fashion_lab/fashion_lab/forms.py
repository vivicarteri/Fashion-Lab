from django import forms
from .models import Partes_de_Cima, Partes_de_Baixo, Calçados, Acessórios

class PartesDeCimaForm(forms.ModelForm):
    descricao = forms.CharField(
        label='Descrição',
        max_length=100
    )
    cor = forms.CharField(
        label='Cor',
        max_length=10
    )
    marca = forms.CharField(
        label='Marca',
        max_length=100
    )
    material = forms.CharField(
        label='Material',
        max_length=100
    )
    tamanho = forms.ChoiceField(
        label='Tamanho',
        choices=Partes_de_Cima._meta.get_field('tamanho').choices
    )

    class Meta:
        model = Partes_de_Cima
        fields = ['descricao', 'cor', 'marca', 'material', 'tamanho']

class PartesDeBaixoForm(forms.ModelForm):
    descricao = forms.CharField(
        label='Descrição',
        max_length=100
    )
    cor = forms.CharField(
        label='Cor',
        max_length=100
    )
    marca = forms.CharField(
        label='Marca',
        max_length=100
    )
    material = forms.CharField(
        label='Material',
        max_length=100
    )
    tamanho = forms.ChoiceField(
        label='Tamanho',
        choices=Partes_de_Baixo._meta.get_field('tamanho').choices
    )
    comprimento = forms.ChoiceField(
        label='Comprimento',
        choices=Partes_de_Baixo._meta.get_field('comprimento').choices
    )

    class Meta:
        model = Partes_de_Baixo
        fields = ['descricao', 'cor', 'marca', 'material', 'tamanho', 'comprimento']

class CalcadosForm(forms.ModelForm):
    descricao = forms.CharField(
        label='Descrição',
        max_length=100
    )
    cor = forms.CharField(
        label='Cor',
        max_length=100
    )
    marca = forms.CharField(
        label='Marca',
        max_length=100
    )
    material = forms.ChoiceField(
        label='Material',
        choices=Calçados._meta.get_field('material').choices,
        required=False
    )
    tamanho = forms.ChoiceField(
        label='Tamanho',
        choices=Calçados._meta.get_field('tamanho').choices
    )
    tipo = forms.ChoiceField(
        label='Tipo',
        choices=Calçados._meta.get_field('tipo').choices
    )

    class Meta:
        model = Calçados
        fields = ['descricao', 'cor', 'marca', 'material', 'tamanho', 'tipo']

class AcessoriosForm(forms.ModelForm):
    descricao = forms.CharField(
        label='Descrição',
        max_length=100
    )
    cor = forms.CharField(
        label='Cor',
        max_length=100
    )
    marca = forms.CharField(
        label='Marca',
        max_length=100
    )
    material = forms.CharField(
        label='Material',
        max_length=100
    )
    tipo = forms.ChoiceField(
        label='Tipo',
        choices=Acessórios._meta.get_field('tipo').choices
    )
    tamanho = forms.ChoiceField(
        label='Tamanho',
        choices=Acessórios._meta.get_field('tamanho').choices,
        required=False
    )
    material_acessorio = forms.ChoiceField(
        label='Material do Acessório',
        choices=Acessórios._meta.get_field('material_acessorio').choices
    )

    class Meta:
        model = Acessórios
        fields = ['descricao', 'cor', 'marca', 'material', 'tipo', 'tamanho', 'material_acessorio']