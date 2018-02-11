from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from .models import RestaurantLocation

# Create your views here.

def restaurant_listview(request):
	template_name = 'restaurants/restaurant_list.html'
	queryset = RestaurantLocation.objects.all()
	context={
		"object_list":queryset
	}
	return render(request,template_name,context)

class RestaurantListView(ListView):
	#template_name = 'restaurants/restaurant_list.html'

	def get_queryset(self):
		
		slug =self.kwargs.get("slug")
		if slug:
			queryset=RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)

				)
		else:
			queryset=RestaurantLocation.objects.all()
		return queryset

class RestaurantDetailView(DetailView):
	queryset=RestaurantLocation.objects.all()
	
	#def get_context_data(self,*args,**kwargs):
	#	print(self.kwargs)
	#	context = super(RestaurantDetailView, self).get_context_data(*args,**kwargs)
	#	print(context)
	#	return context

	#def get_object(self,*args,**kwargs):
	#	rest_id = self.kwargs.get('rest_id')
	#	obj = get_object_or_404(RestaurantLocation, id=rest_id) # mereplace pk dengan rest_id
	#	return obj


#class MexicanListView(ListView):
	#queryset=RestaurantLocation.objects.filter(category__iexact='mexican')
	#template_name = 'restaurants/restaurant_list.html'

#class AsianFusionListView(ListView):
	#queryset=RestaurantLocation.objects.filter(category__iexact='asian fusion')
	#template_name = 'restaurants/restaurant_list.html'

#class SearchListView(ListView):
#	template_name = 'restaurants/restaurant_list.html'

#	def get_queryset(self):
#		print(self.kwargs)
#		slug =self.kwargs.get("slug")
#		if slug:
#			queryset=RestaurantLocation.objects.filter(
#				Q(category__iexact=slug) |
#				Q(category__icontains=slug)

#				)
#		queryset=RestaurantLocation.objects.none()
#		return queryset


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
		