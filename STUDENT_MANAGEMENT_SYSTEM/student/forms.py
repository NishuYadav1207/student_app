from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            'name',
            'date_of_birth',
            'age',
            'address',
            'roll_no',
            'fees_amount',
            'parents_name',
            'phone_no',
            'email_id',
            'gender',
            'course',
            'semester',
            'image',
            'marks',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter student name'
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter age'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter complete address',
                    'rows': 4
                }
            ),

            'roll_no': forms.TextInput(
                attrs={
                    'placeholder': 'Enter roll number'
                }
            ),

            'fees_amount': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter fees amount',
                    'step': '0.01'
                }
            ),

            'parents_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter parents name'
                }
            ),

            'phone_no': forms.TextInput(
                attrs={
                    'placeholder': 'Enter phone number'
                }
            ),

            'email_id': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email address'
                }
            ),

            'course': forms.TextInput(
                attrs={
                    'placeholder': 'Enter course'
                }
            ),

            'marks': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter marks',
                    'step': '0.01'
                }
            ),
        }