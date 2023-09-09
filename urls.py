"""Cyber_security URL Configuration

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
from django.urls import path
from my_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contact/',views.contact, name='Contact'),
    path('Aboutus/',views.aboutus, name='Aboutus'),
    path('FAQ/',views.FAQ, name='FAQ'),
    path('Footer/',views.footer, name='Footer'),
    path('Forgetpassword/',views.forgetpassword, name='Forgetpassword'),
    path('Login/',views.login, name='Login'),
    path('Register/',views.register, name='Register'),
    path('Services/',views.services, name='Services'),
    path('Changepassword/',views.changepassword, name='Changepassword'),
    path('Help/',views.Help, name='Help'),
    path('Review/',views.review, name='Review'),
    path('Main/',views.main, name='Main'),
    path('Index/',views.index, name='Index'),
    path('Base/',views.base, name='Base'),
    path('Dashboard/',views.dashboard, name='Dashboard'),
    path('Allattacks/',views.allattacks, name='Allattacks'),
    path('Allthreats/',views.allthreats, name='Allthreats'),
    path('Allnews/',views.allnews, name='Allnews'),
    path('Alllawyers/',views.alllawyers, name='Alllawyers'),
    path('Allngos/',views.allngos, name='Allngos'),
    path('Allhelplines/',views.allhelplines, name='Allhelplines'),
    path('Allpolicestations/',views.allpolicestations, name='Allpolicestations'),
    path('Allacts/',views.allacts, name='Allacts'),
    path('Detaillawyer/<int:id>',views.detaillawyer, name='Detaillawyer'),
    path('Detailattack/<int:id>',views.detailattack, name='Detailattack'),
    path('Detailnews/<int:id>',views.detailnews, name='Detailnews'),
    path('Detailthreat/<int:id>',views.detailthreat, name='Detailthreat'),
    path('Alltips/',views.alltips, name='Alltips'),
    path('Allcrimes/',views.allcrimes, name="Allcrimes"),
    path('Detailcrimes/<int:id>',views.detailcrimes, name='Detailcrimes'),
    path('Profile/',views.profile, name="Profile"),
    path('Logout/',views.logout, name="Logout"),
    path('Allalerts/',views.allalerts, name="Allalerts"),
    path('Detailalert/<int:id>',views.detailalert, name='Detailalert'),
    path('Fullscan/',views.fullscan, name="Fullscan"),
    path('Quickscan/',views.quickscan, name="Quickscan"),
    path('Rangescan/',views.rangescan, name="Rangescan"),
    path('Portscan/',views.portscan, name="Portscan"),
    path('Filescan/',views.filescan, name="Filescan"),
    path('Filescanresult/',views.filescanresult, name="Filescanresult"),
    path('Editprofile/',views.editprofile, name="Editprofile"),
    path('AllDGPSuraksha/',views.alldgpsuraksha, name="AllDGPSuraksha"),
    path('Allsecurity_tips/',views.allsecurity_tips, name="Allsecurity_tips"),
    path('Security_tools/',views.security_tools, name="Security_tools"),
    path('Vulnerability/',views.vulnerability, name="Vulnerability"),
    path('Allblogs/',views.allblogs, name='Allblogs'),
    path('Detailblog/<int:id>',views.detailblog, name='Detailblog'),
    path('Detailvulnerability/<str:id>',views.detailvulnerability, name='Detailvulnerability'),

    path('Vulnerabilitysearch/',views.vulnerabilitysearch, name="Vulnerabilitysearch"),
    #path('Detailvulnerability/<int:did>',views.detailvulnerability, name='Detailvulnerability'),
    path('Portscanresult/',views.portscanresult, name="Portscanresult"),
    path('Quickscanresult/',views.quickscanresult, name="Quickscanresult"),
    path('Rangescanresult/',views.rangescanresult, name="Rangescanresult"),
    path('Fullscanresult/',views.fullscanresult, name="Fullscanresult"),
    path('Whoisscanning/',views.whoisscanning, name="Whoisscanning"),
    path('Whoisscanningresult/',views.whoisscanningresult, name="Whoisscanningresult"),
    path('Domainscan/',views.domainscan, name="Domainscan"),
    path('Domainresult/',views.domainresult, name="Domainresult"),
    path('Phishingdetection/',views.phishingdetection, name="Phishingdetection"),
    path('Phishingresult/',views.phishingresult, name="Phishingresult"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)