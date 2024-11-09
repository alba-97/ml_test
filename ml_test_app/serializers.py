from rest_framework import serializers

class DNASequenceSerializer(serializers.Serializer):
    dna = serializers.ListField(
        child=serializers.ListField(
            child=serializers.CharField()
        )
    )

    def validate_dna(self, value):
        if not all(isinstance(row, list) for row in value):
            raise serializers.ValidationError("DNA must be a list of lists.")
        
        row_length = len(value[0])
        
        for row in value:
            if len(row) != row_length:
                raise serializers.ValidationError("All rows must have the same length.")
        
        return value
