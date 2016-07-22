from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print ('***')*3
    print "index"
    print ('***')*3
    return render(request, 'index.html')

def ninjas(request):
    print ('***')*3
    print "ninjas"
    print ('***')*3
    request.session['ninjas'] = ninjas
    return render(request, 'ninjas.html')

def colors(request):
    print ('***')*3
    print "colors"
    print ('***')*3
    if ninjas
    request.session['ninjas'] = ninjas
    return render(request, 'ninjas.html')
