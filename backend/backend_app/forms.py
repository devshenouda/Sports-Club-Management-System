from django import forms
from .models import *
class TeamForm (forms.ModelForm):
    class Meta:
        model = Team 
        fields = '__all__'

        widgets = {
            'players_no' : forms.NumberInput(attrs={'class':'form-control'}) , 
            'status' : forms.Select(attrs={'class':'form-control'}) , 
            'type' : forms.Select(attrs={'class':'form-control'}) , 
            'team_photo' : forms.FileInput(attrs={'class':'form-control'}) , 
            'captain' : forms.TextInput(attrs={'class':'form-control'}) , 
            'team_name' : forms.TextInput(attrs={'class':'form-control'}) , 
        }


class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['revenue_type', 'amount', 'date', 'description', 'member', 'product_name', 'quantity']
        widgets = {
            'revenue_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'member': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'phone_number', 'team', 'is_active', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'phone_number', 'team', 'is_active', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }



class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['revenue_type', 'date',  'amount',  'quantity' ,  'total_revenue' , 'member', 'product_name' ,'description']
        widgets = {
            'revenue_type': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'member': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control' , 'id':'revenueamount'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control' , 'id':'revenuequantity'}),
            'total_revenue': forms.NumberInput(attrs={'class': 'form-control' , 'id':'revenuetotal'}),
        }



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_type', 'amount', 'date', 'description']
        widgets = {
            'expense_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        