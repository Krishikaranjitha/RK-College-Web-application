from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.Login,name="login"),
    path('result/<int:pk>/',views.Result,name="student_Result"),
    path('st_db',views.Stud_DB,name="biodata"),
    path('cse',views.CSE,name="cse"),
    path('eee',views.EEE,name="eee"),
    path('ece',views.ECE,name="ece"),
    path('civil',views.CIVIL,name="civil"),
    path('mech',views.Mech,name="mech"),
    path('About',views.About,name="about"),
    path('Colfees',views.College_Fees,name="colfees"),
    path('Hosfees',views.Hostel_Fees,name="hosfees"),
    path('Gallery',views.Gallery,name="gallery"),
    path('contact',views.Contact,name="contact"),
    path('admission',views.Admission,name="admission"),
    path('Delete/<int:id>',views.DELETE,name="Delete"),
    path('Update/<int:id>',views.UPDATE,name="Update"),
    # path('admission/update/<int:id>/', views.UPDATE, name='UPDATE'),
    path('View/<int:id>',views.View,name="View"),
    path('CSE',views.CSE_dept,name='cs_dep'),
    path('EEE',views.EEE_dept,name='ee_dep'),
    path('ECE',views.ECE_dept,name='ec_dep'),
    path('Civil',views.Civil_dept,name='ce_dep'),
    path('Mech',views.Mech_dept,name='me_dep'),
    path('ad',views.RE,name="ad"),
    
]


    