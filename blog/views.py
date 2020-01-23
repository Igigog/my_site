from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Thread, Message
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    threads = Thread.objects.order_by("-pub_date")[:10]
    return render(request, 'blog/forum.html', {'threads': threads})


def thread(request, int_thread_id):
    curr_thread = Thread.objects.get(id=int_thread_id)
    comments = Message.objects.filter(thread=int_thread_id)
    return render(request, 'blog/thread.html', {'thread': curr_thread,
                                                'comments': comments,
                                                })


@login_required(login_url='/login')
def create_thread(request):
    try:
        title = request.POST['title']
        text = request.POST['text']
        time = timezone.now()
        new_thread = Thread(title=title, text=text, creator=request.user, pub_date=time)
        new_thread.save()
    except KeyError:
        return HttpResponse('Something went wrong')  # TBI
    else:
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url='/login')
def my_threads(request):
    threads = Thread.objects.filter(creator=request.user)
    return HttpResponse(str([trd.title for trd in threads]))


def search_thread(request):
    title = request.POST['search']
    threads = Thread.objects.filter(title__icontains=title)
    return HttpResponse(str([trd.title for trd in threads]))


@login_required(login_url='/login')
def change_thread(request, int_thread_id):
    title = request.POST['title']
    text = request.POST['text']
    thread = Thread.objects.get(id=int_thread_id)
    thread.title = title
    thread.text = text
    thread.save()
    return HttpResponseRedirect(reverse('index'))


def create_comment(request, int_thread_id):
    try:
        text = request.POST['text']
        thread = Thread.objects.get(id=int_thread_id)
        new_comment = Message(text=text, pub_date=timezone.now(),
                              creator=request.user, thread=thread)
        new_comment.save()
    except KeyError:
        return HttpResponse('Something went wrong')  # TBI, maybe...
    else:
        return HttpResponseRedirect(reverse('thread', args=(int_thread_id,)))


def creation_page(request):
    return render(request, 'blog/create_thread.html')
