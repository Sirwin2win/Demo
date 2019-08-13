from django.urls import path
from . import views
# from users import views as user_views
# from . import contact
from .views import HomePageView

urlpatterns=[


    path('hello/', views.hello, name='post-hello'),
    path('', views.home, name='post-home'),
    path('', HomePageView.as_view(), name='pics'),
    path('see/', views.see, name='post-see'),
    # path('sendSimpleEmail/', views.sendSimpleEmail)
    # path('register/', user_views.register, name='register')
]
    # path('admin/', admin.site.urls),
