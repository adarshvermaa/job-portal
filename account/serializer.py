from .models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken

# register serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','phone_no','email','password','employee','client']
        extra_kwargs = {
            'password' :{'write_only':True}  #  to does not return password in api ## postman
        }
    # convert password to hash key
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if len(password) <6:
            raise serializers.ValidationError("entre strong password")
        instance.save()
        return instance
# login serializers
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()
    client = serializers.BooleanField(read_only=True)
    employee = serializers.BooleanField(read_only=True)

   
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        tokens_data = {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    # Include 'client' and 'employee' only if they are True
        if user.client:
            tokens_data['fitness'] = user.client
        if user.employee:
            tokens_data['employee'] = user.employee

        return tokens_data

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens', 'client', 'employee']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        if not user.is_verified:
                raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'tokens': user.tokens,
         
        }

        return super().validate(attrs)


# email verification
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


# logout apis
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        RefreshToken(self.token).blacklist()



# password reset api
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class DashboardAccessSerializer(serializers.ModelSerializer):
    pass