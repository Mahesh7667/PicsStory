from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.contrib import messages
from django.http import HttpResponse
import templates
from .models import ImgModel
from .forms import ImgForm
from rest_framework import serializers
# Create your views here.

class HomeView(APIView):
    def get(self, request):
        query_results = ImgModel.objects.all()
        return render(request , 'index.html' , {'query_results':query_results})

class serializerClass(serializers.Serializer):
    img = serializers.ImageField()
    msg = serializers.CharField(max_length=100)

class ImgView(APIView):
    serializer_class = serializerClass
    def get(self, request):
        print("GET")
        return render(request , 'post.html' ,{'form':ImgForm})

    def post(self, request):
        print("----------POST-----------")
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request , "IMAGE UPLOADED")
            # return render(request , 'post.html' ,{'form':ImgForm})
            return HttpResponse(render(request,'post.html', {'form':ImgForm}),status = 200)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class SearchView(APIView):
    serializer_class = serializerClass
    def get(self, request, pk,*args,**kwargs ):
        print("GET")
        print(pk)
        obj = ImgModel.objects.get(pk=pk)
        print(obj.img)
        return render(request , 'Search.html' ,{"obj":obj})


    # def post(self, request):
    #     print(request)
    #     print(request.data)
    #     print(request.POST)
    #     data = self.serializer_class(data=request.data)
    #     if data.is_valid():
    #         obj = ImgModel() #gets new object
    #         print(data)
    #         obj.img =  data.validated_data.get('img')
    #         obj.save()
    #         return Response({'oj':'df'}, status=status.HTTP_200_OK)
    #     return Response({'oj':'df'}, status=status.HTTP_404_NOT_FOUND)
