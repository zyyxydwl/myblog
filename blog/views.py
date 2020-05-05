from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog import models


def index(request):
    # return HttpResponse("Hello blog.")
    articals = models.Artical.objects.all()
    return render(request, "index.html", {'articals': articals})


def artical_page(request, artical_id):
    artical = models.Artical.objects.get(pk=artical_id)
    return render(request, "blog/artical_page.html", {'artical': artical})


def edit_page(request, artical_id):
    # 在新建文章中传 0，在修改文章中传artical_id
    if str(artical_id) == '0':
        return render(request, "blog/edit_page.html")
    artical = models.Artical.objects.get(pk=artical_id)
    return render(request, "blog/edit_page.html", {'artical': artical})


def edit_action(request):
    artical_id = request.POST.get('artical_id','0')
    # print(artical_id) 从 edit_page 接收过来的值
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')

    if artical_id == '0':
        models.Artical.objects.create(title=title, content=content)
        articals = models.Artical.objects.all()
        return render(request, "index.html", {"articals": articals})
    artical = models.Artical.objects.get(pk=artical_id)
    artical.title = title
    artical.content = content
    artical.save()
    # artical.update()
    # 修改完成后跳转至文章页面
    return render(request, "blog/artical_page.html", {'artical': artical})



