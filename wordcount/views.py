from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    word_list = fulltext.split()

    word_dictionary = {}
    for word in word_list:
        word_dictionary[word] = word_dictionary.get(word, 0) + 1

    word_count = list(word_dictionary.items())
    word_count.sort(key=operator.itemgetter(1), reverse=True)

    # word_count.sort(key=operator.itemgetter(1))

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(word_list), 'word_count': word_count})


def about(request):
    return render(request, 'about.html')
