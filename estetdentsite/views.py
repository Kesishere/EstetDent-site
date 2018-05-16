from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from estetdentsite.models import Spec, Service


class AboutView(TemplateView):
    template_name = 'about.html'


class SpecListView(ListView):
    model = Spec
    template_name = 'spec_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spec_list'] = Spec.objects.all()
        return context


class SpecDetailView(DetailView):
    model = Spec
    template_name = 'spec_detail.html'
    queryset = Spec.objects.all()

    def get_object(self):
        # Call the superclass
        object = super().get_object()
        # Record the last accessed date
        object.save()
        # Return the object
        return object

class ContactsView(TemplateView):
    template_name = 'contacts.html'

class ServiceListView(ListView):
    model = Service
    template_name = 'serv_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['serv_list'] = Service.objects.all()
        return context