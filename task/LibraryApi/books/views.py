from django.shortcuts import render,redirect
from books.models import Book
from django.contrib import messages
from rest_framework import generics
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def Add(request):
    if request.method =="POST":
        tt = request.POST.get('title')
        aut=request.POST.get('author')
        year=request.POST.get('year')
        ob=Book(Title=tt,Author=aut,Publication_Year=year)
        ob.save()
        messages.add_message(request,messages.INFO,"Book Data Added Successfully")

    return render(request,'Addbooks.html')

def View(request):
    op=Book.objects.all()
    
    return render(request,'index.html',{"ok":op})

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.add_message(request,messages.INFO,"Book Data Deleted Successfully")
    return redirect('view')

def edit(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == "POST":
        # Retrieve the updated data from the form
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('year')

        # Update the book object with the new data
        book.Title = title
        book.Author = author
        book.Publication_Year = publication_year
        book.save()
        messages.add_message(request,messages.INFO,"Book Data updated Successfully")

        return redirect('view')  # Assuming 'view' is the name of the view for displaying the book list

    return render(request, 'edit.html', {'book': book})
    
