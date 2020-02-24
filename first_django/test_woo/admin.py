from django.contrib import admin
from test_woo.models import Test_woo

@admin.register(Test_woo)
class Test_wooAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')
