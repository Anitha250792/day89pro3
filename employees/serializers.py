from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Employee.objects.all(),
                message="Email must be unique."
            )
        ]
    )
    full_name_upper = serializers.SerializerMethodField(read_only=True)

    def get_full_name_upper(self, obj):
        return obj.full_name_upper()

    class Meta:
        model = Employee
        fields = [
            'id', 'name', 'role', 'department', 'email',
            'full_name_upper', 'created_at', 'updated_at'
        ]
