from django.test import TestCase

# Create your tests here.
from django.shortcuts import render

def Exam_board(request):
    return render(request, 'Exam_board.html')
