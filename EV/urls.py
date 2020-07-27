from django.contrib import admin
from django.urls import path
import Main.views
import Community.views
import Introduce.views
import Member.views
import Recommand.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.views.index, name='index'),
    path('login/', Member.views.login, name='login'),
    path('join/', Member.views.join, name='join'),
    path('login_pro/', Member.views.login_pro, name='login_pro'),
    path('join_pro/', Member.views.join_pro, name='join_pro'),
    path('community/', Community.views.community, name='community'),
    path('logout/', Member.views.logout, name='logout'),
    path('recommand/', Recommand.views.recommand, name='recommand'),
]
