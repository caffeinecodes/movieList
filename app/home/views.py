import urllib2
from bs4 import BeautifulSoup
from django.shortcuts import render
from app.movies.models import Movie
from app.series.models import Season, Series
from app.links.models import Links


def index(request):
    context = {}
    series_url = 'http://79.127.126.110/Serial/Game%20of%20Thrones'
    series, created = Series.objects.get_or_create(name="Game of Thrones", url=series_url)
    for i in range(10):
        try:
            season_index = str(i).zfill(2)
            url = '{0}/S{1}/'.format(series_url, season_index)
            page = urllib2.urlopen(url).read()
            context['soup'] = BeautifulSoup(page)
            season, created = Season.objects.get_or_create(series=series, url=url,
                                                           name='Series {0}'.format(season_index))
            for anchor in context['soup'].findAll('a', href=True):
                print url + anchor['href']
                try:
                    if anchor['href'].index(".mkv"):
                        link, created = Links.objects.get_or_create(season=season, url=url + anchor['href'], name=anchor['href'])
                except ValueError:
                    pass
            season.save()
        except (urllib2.HTTPError, urllib2.URLError):
            pass

    context['links'] = Links.objects.all()
    return render(request, 'home/index.html', context)

