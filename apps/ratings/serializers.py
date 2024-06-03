from .models import Rating
from rest_framework import serializers

class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]    


    def get_rater(self, obj):
        return obj.rater.username # obj is the instance of Rating -> User
    
    def get_agent(self, obj):
        return obj.agent.user.username # obj is the instance Rating -> Profile -> User
    


