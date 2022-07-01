from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_details, name='post_details'),
    path('about/',views.About,name="about"),
    path('blog/about.html',views.About,name="about"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/blog/about',views.aboutWargs,name="AboutWargs"),

    path('blog/contact.html',views.Contact,name="contact"),
    path('contact/',views.Contact,name="contact"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/blog/contact',views.contactWargs,name="ContactWargs"),
]
