from django.urls import path
from . import views

urlpatterns = [
    path('entrance/',views.entranceLogin,name="entranceurl"),
    path('humanlogin/',views.humanLoginPage,name="humanloginurl"),
    path('humansignup/',views.humanSignUpPage, name="humansignupurl"),
    path('humanlogout/',views.humanlogoutPage,name='humanlogouturl'),
    path('pgdetails/',views.pgDetails, name="pgdetailsurl"),
    path('statusdetails/',views.statusDetails, name="statusdetailsurl"),
    path('searchpg/',views.searchPG,name="searchpgurl"),
    path('registerpg/<int:pgno>',views.registerPG,name="registerpgurl"),
    path('accessdetails/',views.adminAccessRegisterpg,name='adminAcessRegisterpurl'),
    path('selectpgimagesurl/<int:pgno>',views.selectPGImages,name="selectpgimagesurl"),
    path('pglogin/',views.pgLoginPage,name="pgloginurl"),
    path('pgsignup/',views.PGSignUpPage,name="pgsignupurl"),
    path('pglogout/',views.pglogoutPage,name='pglogouturl'),
]