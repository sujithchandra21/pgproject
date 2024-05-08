from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import PG,Status_PG,Registration_PG
from django.contrib.auth.models import Group
from . forms import RegisterUser,PGModelForm,StatusPgModelForm,GroupForm,RegisterPGOwner
from . decorators import CheckGroup,CheckpgSearch


# Create your views here.
def entranceLogin(request):
    return render(request,'MainPage/entrance.html')

def humanLoginPage(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['password']

        validuser = authenticate(request,username=uname,password=pwd)
        print(validuser)
        if validuser != None:
            login(request,validuser)
            return redirect('searchpgurl') 
            #return render(request,'MainPage/humanLoginPage.html',{'msg':'login successfully'})
        else:
            return render(request,'MainPage/humanLoginPage.html',{'msg':'login failed'})

    return render(request,'MainPage/humanLoginPage.html')

def humanSignUpPage(request):
    emptyForm = RegisterUser()
    #emptyForm1 = GroupForm()
    f = Group.objects.all()
    #print(emptyForm1)
    if request.method == 'POST':
        dataForm = RegisterUser(request.POST)
        if dataForm.is_valid():
            user = dataForm.save()  # Save the user object
            group_id = request.POST.get('group')  # Get selected group ID from form data
            #print(group_id)
            group = Group.objects.get(pk=group_id)  # Get the group object by ID
            #print(group)
            user.groups.add(group)  # Add user to the group
            return redirect('humanloginurl')
        else:
            # Handle form validation errors
            return render(request, 'MainPage/humanSignUpPage.html', {'form': dataForm})
    return render(request,'MainPage/humanSignUpPage.html', {'form': emptyForm,'f':f})

def humanlogoutPage(request):
    logout(request)
    return redirect('humanloginurl')

def pgLoginPage(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['password']

        validuser = authenticate(request,username=uname,password=pwd)
        print(validuser)
        if validuser != None:
            login(request,validuser)
            return redirect('adminAcessRegisterpurl')
            #return render(request,'MainPage/humanLoginPage.html',{'msg':'login successfully'})
        else:
            return render(request,'MainPage/pgLoginPage.html',{'msg':'login failed'})

    return render(request,'MainPage/pgLoginPage.html')

def PGSignUpPage(request):
    emptyForm = RegisterPGOwner()
    #emptyForm1 = GroupForm()
    f = Group.objects.all()
    #print(emptyForm1)
    if request.method == 'POST':
        dataForm = RegisterPGOwner(request.POST)
        if dataForm.is_valid():
            user = dataForm.save()  # Save the user object
            group_id = request.POST.get('group')  # Get selected group ID from form data
            #print(group_id)
            group = Group.objects.get(pk=group_id)  # Get the group object by ID
            #print(group)
            user.groups.add(group)  # Add user to the group
            return redirect('pgdetailsurl')
            #return redirect('pgloginurl')
        else:
            # Handle form validation errors
            return render(request, 'MainPage/PGSignUpPage.html', {'form': dataForm})
    return render(request,'MainPage/PGSignUpPage.html', {'form': emptyForm,'f':f})

def pglogoutPage(request):
    logout(request)
    return redirect('pgloginurl')

def pgDetails(request):
    emptyForm = PGModelForm()
    if request.method == 'POST':
        dataForm = PGModelForm(request.POST)
        if dataForm.is_valid() == True:
            dataForm.save()
            #print(dataForm)
            #return render(request,'MainPage/pgdetail.html',{'form':emptyForm})
            return redirect('statusdetailsurl')
        else:
            return render(request,'MainPage/pgdetail.html',{'form':dataForm})

    return render(request,'MainPage/pgdetail.html',{'form':emptyForm})

def statusDetails(request):
    emptyForm = StatusPgModelForm()
    if request.method == 'POST':
        dataForm = StatusPgModelForm(request.POST,request.FILES)
        if dataForm.is_valid() == True:
            dataForm.save()
            #print(dataForm)
            return render(request,'MainPage/statusdetail.html',{'frm':emptyForm})
            #return redirect('pgloginurl')
        else:
            return render(request,'MainPage/statusdetail.html',{'frm':dataForm})

    return render(request,'MainPage/statusdetail.html',{'frm':emptyForm})

@CheckpgSearch
@login_required(login_url='humanloginurl')
def searchPG(request):
    total_details = Status_PG.objects.all()
    if request.method == 'POST':
        loc = request.POST['location']
        searching = PG.objects.filter(address=loc)
        #print(searching)
        if len(searching) > 0:
            l =  []
            for j in searching:
                obj = j.pg_code
                #print(obj)
                res = Status_PG.objects.filter(pg_id = obj)
                for k in res:
                    #print(k.sharing)
                    l.append(k)
            return render(request,'MainPage/searchpg.html',{'data':l,'myvar':1})
        # else:
        #     return render(request,'MainPage/searchpg.html',{'data':'please enter valid location'})
    return render(request,'MainPage/searchpg.html',{'empty':total_details,'myvar':0})


# def registerPG(request,pgno):
#     if request.method == 'POST':
#         rid = request.POST['registerid']
#         rname = request.POST['name']
#         remail = request.POST['email']
#         rmobile = request.POST['mobile']
#         obj = Status_PG.objects.get(id=pgno)
#         rshare = obj.sharing
#         rprice = obj.price
#         Registration_PG.objects.create(Registration_id=rid,Full_name=rname,Email=remail,Mobile_number=rmobile,sharing_person=rshare,price_person=rprice)
#         return render(request,'MainPage/registerpg.html')
#     return render(request,'MainPage/registerpg.html')

def selectPGImages(request,pgno):
    obj = Status_PG.objects.get(id=pgno)
    res = obj.images
    print(res)
    return render(request,'MainPage/selectpgimages.html',{'resp':obj})

@CheckGroup
def adminAccessRegisterpg(request):
    total_details = Registration_PG.objects.all()
    if len(total_details)>0:

        return render(request,'MainPage/adminaccesspg.html',{'res':total_details})
    return render(request,'MainPage/adminaccesspg.html')




def registerPG(request,pgno):
    obj = Status_PG.objects.get(id=pgno)
    rvcan = obj.vaccancies
    if rvcan > 0:
        if request.method == 'POST':
            rid = request.POST['registerid']
            rname = request.POST['name']
            remail = request.POST['email']
            rmobile = request.POST['mobile']
            obj = Status_PG.objects.get(id=pgno)
            rshare = obj.sharing
            rprice = obj.price
            rvcancy = rvcan - 1
            print(rvcancy)
            obj.vaccancies = rvcancy
            obj.save()
            # sobj = Status_PG(id=pgno,pg_id=pg,vaccancies = rvcancy)
            # sobj.save()
            Registration_PG.objects.create(Registration_id=rid,Full_name=rname,Email=remail,Mobile_number=rmobile,sharing_person=rshare,price_person=rprice)
            return render(request,'MainPage/registerpg.html')
    else:
        return redirect('searchpgurl')
    return render(request,'MainPage/registerpg.html')