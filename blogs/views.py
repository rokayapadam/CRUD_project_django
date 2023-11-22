from django.shortcuts import render,HttpResponseRedirect
from .forms import BlogsFOrm
from .models import User
# Create your views here.

# create add and show dat 
def add_view(request):
    if request.method == 'POST':
        fm = BlogsFOrm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = BlogsFOrm()

    else:
        fm = BlogsFOrm()
    stud = User.objects.all()
    return render(request, 'blogs/addshow.html', {'form':fm, 'stu':stud}) 


# update function 
def update_view(request, id ):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = BlogsFOrm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=BlogsFOrm(instance=pi)
    return render(request, 'blogs/updateshow.html', {'form':fm})





# delete function 
def delete_view(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')