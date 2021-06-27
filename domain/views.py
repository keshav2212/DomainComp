from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    header = {
    'Authorization': 'sso-key UzQxLikm_46KxDFnbjN7cQjmw6wocia:46L26ydpkwMaKZV6uVdDWe',
    'Accept': 'application/json'
    }
    context ={}
    if request.method == "POST":
    	domain = request.POST['domain']
    	url = "https://api.ote-godaddy.com/v1/domains/available?domain=%s"%domain
    	res = requests.get(headers = header, url = url)
    	try:
    		x = res.json()
    		if x['available'] is True:
    			x['price'] = (x['price']/1000000)*74
    		context['res1'] = x
    	except:
	    	context['error'] = res.json()
    	return render(request, 'index.html', context)
    url = "https://api.ote-godaddy.com/v1/domains/tlds"
    res = requests.get(headers = header, url = url)
    context['res'] = res.json()
    return render(request, 'index.html',context)