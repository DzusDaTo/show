from .models import Resume
from django.forms import ModelForm, TextInput


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['last_name', 'first_name', 'number', 'city', 'date', 'gender', 'opat_rabot', 'special', 'o_sebe', 'obrazov', 'obraz_ucher', 'leanguage', 'komandirovka', 'zanyatost']
        widgets = {
            "last_name": TextInput(attrs={'class':'form-control', 'placeholder': 'Фамилия'}),
            "first_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            "number": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            "city": TextInput(attrs={'class': 'form-control', 'placeholder': 'Проживаете в городе/селе'}),
            "date": TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата рождения'}),
            "gender": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пол'}),
            "opat_rabot": TextInput(attrs={'class': 'form-control', 'placeholder': 'Опыт работы '}),
            "special": TextInput(attrs={'class': 'form-control', 'placeholder': 'Специальность'}),
            "o_sebe": TextInput(attrs={'class': 'form-control', 'placeholder': 'О себе'}),
            "obrazov": TextInput(attrs={'class': 'form-control', 'placeholder': 'Образование'}),
            "obraz_ucher": TextInput(attrs={'class': 'form-control', 'placeholder': 'Образовательное учереждение'}),
            "leanguage": TextInput(attrs={'class': 'form-control', 'placeholder': 'Язык'}),
            "komandirovka": TextInput(attrs={'class': 'form-control', 'placeholder': 'Готовность к командировкам'}),
            "zanyatost": TextInput(attrs={'class': 'form-control', 'placeholder': 'Занятость'}),
        }