from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()#각단어들을 리스트에 넣어놓은것
    word_dic = {}#텅 비어있는 딕셔너리
    for word in words :#words 리스트에 각각의 변수를 word로 탐색
        if word in word_dic :#만약 word_dic의 key값중 word가 있으면
            #increase
            word_dic[word]+=1 # word_dic의 value를 1증가
        else : #만약 word_dic의 key값중 word가 없으면
            # add to dictionary
            word_dic[word]=1# word_dic value를 1로 설정

    return render(request,'result.html', {'full': text, 'total':len(words), 'dictionary': word_dic.items()})    