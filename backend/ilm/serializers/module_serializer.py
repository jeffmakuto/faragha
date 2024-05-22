from rest_framework import serializers
from ilm.models import Module
from ilm.models import Course


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Module model.
    Includes a write-only field for the course_id to establish the relationship
    between Module and Course when creating or updating Module instances.
    """
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), 
        write_only=True,
        help_text="ID of the Course this Module belongs to."
    )

    class Meta:
        model = Module
        fields = '__all__'
