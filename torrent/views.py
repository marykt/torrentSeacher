from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import TorrentData
# Create your views here.
def index(request):
    template = loader.get_template('torrent/index.html')
    context={}
    return HttpResponse(template.render(context))
# def full_search(request):
#     sform = SearchForm(request.GET)
#     posts = sform.search()
#     template = 'product_search_list.html'
#     c = Context({'posts': posts})
#     return render_to_response(template, c)
def searchResult(request):
    s=request.GET.get("wd")

    torrents=TorrentData.objects.filter(name__contains=s).order_by("-hot1")
    template = loader.get_template('torrent/showResult.html')
    context = {"torrents":torrents}
    return HttpResponse(template.render(context))