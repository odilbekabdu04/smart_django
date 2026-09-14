from rest_framework import serializers
from .models import User, rest


# ============================================
# USER SERIALIZER
# ============================================
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'fullname', 'password',
            'is_blocked', 'is_staff', 'is_superuser', 'role', 'date_joined'
        ]
        read_only_fields = ['id', 'date_joined', 'is_staff', 'is_superuser', 'role']

    def get_role(self, obj):
        return 'admin' if obj.is_superuser else 'customer'

    def validate_email(self, value):
        qs = User.objects.filter(email=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Bu email allaqachon band!")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password:
            raise serializers.ValidationError({"password": "Parol majburiy!"})

        username = validated_data.pop('username', None)
        if not username:
            username = validated_data['email'].split('@')[0]

        base = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base}{counter}"
            counter += 1

        user = User.objects.create_user(
            username=username,
            password=password,
            is_staff=False,
            is_superuser=False,
            **validated_data
        )
        return user


# ============================================
# REGISTER SERIALIZER
# ============================================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Parollar mos kelmadi!"})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Bu email band!"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        email = validated_data['email']
        username = email.split('@')[0]

        base = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base}{counter}"
            counter += 1

        return User.objects.create_user(
            username=username,
            password=password,
            is_staff=False,
            is_superuser=False,
            **validated_data
        )


# ============================================
# MAHSULOT SERIALIZER — TUZATILDI
# ============================================
class RestSerializer(serializers.ModelSerializer):
    """Mahsulot serializer — model maydonlariga mos"""
    
    image_url = serializers.SerializerMethodField()
    chegirma_foiz = serializers.ReadOnlyField()
    kategoriya_nomi = serializers.CharField(
        source='get_kategoriya_display',
        read_only=True
    )

    class Meta:
        model = rest
        fields = [
            'id',
            'nomi',
            'kategoriya',
            'kategoriya_nomi',
            'puli',           # ✅ puli (narx emas)
            'eski_narx',
            'chegirma_foiz',
            'yulduzi',        # ✅ yulduzi (reyting emas)
            'korishi',
            'oyiga',
            'qancha',
            'yetkazish_kun',
            'fermer_ismi',
            'fermer_manzil',
            'image',
            'image_url',
            'faol',
            'yaratilgan',
        ]
        read_only_fields = ['id', 'yaratilgan']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        elif obj.image:
            return obj.image.url
        return None