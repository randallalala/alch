from django import forms
from .models import Cocktail

class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ['name']

    def clean(self):
        data = self.cleaned_data
        name = data.get("name")
        qs = Cocktail.objects.filter(name__icontains=name)
        if qs.exists():
            self.add_error("name", f"\"{name}\" is already in use. Please pick another name.")
        return data


class CocktailFormOld(forms.Form):
    name = forms.CharField()
    content = forms.CharField()

    # def clean_name(self):
    #     cleaned_data = self.cleaned_data # dictionary
    #     print("cleaned_data", cleaned_data)
    #     name = cleaned_data.get('name')
    #     if name.lower().strip() == "the office":
    #         raise forms.ValidationError('This name is taken.')
    #     print("name", name)
    #     return name

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        name = cleaned_data.get('name')
        content = cleaned_data.get("content")
        if name.lower().strip() == "the office":
            self.add_error('name', 'This name is taken.')
            # raise forms.ValidationError('This name is taken.')
        if "office" in content or "office" in name.lower():
            self.add_error('content', "Office cannot be in content")
            raise forms.ValidationError("Office is not allowed")
        return 