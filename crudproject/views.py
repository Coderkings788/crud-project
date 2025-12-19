from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from crud.models import rform


def homepage(request):
    return render(request,'Home.html')
def form(request):
#     return render(request,'form.html')
# def rviews(request):
    if request.method =='POST':
        fname=(request.POST['first_name'])
        lname=(request.POST['last_name'])
        dob=(request.POST['dob'])
        gender=(request.POST['gender'])
        image=request.FILES.get('image')
        form=rform(fname=fname,lname=lname,dob=dob,gender=gender,file=image)
        form.save()
        return redirect("table")
    return render(request,'Form.html')
def formdata(request):
    form=rform.objects.all()
    datas={
        'formdata': form
    }
    return render(request,'table.html',datas)

def edit(request,id):
    editdata=rform.objects.get(id=id)
    if request.method=='POST':
        fname=(request.POST['first_name'])
        lname=(request.POST['last_name'])
        dob=(request.POST['dob']) 
        gender=(request.POST['gender'])
        editdata.fname = fname
        editdata.lname = lname
        editdata.dob = dob
        editdata.gender = gender
        # editdata.file = 
        data=rform(fname=fname,lname=lname,dob=dob,gender=gender)
        editdata.save()
        return HttpResponseRedirect('/table?result=update successful')
    else:
        return render(request,'Edit.html',{'id':id,'fname':editdata.fname,'lname':editdata.lname,'dob':editdata.dob.strftime('%Y-%m-%d'),'gender':editdata.gender})


def delete(request,id):
    det=rform.objects.get(id=id)
    det.delete()
    return HttpResponseRedirect('/table?result=update successful')