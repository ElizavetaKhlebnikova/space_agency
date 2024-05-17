from django.views.generic.base import TemplateView
from .models import ImageForMainPageModel


class LandingPageView(TemplateView):
    template_name = 'landing/landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context['object_list'] = ImageForMainPageModel.objects.order_by('my_order')
        context['title'] = 'NASA - космическое агентство'
        return context
