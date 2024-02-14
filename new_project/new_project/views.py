from django.shortcuts import render
from chat_downloader import ChatDownloader
from chat_downloader.errors import NoChatReplay
from django.http import JsonResponse,HttpResponse


def index(request):
    return render(request, 'index.html')


def vanity_url(request):
    if request.method == 'GET': 
        url = request.GET.get('q', None)
        try:
            chat = ChatDownloader().get_chat(url,chat_type='live')
            if chat:
                return JsonResponse({'msg':'當前直播中'})
            raise NoChatReplay
        except NoChatReplay:
            return JsonResponse({'msg':'當前輸入網址並非直播或已經結束直播'})
    else:
        return HttpResponse(status=405)