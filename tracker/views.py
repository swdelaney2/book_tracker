from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render

from .models import Book
from .forms import NewBookForm

def index(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.save()
            book = get_object_or_404(Book, pk=saved_form.id)
            message = "Book added!!"
            context = {'book': book,
                       'message': message
                }
            return render(request, 'detail.html', context)

    else:
        form = NewBookForm()

        context = {'form': form
               }

        return render(request, 'index.html', context)

def overview(request):
    read_books = Book.objects.filter(read=True).order_by('-date_created')
    to_read_books = Book.objects.filter(read=False).order_by('-date_created')

    context = {'read_books': read_books,
               'to_read_books': to_read_books
           }

    return render(request, 'overview.html', context)


def change_read_status(request, book_id, status):
    book = get_object_or_404(Book, pk=book_id)
    setattr(book, 'read', status)
    book.save()


    read_books = Book.objects.filter(read=True).order_by('-date_created')
    to_read_books = Book.objects.filter(read=False).order_by('-date_created')

    context = {'read_books': read_books,
               'to_read_books': to_read_books
               }

    return render(request, 'overview.html', context)

# PAGINATOR

def listing(request):
    full_book_list = Book.objects.all().order_by('title')
    paginator = Paginator(full_book_list, 4) # Show 5 books per page

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'books': books})
