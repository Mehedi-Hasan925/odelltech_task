from django.contrib.auth import forms
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,redirect
from app_user_info import models
from app_user_info import forms
from django.urls import reverse,reverse_lazy
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


# Create your views here.
class division_view(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self,request):
        form = forms.user_info_form()
        diction = {'form':form}
        return render(request,'app_user_info/home.html',context=diction)
        
    
    def post(self,request,format=None):
        country = request.data['country'] # name of the Divisions tables foreignkey
        division = {}
        # div = request.POST.get['Division']
        # dis = request.POST.get['District']
        # upz = request.POST.get[]
        form = forms.user_info_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_user_info:home_view'))
        
        if country:
            divisions = models.Country.objects.get(id=country).divisions.all()
            division = {p.name:p.id for p in divisions}
        return JsonResponse(data=division,safe=False)

class district_view(APIView):
    # permission_classes = [IsAuthenticated,]
    
    def post(self,request,format=None):
        division = request.data['division'] # name of the District tables foreignkey
        district = {}
        if division:
            districts = models.Divisions.objects.get(id=division).zila.all()
            district = {p.name:p.id for p in districts}
        return JsonResponse(data=district,safe=False)


class upazilla_view(APIView):
    # permission_classes = [IsAuthenticated,]
    
    def post(self,request,format=None):
        district = request.data['district'] # name of the upazila tables foreignkey
        upazilla = {}
        if district:
            upazillas = models.Districts.objects.get(id=district).thana.all()
            upazilla = {p.name:p.id for p in upazillas}
        return JsonResponse(data=upazilla,safe=False)

def users_view(request):
    all_user = models.User_info.objects.all()
    diction = {'all_user':all_user}
    return render(request,'app_user_info/users.html',context=diction)


def search_user_view(request):
     if request.method == 'GET':
        pattern = request.GET.get('search','')
        result = models.User_info.objects.filter(Q(name__icontains=pattern))
        diction = {'result':result,'pattern':pattern}
        return render(request,'app_user_info/search_user.html',context=diction)
