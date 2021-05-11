from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("entro token")
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['rol'] = user.rol
        token['username'] = user.username
        token['email'] = user.email
        
        return token