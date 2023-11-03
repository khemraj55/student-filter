
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('getstudents/', views.get_students, name='get_students'),
    path('getstudents/<int:class_name>/', views.get_students, name='get_students_filtered'),
    path('createstudent/', views.create_student, name='create_student'),
    path('display_students/', views.display_students, name='display_students'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)