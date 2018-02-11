from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import RestaurantLocation

# Create your views here.

def restaurant_listview(request):
	template_name = 'restaurants/restaurant_list.html'
	queryset = RestaurantLocation.objects.all()
	context={
		"object_list":queryset
	}
	return render(request,template_name,context)

#def home(request):
	#return HttpResponse("Hello")
	#return render(request, "home.html")

#def about(request):
	#return HttpResponse("Hello")
	#return render(request, "about.html")


#def kontak(request):
	#return HttpResponse("Hello")
	#return render(request, "kontak.html")

#class ContactView(View):
	#def get(self,request):
		#context = {}
		#return render(request,"kontak.html",context)

#class ContactView(TemplateView):
#	template_name = 'kontak.html'

	#template_name = 'home.html'
		
#class AboutView(TemplateView):
	#template_name = 'about.html'		
		