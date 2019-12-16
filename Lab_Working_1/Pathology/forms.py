from django import forms
from Pathology.models import *
from Pathology.choices import *


class Patient_Details_Form(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    phone = forms.RegexField(regex=r'^\+?1?\d{9,10}$')

    class Meta:
        model = Patient_Details
        fields = ['Name', 'Age', 'Gender', 'phone', 'time']


class Image_Input_Forms(forms.ModelForm):
    class Meta:
        model = Image_Input
        fields = ['Image_Upload']


class Reports_Form(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['location', 'patient_details', 'test', 'image_output']


class Location_Form(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location']


# class Blood_Test_Form(forms.ModelForm):
#   class Meta:
#      model = Blood_Test
#     fields = ['blood_test']


# class Urine_Test_Form(forms.ModelForm):
#   class Meta:
#      model = Urine_Test
#     fields = ['urine_test']


class Test_Form(forms.ModelForm):
    class Meta:
        model = Test_Pathology
        fields = ['some_test']


class Test_Pathology_Form(forms.ModelForm):
    # blood = forms.ModelMultipleChoiceField(queryset = Blood_Test.objects.all(), widget=forms.CheckboxSelectMultiple)
    # urine = forms.ModelMultipleChoiceField(queryset = Urine_Test.objects.all(), widget=forms.CheckboxSelectMultiple)
    test1 = forms.ModelMultipleChoiceField(queryset=Test_Pathology.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Test_Pathology
        fields = ['test1']

# class Name_Form(forms.ModelForm):
#     class Meta:
#         model = Name
#         fields = ['some_text']
