from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

CustomerUser = get_user_model()

class CustomerUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomerUser
	list_display = ['email', 'username',]


admin.site.register(CustomerUser, CustomerUserAdmin)
