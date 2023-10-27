from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from mysite import models
import random 

DEVELOPER_KEY = "AIzaSyCqWPwBqGABC-zZPCagJcMcC_8bZhUz_EQ"

def index(request):
    mlists = models.MovieList.objects.all().order_by('-id')
    if request.method=="POST":
        name = request.POST['name']
        desc = request.POST['desc']
        if name != "" and desc != "":
            models.MovieList.objects.create(name=name, desc=desc)
        return redirect("/")
    return render(request, 'index.html', locals())

def show(request, id):
    target_list = models.MovieList.objects.get(id=id)
    videos = target_list.movie_set.all()
    #videos = models.Movie.objects.filter(mlist=target_list)
    return render(request, 'show.html', locals())

@login_required
def search(request):
    mlists = models.MovieList.objects.all().order_by('-id')
    if request.method=="POST":
        youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY)
        google_req = youtube.search().list(
        part = "snippet",
        q = request.POST['q'],
        maxResults = 20
        )
        response = google_req.execute()
        items = response['items']
        videos = list()
        for item in items:
            try:
                video = dict()
                if item['id']['kind']=='youtube#playlist':
                    video["vid"] = item['id']['playlistId']
                else:
                    video["vid"] = item['id']['videoId']
                video["title"] = item['snippet']['title']
                video["channel"] = item['snippet']['channelTitle']
                videos.append(video)
            except:
                pass
        random.shuffle(videos)
    else:
        pass
    return render(request, "search.html", locals())

@login_required
def add(request, title, vid):
    mlists = models.MovieList.objects.all()
    if request.method=='POST':
        list_id = request.POST["list_id"]
        target_list = models.MovieList.objects.get(id=list_id)
        title = request.POST['title']
        vid = request.POST['vid']
        if title != "" and vid != "":
            models.Movie.objects.create(title=title, vid=vid, mlist=target_list)
        return redirect("/show/{}/".format(list_id))
    else:
        pass
    return render(request, "add.html", locals())

@login_required
def edit(request, id):
    target_list = models.MovieList.objects.get(id=id)
    videos = target_list.movie_set.all()
    if request.method=="POST":
        title = request.POST['title']
        vid = request.POST['vid']
        if title != "" and vid != "":
            models.Movie.objects.create(title=title, vid=vid, mlist=target_list)
        return redirect("/edit/%s/" % id)
    return render(request, "edit.html", locals())

@login_required
def delete_list(request, id):
    target_list = models.MovieList.objects.get(id=id)
    target_list.delete()
    return redirect("/")

@login_required
def delete(request, id):
    target_video = models.Movie.objects.get(id=id)
    target_video.delete()
    return redirect("/edit/%s/" % target_video.mlist.id)

def play(request, id):
    target_video = models.Movie.objects.get(id=id)
    target_video.counter += 1
    target_video.save()
    return render(request, "play.html", locals())

def info(request):
    rank = models.Movie.objects.order_by("-counter")[:5]
    return render(request, "info.html", locals())