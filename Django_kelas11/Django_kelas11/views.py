from django.shortcuts import render


def index(request):
    dict = {
        'title': 'Kelas Terbuka',
        'heading': 'Selamat datang',
        'subheading': 'Selamat datang di web ini'
    }
    return render(request, 'index.html', dict)
