from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ml_test_app.utils.check_sequences import check_sequences
from .serializers import DNASequenceSerializer
from .models import DNASequence
import json

class IsMutant(APIView):
    def post(self, request):
        serializer = DNASequenceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dna = serializer.validated_data["dna"]
        result = check_sequences(dna)
        sequence = DNASequence(dna=json.dumps(dna), is_mutant=result > 1)
        sequence.save()

        if result > 1:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_200_OK)


class StatsView(APIView):
    def get(self, request):
        mutant_count = DNASequence.objects.filter(is_mutant=True).count()
        human_count = DNASequence.objects.filter(is_mutant=False).count()
        ratio = mutant_count / human_count if human_count > 0 else 0

        return Response({
            'count_mutant_dna': mutant_count,
            'count_human_dna': human_count,
            'ratio': ratio
        })