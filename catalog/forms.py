from django.forms import ModelForm
from .models import Category, Product
from django.core.exceptions import ValidationError
from django.forms.fields import BooleanField


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        name = self.cleaned_data.get('name')
        for banned_word in banned_words:
            if banned_word in name.lower():
                raise ValidationError(f'Слово "{banned_word}" недопустимо в имени товара')
        return name

    def clean_description(self):
        banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        description = self.cleaned_data.get('description')
        for banned_word in banned_words:
            if banned_word in description.lower():
                raise ValidationError(f'Слово "{banned_word}" недопустимо в описании товара')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError(f'Цена не должна быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Размер файла не должен превышать 5 МБ')
            if not image.name.lower().endswith('.jpg') or image.name.lower().endswith('.png'):
                raise ValidationError('Вы можете загрузить только .JPG и .PNG файлы')
