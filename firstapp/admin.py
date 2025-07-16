from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from .models import UserAccount

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'first_name', 'last_name', 'birthdate', 'type')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # hash the password
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'

    def clean_password(self):
        # return the initial value so it doesn't get cleared
        return self.initial["password"]


class UserAccountAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserAccount

    list_display = ('username', 'email', 'type', 'is_staff', 'is_admin')
    list_filter = ('is_staff', 'type')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name', 'birthdate')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'birthdate', 'type', 'password', 'is_staff', 'is_admin')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(UserAccount, UserAccountAdmin)
