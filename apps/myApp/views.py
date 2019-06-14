from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    context = {
        'allbooks': Book.objects.all(),
    }
    return render(request, 'myApp/index.html', context) 


def books(request):
    Book.objects.create(title=request.POST['titleadd'], description=request.POST['descadd'])
    return redirect('/')

def bookid(request, Book_id):
    Book_id = int(Book_id)
    book = Book.objects.get(id=Book_id)
    allauthors = book.authors.all()
    everyauthor = Author.objects.all()
    context = {
        'book': book,
        'allauthors': allauthors,
        'otherauthors': everyauthor.difference(allauthors),
    }
    return render(request, 'myApp/bookint.html', context)

def authors(request):
    context = {
        'allauthors': Author.objects.all(),
    }
    return render(request, 'myApp/authors.html', context)

def authoradd(request):
    Author.objects.create(first_name = request.POST['firstname'], last_name=  request.POST['lastname'], notes = request.POST['notes'])
    return redirect('/authors')

def authorid(request, Author_id):
    Author_id = int(Author_id)
    author = Author.objects.get(id=Author_id)
    allbooks = author.books.all()
    everybook = Book.objects.all()
    context = {
        'author': author,
        'allbooks': allbooks,
        'otherbooks': everybook.difference(allbooks),
    }
    return render(request, 'myApp/authorint.html', context)

def bookauthor(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')


def authorbook(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/authors/{author_id}')
