from rest_framework import serializers
from API.models import Employee


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'eno', 'ename', 'esal', 'eaddr', 'eemail',)


class EmployeeSerializersfunc(serializers.Serializer):
    eno = serializers.IntegerField(read_only=True)
    ename = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    esal = serializers.IntegerField(read_only=True)
    eaddr = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    eemail = serializers.EmailField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.eemail = validated_data.get('eemail', instance.eemail)
        instance.save()
        return instance
