from django.shortcuts import render
import operator
# Create your views here.

def word_home(request):
    return render(request, 'word_home.html')

def count(request):
    fulltext = request.POST['fulltext']
    word_list = fulltext.split()
    word_list_len = len(word_list)
    
    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1 
            
    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'word_count.html', {'fulltext': fulltext, 'word_dic_len': word_list_len, 'worddictionary': sorted_words})
