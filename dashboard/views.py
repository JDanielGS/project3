from django.shortcuts import render
from django.views.generic import TemplateView, View
from newsletters.models import NewsLetter

class dashboardHomeView(TemplateView):
    template_name=r'C:\Users\usuario\project3\templates\dashboard\index.html'

class NewsLettersDashboardHomeView(View):
    def get(self, request, *args, **kwargs):
        newsletters=NewsLetter.objects.all()

        context={
            'newsletters':newsletters
        }
        return render(request, 'dashboard/list.html', context)