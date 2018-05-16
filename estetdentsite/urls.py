from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

from estetdent import settings
from estetdentsite import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('spec/', views.SpecListView.as_view(), name='spec_list'),
    path('spec/<int:pk>/', views.SpecDetailView.as_view(), name='spec_detail'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('',RedirectView.as_view(pattern_name='about')),
    path('service/', views.ServiceListView.as_view(), name='serv_list')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
