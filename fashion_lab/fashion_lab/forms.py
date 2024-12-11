from django import forms
from .models import Usuario, Partes_de_Cima, Partes_de_Baixo, Calçados, Acessórios

class CadastroUsuarioForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome',
        max_length=100
    )
    genero = forms.ChoiceField(
        label='Gênero',
        choices=Usuario._meta.get_field('genero').choices,
        widget=forms.Select(attrs={'class': 'genero-select'})
    )
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        widget=forms.TextInput(attrs={'placeholder': 'ddd.ddd.ddd-dd'})
    )
    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    usuario = forms.CharField(
        label='Usuário',
        max_length=50
    )
    email = forms.EmailField(
        label='Email',
        max_length=100
    )
    senha = forms.CharField(
        label='Senha',
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': '************'})
    )
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': '************'})
    )

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError("As senhas não coincidem!")

        return cleaned_data

    class Meta:
        model = Usuario
        fields = ['nome', 'genero', 'cpf', 'data_nascimento', 'usuario', 'email', 'senha', 'confirmar_senha']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['senha'])
        if commit:
            user.save()
        return user

class PartesDeCimaForm(forms.ModelForm):
    imagem = forms.ImageField(
        label='Imagem',
    )
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
        fields = ['imagem','descricao', 'cor', 'marca', 'material', 'tamanho']
    
    def save(self, commit=True):
        return super().save(commit=commit)


class PartesDeBaixoForm(forms.ModelForm):
    imagem = forms.ImageField(
        label='Imagem',
    )
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
        fields = ['imagem','descricao', 'cor', 'marca', 'material', 'tamanho', 'comprimento']

    def save(self, commit=True):
        return super().save(commit=commit)

class CalcadosForm(forms.ModelForm):
    imagem = forms.ImageField(
        label='Imagem',
    )
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
        fields = ['imagem','descricao', 'cor', 'marca', 'material', 'tamanho', 'tipo']

    def save(self, commit=True):
        return super().save(commit=commit)

class AcessoriosForm(forms.ModelForm):
    imagem = forms.ImageField(
        label='Imagem',
    )
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
        fields = ['imagem','descricao', 'cor', 'marca', 'material', 'tipo', 'tamanho', 'material_acessorio']

    def save(self, commit=True):
        return super().save(commit=commit)