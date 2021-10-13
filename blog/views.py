from django.shortcuts import render , redirect 
from django.http import HttpResponse
from .models import Blog , Page_seo , report , feature
from django.contrib import messages
from django.core.paginator import Paginator
#########################################################################################
def home(request):
    data = reversed(Blog.objects.all())
    features = feature.objects.all()
    recent = Blog.objects.last()   
    data = list(data)
    data = data[1:5]
    page_data = Page_seo.objects.filter(name = 'home') 
    return render(request,'index.html',{'data':data,'recent':recent,'page_data':page_data[0],'features':features})
#########################################################################################
def all(request):
    data = reversed(Blog.objects.all())
    page_data = Page_seo.objects.filter(name = 'all') 
    features = feature.objects.all()
    return render(request,'all.html',{'data':data,'page_data':page_data[0],'features':features})
#########################################################################################
def about(request):
    page_data = Page_seo.objects.filter(name = 'about') 
    features = feature.objects.all()
    return render(request,'about.html',{'page_data':page_data[0],'features':features}) 
#########################################################################################
def privacy(request):
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'privacy') 
    return render(request,'privacy and policy.html',{'page_data':page_data[0],'features':features})
######################################################################################### 
def terms(request):
    page_data = Page_seo.objects.filter(name = 'terms') 
    features = feature.objects.all()
    return render(request,'terms.html',{'page_data':page_data[0],'features':features}) 
#########################################################################################
def viewpost(request ,slug_text):
    page_data = Blog.objects.filter(slug = slug_text)
    features = feature.objects.all()
    blog = page_data[0]
    category = page_data[0].category
    suggested_post = Blog.objects.filter(category=category)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", blog) 
    if page_data.exists():
        page_data = page_data.first()
    else:
        return HttpResponse("<h1>Page not founddddddddddddddd</h1>")
    all_data = Blog.objects.all()
    parametre = {'page_data':page_data,'data':suggested_post,'features':features}
    return render(request,'viewpost.html',parametre)

#########################################################################################
def page_motivation(request):
    data = Blog.objects.filter(category = 'motivation')
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'motivation') 
    param = {'data':data,'page_data':page_data[0],'features':features}
    return render(request,'page.html',param)
#########################################################################################
def page_mystery(request):
    data = Blog.objects.filter(category = 'mystery')
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'mystery')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>",page_data)
    param = {'data':data,'page_data':page_data[0],'features':features}
    return render(request,'page.html',param)
#########################################################################################
def page_history(request):
    data = Blog.objects.filter(category = 'history')
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'history')
    param = {'data':data,'page_data':page_data[0],'features':features}
    return render(request,'page.html',param)
#########################################################################################
def page_fact(request):
    data = Blog.objects.filter(category = 'fact')
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'fact')
    param = {'data':data,'page_data':page_data[0],'features':features}
    return render(request,'page.html',param)
#########################################################################################
def page_horror(request):
    data = Blog.objects.filter(category = 'horror')
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'horror')
    param = {'data':data,'page_data':page_data[0],'features':features}
    return render(request,'page.html',param)
#########################################################################################
def page_movie(request):
    data = Blog.objects.filter(category = 'movie')
    features = feature.objects.all()
    page_data = Page_seo.objects.filter(name = 'movie')
    param = {'data':data,'page_data':page_data[0],'features':features}
    return render(request,'page.html',param)
#########################################################################################
def search(request ):
    if request.method == "POST":
        features = feature.objects.all()
        a = request.POST.get("search",False)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>",a)
        a_list = a.split()
        print(a_list)
        search_data = []
        get_data = Blog.objects.all()
        for data in get_data:
            i = 0
            for item in a_list:
                if item.lower() in (data.title+data.content+data.metatags+data.metadesc+data.category).lower():
                    i +=1
            if len(a_list)==i:
                if data not in search_data:
                    search_data.append(data)  
        return render(request, "search.html",{'data':search_data,'features':features})
    else:
        return redirect('search')
# Create your views here.
#########################################################################################
def report_data(request):
    if request.method == "POST":
        features = feature.objects.all()
        email = request.POST.get('email',False)
        discription = request.POST.get('discription',False)
        
        i = len(report.objects.all())
        print(email , discription , i)
        if i<30:
            report.objects.create(email = email , discription = discription)
            messages.info(request , 'successfully submited')
            return render(request, "about.html" , {'features':features})
        else:
            messages.info(request , 'this process can not be proceed now please try again later')
            return render(request, "about.html" ,{'features':features} )

