from django.shortcuts import render, redirect
import datetime
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))


def indexpage(requerst):
    date_now = datetime.date.today()
    curr_date = f'{date_now.day}/{date_now.month}/{date_now.year}'
    context = {'date': curr_date, 'page': 'index'}
    return render(requerst, 'index.html', context)

def wordlist(request):
    ori = []
    with open(os.path.join(curr_dir, 'media/words.txt'), 'r', encoding="utf-8") as file:
        for pair in file:
            pair = pair.split(',')
            ori.append(pair)
    return render(request, 'wordlist.html', context={'words': ori, 'page': 'wordlist'})

def addword(request):
    if request.method == 'GET':
        return render(request, 'newword.html', context={'page': 'newword'})
    else:
        print(request.POST['ori'], request.POST['tr'])
        with open(os.path.join(curr_dir, 'media/words.txt'), 'a', encoding="utf-8") as file:
            file.writelines(f'{request.POST["ori"]},{request.POST["tr"]}\n')
        return redirect(indexpage)
