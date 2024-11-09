from rest_framework import serializers

class DNASequenceSerializer(serializers.Serializer):
    dna = serializers.ListField(
        child=serializers.CharField()
    )

    def validate_dna(self, value):
        lengths = [len(seq) for seq in value]
        if len(set(lengths)) > 1:
            raise serializers.ValidationError("All DNA sequences must have the same length")
        return value