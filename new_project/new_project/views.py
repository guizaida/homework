from django.shortcuts import render
from yt_dlp import YoutubeDL
from django.http import JsonResponse,HttpResponse


def index(request):
    return render(request, 'index.html')


def verify_url(request):
    if request.method == 'GET': 
        url = request.GET.get('q', None)
        ydl_opts = {
            'quiet': True,  # 減少輸出信息，保持輸出整潔
            'simulate': True,  # 不實際下載視頻
        }
        info_msg = "影片標題:{0}\n頻道名稱:{1}\n直播狀態:{2}\n\n"
        with YoutubeDL(ydl_opts) as ydl:
            msg = None
            info_dict = ydl.extract_info(url, download=False)
            status = info_dict.get('live_status')
            title = info_dict.get('fulltitle')
            channel = info_dict.get('channel')
            if status in {"is_live", 'was_live'}:
                if info_dict.get('is_live'):
                    msg = '正在進行中'
                else:
                    msg = '結束'
            else:
                msg = '並非直播'
        return JsonResponse({'msg':info_msg.format(title,channel,msg if msg else '未知錯誤')})
    else:
        return HttpResponse(status=405)