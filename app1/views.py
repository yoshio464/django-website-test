from django.views.generic import TemplateView

# index用のview
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['username'] = '太郎'
        return ctxt

#about用のview
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['num_services'] = 123456
        ctxt['skills'] = [
            'Python',
            'C++',
            'JavaScript',
            'Rust',
            'Go'
        ]
        return ctxt
