from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        u=request.POST['u'].strip()
        p=request.POST['p'].strip()
        if (u=="" or p=="") :
            context={'msg':'用户名或密码不能为空'}
            return render(request,'login.html',context)
        elif(u=='guojiang' and p=='GJKFcdnchange2018'):
            return render(request, 'index.html')
        else:
            context={'msg':'用户名或密码不正确'}
            return render(request,'login.html',context)
    else:
        return HttpResponse("禁止访问")

def ChangeCDN(request):
    if request.method == 'POST':
        id=request.POST['id'].strip()
        cdn=request.POST['cdn'].strip()

        if(id=="" or cdn==""):
            shu = {'shu': '不能为空'}
            return render(request, 'index.html', shu)

        try:
            id=int(id)
            cdn=int(cdn)
        except:
            shu={'shu':'主播ID只能是数字'}
            return render(request, 'index.html', shu)
        
        print("id:",id)
        print("cnd:",cdn)
        id=str(id)
        cdn=str(cdn)
        sh="/bin/bash x /scripts/change_cdn.sh "+id+" "+cdn
        print(sh)
        os.system(sh)
        context={'msg':'主播ID：','id':id,'msg1':'已执行推流节点切换动作','msg2':'请通知主播退出APP后重新打开APP进行直播'}
        return render(request,'index.html',context)
    else:
        return HttpResponse('非法访问<a href="/">返回首页</a>')