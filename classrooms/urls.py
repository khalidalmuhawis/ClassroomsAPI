
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from classes import views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),


    path('login/', TokenObtainPairView.as_view(), name="api-login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('register/', api_views.Register.as_view(), name="api-register"),

    path('classroomsapi/', api_views.ClassroomList.as_view(), name="api-classroom-list"),
    path('classroomsapi/<int:classroom_id>/', api_views.ClassroomDetail.as_view(), name="api-classroom-detail"),


    path('classroomcreateapi/', api_views.ClassroomCreate.as_view(), name="api-classroom-create"),
    path('classroomupdateapi/<int:classroom_id>/', api_views.ClassroomUpdate.as_view(), name="api-classroom-update"),
    path('classroomcanceleapi/<int:classroom_id>/', api_views.ClassroomCancel.as_view(), name="api-classroom-delete"),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
