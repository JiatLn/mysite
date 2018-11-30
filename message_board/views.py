from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

from .models import Message

# Create your views here.
def message(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    messages = Message.objects.all()
    context = {}
    context['content'] = '这是留言板1.0，属于测试版本...'
    context['messages'] = messages

    if request.method == 'POST':
        nickname = request.POST.get('nickname', 'null')
        email = request.POST.get('email', 'null')
        content = request.POST.get('content', 'null')

        # print(nickname, email, content, referer)
        message = Message(nickname=nickname, email=email, content=content)
        message.save()
        return redirect(referer)

    return render(request, 'message_board/message.html', context)