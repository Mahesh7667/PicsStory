from django.urls import path
from .views import HomeView, ImgView, SearchView
from django.conf.urls.static import static
from PicsStory import settings
urlpatterns =[
    path('', HomeView.as_view() ),

    path('addpost/', ImgView.as_view() ,name="addImage"),

    path(r'search/<int:pk>/', SearchView.as_view(), name='search_page'),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)