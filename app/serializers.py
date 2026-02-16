from rest_framework import serializers


class ResumeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    ph_no = serializers.RegexField(regex= "^\d{10}$")