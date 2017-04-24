from django.shortcuts import render
from django.http import HttpResponse
from acorta.models import urls
from django.views.decorators.csrf import csrf_exempt
import urllib
# Create your views here.

@csrf_exempt  #Se pone para que no se tengan en cuenta las funciones de seguridad
def barra(request):


	if request.method == 'GET':

		htmlbody = "<h3>Hola. Bienvenido a 'acorta'</h3>" + \
					"<form method ='POST' action=''>Dame una URL: <input type='text'" + \
 					"name = 'url'><input type='submit' value='Send'></form>"
		
	elif request.method == 'POST':
		urls_list = urls.objects.all()
		cuerpo = str(request.body)
		url = cuerpo.split('=')[1][:-1]
		if not url.startswith('https://') or not url.startswith('http://'):
			url = 'http://' + url
		try:
			url_new = urls.objects.get(url_real = url)
			
			urls_list = urls.objects.all()
			htmlbody = 'LISTA CON LAS URLs GUARDADAS'
			for pags in urls_list:
				htmlbody += '<ul>'
				htmlbody += '<li><a href=' + pags.url_real + '> Url real:  ' + pags.url_real +'</a>'
				htmlbody += '<a href= ' + pags.url_real + '> || Url acortada:  ' + str(pags.url_short) + '</a></li>'
				htmlbody += '</ul>'

		except urls.DoesNotExist:
			guardar= urls(url_real=url,url_short = len(urls_list))
			guardar.save()

			urls_list = urls.objects.all()
			htmlbody = 'LISTA CON LAS URLs GUARDADAS'
			for pags in urls_list:
				htmlbody += '<ul>'
				htmlbody += '<li><a href=' + pags.url_real + '> Url real:  ' + pags.url_real +'</a>'
				htmlbody += '<a href= ' + pags.url_real + '> || Url acortada:  ' + str(pags.url_short) + '</a></li>'
				htmlbody += '</ul>'
	return HttpResponse(htmlbody)

def error(request):
	body = '<h3><p> Page not found </p></h3>'
	body += '<p>Try a correct url: "localhost:1234/"</p>'
	return HttpResponse(body)
