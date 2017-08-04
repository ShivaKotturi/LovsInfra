from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^$', views.stocks, name="stocks"),
    url(r'^price/(?P<category>\w+)$', views.get_price, name="price"),
    url(r'^invoice/$', views.generate_invoice, name="invoice")
]