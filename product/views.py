#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import MainContent

#from django.shortcuts import render

# Create your views here.
def index(request):
    content_list = MainContent.objects.order_by('-pub_date') # - : 역순이므로 가장 최근 것 상단에
    context = {'content_list':content_list}
    return render(request, 'product/content_list.html',context)
    #return HttpResponse("Hello World")


def detail(request, content_id):
    #content_list = MainContent.objects.get(id=content_id)
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list':content_list}
    return render(request, 'product/content_detail.html',context)
