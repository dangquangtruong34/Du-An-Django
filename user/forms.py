from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm password'
    )
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
            'avatar',
            'first_name',
            'last_name',
            'country',
        ]
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError(
                'Username đã tồn tại.'
            )

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Email đã tồn tại.')
        return email
    
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 1024 * 1024:
                raise ValidationError('Ảnh phải nhỏ hơn hoặc bằng 1MB.')

            allowed_extensions = ('.jpg','.jpeg','.png')
            if not avatar.name.lower().endswith(allowed_extensions):
                raise ValidationError('Ảnh phải có định dạng JPG, JPEG hoặc PNG.')
            
        return avatar
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError(
                    'Mật khẩu xác nhận không khớp.'
                )

        return cleaned_data