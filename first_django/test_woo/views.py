from django.views.generic import ListView, DetailView
from test_woo.models import Test_woo

class Test_wooLV(ListView):
    model = Test_woo

class Test_wooDV(DetailView):
    model = Test_woo
    