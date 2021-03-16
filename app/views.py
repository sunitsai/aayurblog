from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *

# Create your views here.
def AdminIndexPage(request):
    if 'username' in request.session:
        all_cat = Category.objects.all()
        all_post = Post.objects.all()
        count_cat = len(all_cat)
        count_post = len(all_post)
        return render(request,"app/admin/index.html",{'all_cat':all_cat,'all_post':all_post,'count_cat': count_cat, 'count_post': count_post})
    else:
        return redirect('loginpage')

def Loginpage(request):
    return render(request,"app/admin/login.html")

def Addcat(request):
    if 'username' in request.session:
        print("ADDCAT*****************")
        if request.method == "POST":
            c_name = request.POST['cname']
            newcategory = Category.objects.create(c_name=c_name)
            print("************DATA INSERTED*********")
            return HttpResponseRedirect(reverse('allcat'))
    else:
        return redirect('loginpage')
        
def PostAllCat(request):
    if 'username' in request.session:
        all_cat = Category.objects.all()
        return render(request,"app/admin/categories.html",{'all_cat':all_cat})
    else:
        return redirect('loginpage')

def EditCatPage(request,pk):
    if 'username' in request.session:
        ecat = Category.objects.get(pk=pk)
        return render(request,"app/admin/editcat.html",{'ecat':ecat})
    else:
        return redirect('loginpage')

def UpdatePostCat(request,pk):
    if 'username' in request.session:
        ucat = Category.objects.get(pk=pk)
        ucat.c_name = request.POST['cname']
        ucat.save()
        return HttpResponseRedirect(reverse('postallcat'))
    else:
        return redirect('loginpage')
def DeleteCat(request,pk):
    if 'username' in request.session:
        dcat = Category.objects.get(pk=pk)
        dcat.delete()
        return HttpResponseRedirect(reverse('postallcat'))
    else:
        return redirect('loginpage')
def AllCategory(request):
    if 'username' in request.session:
        all_cat = Category.objects.all()
        return redirect('admin')
    else:
        return redirect('loginpage')
def SortCategory(request,pk):
    all_cat = Category.objects.get(id=pk)
    print("cattttttttt",all_cat)
    post_cat = Post.objects.all().filter(cat_id=all_cat)
    return render(request,"app/blog-3.html",{'key2':post_cat})
def Addpost(request):
    if 'username' in request.session:
        c_id = request.POST['category']
        cid = Category.objects.get(id=c_id)
        title = request.POST['title']
        shortcontent = request.POST['shortcontent']
        content = request.POST['editor1']
        keyword = request.POST['keyword']
        author = request.POST['author']
        blogimg = request.FILES['image']
        authorimg = request.FILES['authorimg']

        newpost = Post.objects.create(cat_id=cid,Title=title,shortcontent=shortcontent,content=content,keyword=keyword,author=author,image=blogimg,authorimg=authorimg)
        return render(request,"app/admin/index.html")
    else:
        return redirect('loginpage')
def AllPost(request):
    if 'username' in request.session:
        all_post = Post.objects.all()
        return render(request,"app/admin/posts.html",{'all_post':all_post})
    else:
        return redirect('loginpage')

def EditPage(request,pk):
    if 'username' in request.session:
        epost = Post.objects.get(pk=pk)
        UpdateCat(request)
        return render(request,"app/admin/details.html",{'key1':epost})
    else:
        return redirect('loginpage')    

def UpdateCat(request):
    if 'username' in request.session:
        print("+++++++++++++UDATE CAT++++++++++++++")
        all_cat = Category.objects.all()
        for i in all_cat:
            print("***********************",i)
        return render(request,"app/admin/details.html",{'all_cat':all_cat})
    else:
        return redirect('loginpage')
def UpdatePost(request,pk):
    if 'username' in request.session:
        if request.method=="POST":
            udata = Post.objects.get(pk=pk)
            udata.Title = request.POST['title']
            udata.shortcontent = request.POST['shortcontent']
            udata.content = request.POST['editor1']
            udata.keyword = request.POST['keyword']
            udata.author = request.POST['author']
            udata.image = request.FILES['image']
            udata.authorimg = request.FILES['authorimg']
            udata.save()
            return HttpResponseRedirect(reverse('allpost'))
    else:
        return redirect('loginpage')

def DeletePost(request,pk):
    if 'username' in request.session:
        dpost = Post.objects.get(pk=pk)
        dpost.delete()
        return HttpResponseRedirect(reverse('allpost'))
    else:
        return redirect('loginpage')
def Adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username=="admin" and password=="admin":
            request.session['username'] = username
            return HttpResponseRedirect(reverse('admin'))
        else:
            message = "Username or Password doesnot match"
            return render(request,"app/admin/login.html")

    else:
        return redirect('loginpage')

def AdminLogout(request):
    if 'username' in request.session:
        del request.session['username']
    return HttpResponseRedirect(reverse('loginpage'))




############################################## Website ############################################




def Indexpage(request):
    return render(request,"app/index.html")
def WhatisAyurveda(request):
    return render(request,"app/whatisAyurveda.html")

def BecomeSellerPage(request):
    return render(request,"app/becomeseller.html")

def BlogPage(request):
    all_blog = Post.objects.all()
    all_cat = Category.objects.all()
    return render(request,"app/blog-3.html",{'key2':all_blog,'key3':all_cat})


def AboutUs(request):
    return render(request,"app/about-element-1.html")


def BlogDetails(request,pk):
    all_cat = Category.objects.all()
    bpost = Post.objects.get(pk=pk)
    return render(request,"app/blog-details.html",{'key4':bpost,'key5':all_cat})



def InsertSeller(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    bname = request.POST['bname']

    newseller = Seller.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Businessname=bname)
    message = "Details Submited"
    return render(request,"app/becomeseller.html",{'msg':message})


def Postcomment(request,pk):
    if request.method=="POST":
        p_id = request.POST['pid']
        pid = Post.objects.get(id=p_id)
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        comment = request.POST['message']
        newcomment = PostComment.objects.create(post_id=pid,Firstname=fname,Lastname=lname,Email=email,Contact=contact,comment=comment)
        message = "Your Comment is Successfully Submitted"
        all_cat = Category.objects.all()    
        bpost = Post.objects.get(pk=pk)
        return render(request,"app/blog-details.html",{'key4':bpost,'key5':all_cat,'msg':message})

