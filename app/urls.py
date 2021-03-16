from django.urls import path,include
from . import views
urlpatterns = [

    ############################# WEBSITE URLS ########################################
    
    path("",views.Indexpage,name="index"),
    path("becomerseller/",views.BecomeSellerPage,name="becomesellerpage"),
    path("blogpage/",views.BlogPage,name="blogpage"),
    path("aboutus/",views.AboutUs,name="aboutus"),
    path("blogdetails/<int:pk>",views.BlogDetails,name="blogdetails"),
    path("sellersubmit/",views.InsertSeller,name="insert"),
    path("comment/<int:pk>",views.Postcomment,name="comment"),
    path("whatisAyurveda/",views.WhatisAyurveda,name="ayurveda"),
    







    ####################################### ADMIN URLS #################################
    path("adminindex/",views.AdminIndexPage,name="admin"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("logout/",views.AdminLogout,name="logout"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("updatepost/<int:pk>",views.UpdatePost,name="udpatepost"),
    path("deletePost<int:pk>",views.DeletePost,name="deletepost"),
    path("postallcat/",views.PostAllCat,name="postallcat"),
    path("editcategories/<int:pk>",views.EditCatPage,name="editcat"),
    path("updateCategories/<int:pk>",views.UpdatePostCat,name="updatecat"),
    path("deleteCategories/<int:pk>",views.DeleteCat,name="deletecat"),
    path("addcat/",views.Addcat,name="addcat"),
    path("addpost/",views.Addpost,name="addpost"),
    path("allcat/",views.AllCategory,name="allcat"),
    path("allpost/",views.AllPost,name="allpost"),
    path("adminlogin/",views.Adminlogin,name="adminlogin"),
    path("sortcategories/<int:pk>",views.SortCategory,name="sortcat"),
]
