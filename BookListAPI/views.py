from django.shortcuts import render

from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
def books_view(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"Books": list(books)})
    else:
        if request.method == "POST":
            title = request.POST.get('title')
            author = request.POST.get('author')
            price = request.POST.get('price')
        book = Book(
            title=title, 
            author=author, 
            price=price
            )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        return JsonResponse(model_to_dict(books) and status==201)


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def books(request):
    return Response('List of books', status=status.HTTP_200_OK)