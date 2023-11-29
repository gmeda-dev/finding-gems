from django import forms


class DifficultyForm(forms.Form):
    EASY = 50
    MEDIUM = 75
    HARD = 100
    CHOICES = (
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (HARD, "Hard"),
    )
    difficulty = forms.ChoiceField(choices=CHOICES)


class FindGemForm(forms.Form):
    latitude = forms.CharField(widget=forms.NumberInput(attrs={"step": 0.1}))
    longitude = forms.CharField(widget=forms.NumberInput(attrs={"step": 0.1}))

    def clean(self):
        cleaned_data = super().clean()
        errors = dict()
        if not (37 <= float(cleaned_data["latitude"]) <= 38):
            errors.update({"latitude": "Value must be between 37 and 38."})

        if not (-123 <= float(cleaned_data["longitude"]) <= -121):
            errors.update({"longitude": "Value must be between -123 and -121."})

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
