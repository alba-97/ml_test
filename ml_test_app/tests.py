import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import DNASequence
from unittest.mock import patch

class IsMutantTests(APITestCase):
    @patch('ml_test_app.utils.check_sequences')
    def test_with_mutant_dna(self, mock_check_sequences):
        mock_check_sequences.return_value = 2
        url = reverse('mutant')
        data = {"dna": [["A", "T", "G", "C", "G", "A"], 
                        ["C", "A", "G", "T", "G", "C"], 
                        ["T", "T", "A", "T", "G", "T"], 
                        ["A", "G", "A", "A", "G", "G"], 
                        ["C", "C", "C", "C", "T", "A"], 
                        ["T", "C", "A", "C", "T", "G"]]}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(DNASequence.objects.count(), 1)
        self.assertTrue(DNASequence.objects.first().is_mutant)
    
    @patch('ml_test_app.utils.check_sequences')
    def test_with_human_dna(self, mock_check_sequences):
        mock_check_sequences.return_value = 1
        url = reverse('mutant')
        data = {"dna": [["A", "T", "G", "C", "G", "A"], 
                        ["C", "A", "G", "T", "G", "C"], 
                        ["T", "T", "A", "T", "F", "T"], 
                        ["A", "G", "A", "A", "G", "G"], 
                        ["C", "A", "C", "C", "T", "A"], 
                        ["T", "C", "A", "C", "T", "G"]]}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DNASequence.objects.count(), 1)
        self.assertFalse(DNASequence.objects.first().is_mutant)

    def endpoint_with_invalid_dna(self):
        url = reverse('is_mutant')
        data = {"dna": [["A", "T", "G", "C"], ["C", "A", "G"]]}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(DNASequence.objects.count(), 0)

class StatsViewTests(APITestCase):
    def setUp(self):
        DNASequence.objects.create(dna=json.dumps([["A", "T", "G", "C", "G", "A"], 
                                                   ["C", "A", "G", "T", "G", "C"], 
                                                   ["T", "T", "A", "T", "G", "T"], 
                                                   ["A", "G", "A", "A", "G", "G"], 
                                                   ["C", "C", "C", "C", "T", "A"], 
                                                   ["T", "C", "A", "C", "T", "G"]]), is_mutant=True)
        
        DNASequence.objects.create(dna=json.dumps([["A", "T", "G", "C", "G", "A"], 
                                                   ["C", "A", "G", "T", "G", "C"], 
                                                   ["T", "T", "A", "T", "G", "T"], 
                                                   ["A", "G", "A", "A", "G", "G"], 
                                                   ["C", "A", "C", "C", "T", "A"], 
                                                   ["T", "C", "A", "C", "T", "G"]]), is_mutant=False)
    
    def stats_endpoint(self):
        url = reverse('stats')
        
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count_mutant_dna'], 1)
        self.assertEqual(response.data['count_human_dna'], 1)
        self.assertEqual(response.data['ratio'], 1.0)