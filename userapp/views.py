from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel
from .serializer import BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def all_book(request):
    books=BookModel.objects.all()
    serializer =BookSerializer(books,many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def get_book(request,id):
    try:
        book = BookModel.objects.get(book_id=id)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except BookModel.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_book(request,id):
    try:
        book = BookModel.objects.get(book_id=id)
        book.delete()
        return Response("book deleted succesfully",status=status.HTTP_200_OK)
    except BookModel.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def add_book(request):
   try:
       serializer = BookSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)
   except BookModel.DoesNotExist:
       return Response(serializer.errors)

@api_view(['PUT'])
def update_book(request,id):
    book = BookModel.objects.get(book_id=id)
    serializer = BookSerializer(instance=book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

