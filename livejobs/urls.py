"""livejobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings # for 'media' folder setting purpose
from django.conf.urls.static import static # for 'media' folder setting purpose

import accounts.url

# django Main_project url.py

urlpatterns = [
    path('admin/', admin.site.urls),
    # home page
    path('',accounts.views.index,name='index_url'),
    path("unicorn/", include("django_unicorn.urls")),

    # accounts app main urls
    path('accounts/',include('accounts.url')),

    # recruiter app main urls
    path('recruiter/',include('recruiter.urls')),

    # candidate app main urls
    path('candidate/',include('candidate.urls')),

    # hr_admin app main urls
    path('hr_admin/',include('hr_admin.urls')),
    
]

# for 'media' folder setting purpose
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
