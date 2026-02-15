from rest_framework import serializers
from .models import JobModel, ProposalModel


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = '__all__'

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalModel
        fields = '__all__'
        # Set freelancer as read_only if you plan to set it from the request.user in the view
        read_only_fields = ['freelancer']

    def validate(self, data):
        # 1. Access the job instance directly from the validated data
        job = data.get('job')
        bid_amount = data.get('bid_amount')

        # In a real scenario, the freelancer is the logged-in user
        # We get this from the context passed by the view
        user = self.context['request'].user

        # 2. Validation: Bid vs Budget
        if bid_amount > job.budget:
            raise serializers.ValidationError({
                "bid_amount": f"Your bid ({bid_amount}) cannot exceed the job budget ({job.budget})."
            })

        # 3. Validation: Prevent bidding on your own job
        if job.created_by == user:
            raise serializers.ValidationError("You cannot submit a proposal for your own job.")

        return data




