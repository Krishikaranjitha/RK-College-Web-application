from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import REG_FORM, LoginForm
from .models import *

def home(request):
    return render(request,'Home.html')

 
def Login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            register_number=form.cleaned_data['register_number']
            date_of_birth=form.cleaned_data['date_of_birth']
            try:
                student = St_Registration.objects.get(Reg_number=register_number,DOB=date_of_birth)
                return redirect('student_Result', pk=student.pk)
            
            except St_Registration.DoesNotExist:
                form.add_error(None, 'Invalid register number or date of birth')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
       
    return render(request, 'login.html', {'form': form})
    
def Result(request,pk):
    student=get_object_or_404(St_Registration,pk=pk)
    return render(request,'result.html',{'student': student})

def Stud_DB(request):
    M=St_Registration.objects.all()
    return render(request,'biodata.html',{"data":M})

def CSE(request):
    return render(request,'dep/cse.html')
def ECE(request):
    return render(request,'dep/ece.html')
def EEE(request):
    return render(request,'dep/eee.html')
def CIVIL(request):
    return render(request,'dep/civil.html')
def Mech(request):
    return render(request,'dep/mech.html')
def About(request):
    return render(request,'Contact/About.html')
def Contact(request):
    return render(request,'Contact/contact.html')

def College_Fees(request):
    m=Col_Fees.objects.all()
    return render(request,'Contact/colfees.html',{'data':m})

def Hostel_Fees(request):
    m=Hos_Fees.objects.all()
    return render(request,'Contact/hosfees.html',{'data':m})

def Gallery(request):
    gal=gallery.objects.all()
    return render(request,'Contact/Gallery.html',{'data':gal})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import REG_FORM

def Admission(request):
    if request.method == 'POST':
        form = REG_FORM(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('/admission')
        else:
            messages.error(request, 'Error in registration. Please correct the errors below.')
    else:
        form = REG_FORM()
    
    return render(request, 'Contact/admission.html', {'form': form})
    # context={}
    # if request.method=="POST":
    #     name=request.POST['name']
    #     fname=request.POST['fname']
    #     dob=request.POST['dob']
    #     age=request.POST['age']
    #     address=request.POST['address']
    #     reg_num=request.POST['reg_num']
    #     bgroup=request.POST['bgroup']
    #     gender=request.POST['gender']
    #     dept=request.POST['dept']
    #     image=request.FILES.get('image')
    #     if name==''or fname=='' or dob=='' or age=='' or address=='' or reg_num=='' or bgroup=='' or gender=='' or dept=='' :
    #         context['error']="Fields cannot be Empty"
    #         return render(request,'Contact/admission.html',context)
    #     else:
    #             M=St_Registration.objects.create(Name=name,Fathers_name=fname,DOB=dob,Age=age,Address=address,Reg_number=reg_num,Gender=gender,Blood_Group=bgroup,Department=dept,image=image)
    #             M.save()
    #             context['success']="Registered Successfully"
    #             return render(request,'Contact/admission.html',context)
    # return render(request,'Contact/admission.html',context)

def DELETE(request,id):
    student=St_Registration.objects.get(id=id)
    student.delete()
    return redirect('/st_db')
    # return HttpResponse("Deleted")
    
def UPDATE(request,id):
    admission = get_object_or_404(St_Registration, id=id)
    if request.method == 'POST':
        form = REG_FORM(request.POST, request.FILES, instance=admission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect('biodata')  # or redirect to another view
        else:
            messages.error(request, 'Error in updating. Please correct the errors below.')
    else:
        form =REG_FORM(instance=admission)
    return render(request, 'update.html', {'form': form})

    # student=St_Registration.objects.get(id=id) 
    # if request.method=="POST":
    #     name=request.POST['name']
    #     fname=request.POST['fname']
    #     dob=request.POST['dob']
    #     age=request.POST['age']
    #     address=request.POST['address']
    #     reg_num=request.POST['reg_num']
    #     bgroup=request.POST['bgroup']
    #     gender=request.POST['gender']
    #     dept=request.POST['dept']
    #     image=request.FILES.get('photo')
        
    #     student.Name=name
    #     student.Fathers_name=fname
    #     student.DOB=dob
    #     student.Age=age
    #     student.Address=address
    #     student.Reg_number=reg_num
    #     student.Blood_Group=bgroup
    #     student.Gender=gender
    #     student.Department=dept
    #     student.image=image
    #     student.save()
    #     return redirect('biodata')
    # return render(request,'update.html',{'student':student})

def View(request,id):
    m=St_Registration.objects.filter(id=id).values()
    return render(request,'view.html',{'data':m})

def CSE_dept(request):
    context={}
    Department='CSE'
    student=St_Registration.objects.filter(Department=Department)
    context['data']=student
    return render(request,'cs.html',context)

def Mech_dept(request):
    context={}
    Department='ME'
    student=St_Registration.objects.filter(Department=Department)
    context['data']=student
    return render(request,'me.html',context)

def ECE_dept(request):
    context={}
    Department='ECE'
    student=St_Registration.objects.filter(Department=Department)
    context['data']=student
    return render(request,'ec.html',context)

def EEE_dept(request):
    context={}
    Department='EEE'
    student=St_Registration.objects.filter(Department=Department)
    context['data']=student
    return render(request,'ee.html',context)

def Civil_dept(request):
    context={}
    Department='CE'
    student=St_Registration.objects.filter(Department=Department)
    context['data']=student
    return render(request,'ce.html',context)

def RE(request):  
    form=REG_FORM()
    return render(request,'s_biodata.html',{'form':form})
    # if request.method=="POST":
    #     if for
