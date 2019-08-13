# from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib import admin
from django.conf import settings # new
# from django.urls import path, include # new
# from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
# from users.views import pics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('register/', user_views.register, name='register'),
    path('email/', user_views.email, name='email'),
    path('pics/',user_views.pics, name='pics'),
    # path('he/',user_views.he, name='he')
    path('successView/',user_views.successView, name='successView'),
    # path('', include('post.urls')),
      path('img/', user_views.img, name = 'img'), 
      path('serv1/', user_views.serv1, name = 'serv1'), 
      path('ev/', user_views.ev, name = 'ev'),
      # path('login/', auth_views.login, {'template_name': 'users/tes.html'}),
      path('tes/', user_views.tes, name = 'tes'),
      path('teaching/', user_views.teaching, name = 'teaching'),
      path('evangelism/', user_views.evangelism, name = 'evangelism'),
      path('steward/', user_views.steward, name = 'steward'), 
      path('pay/', user_views.pay, name = 'pay'), 
      path('photo/', user_views.photo, name = 'photo'), 
      path("paystack", include(('paystack.urls','paystack'),namespace='paystack')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
