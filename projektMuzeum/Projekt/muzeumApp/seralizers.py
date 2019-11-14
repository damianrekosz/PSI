from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_imie(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "Blog post is not about Django",
            )
        return value
