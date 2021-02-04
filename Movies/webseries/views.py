from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h1 style='color:green;background-color:orange'>Hi Welcome to APSSDC Workshop </h1>")
def names(request,name):
	return HttpResponse("my name is "+name)
def tags(req):
	return render(req,'webseries/tag.html')
def re(request):
	if request.method == "POST":
		a = request.POST['fname']
		b = request.POST['mk']
		return render(request,'webseries/viewdata.html',{'f':a, 'e':b})
		
		print(a,b)
	return render(request,'webseries/registration.html')