from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import hotel,department,employee
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection



# Create your views here.

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)

def Login(request):
    return render(request,'Login_page.html')

def Dashboard(request):

    dat = hotel.objects.values('Hotel_name').count()
    data = employee.objects.values('first_name').count()
    view = {
        "view": dat,
        "dat":data
    }
    print(view)


    return render(request,'dashboard.html',view)

def add_hotel(request):
    return render(request,'admin_hotelreg.html')

def hotels_fields(request):
    if request.method == 'POST' and request.FILES['myfile']:
        name = request.POST['name']
        print(name)
        star = request.POST['star']
        print(star)
        about = request.POST['about']
        print(about)
        address = request.POST['address']
        print(address)

        a = request.POST.getlist('facility')
        facility = ','.join(a)
        print(facility)
        latt = request.POST['latt']
        print(latt)
        contact = request.POST['contact']
        print(contact)
        email = request.POST['email']
        print(email)
        website = request.POST['website']
        print(website)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        user = hotel(Hotel_name=name, stars=star, description=about, address=address,facilities=facility, lattitude=latt, contact=contact,email=email,website=website,
                            pic=filename)
        user.save()


        return redirect('/User/hotels/')



def hotels(request):

    data = hotel.objects.all()
    view = {
        "view": data
    }
    print(view)
    return render(request, 'hotel_lists.html',view)

def hotel_update(request,id):
    print(id)

    data1 = hotel.objects.get(pk=id)
    field_value = getattr(data1, 'facilities')
    print(field_value)
    s=list(field_value.split(","))



    context = {
        'context': data1,
        'lan':s,


    }
    return render(request, 'update_hotels.html',context)



def hotel_updated(request):
    if request.method == 'POST' and request.FILES['myfile']:
        name = request.POST['name']
        print(name)
        uid = request.POST['uid']
        star = request.POST['star']
        print(star)
        about = request.POST['about']
        print(about)
        address = request.POST['address']
        print(address)

        a = request.POST.getlist('facility')
        facility = ','.join(a)
        print(facility)
        latt = request.POST['latt']
        print(latt)
        contact = request.POST['contact']
        print(contact)
        email = request.POST['email']
        print(email)
        website = request.POST['website']
        print(website)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        user = hotel.objects.filter(pk=uid).update(Hotel_name=name, stars=star, description=about, address=address,facilities=facility, lattitude=latt, contact=contact,email=email,website=website,
                            pic=filename)
        return redirect('/User/hotels/')



def hotel_delete(request,id):
    hotel.objects.get(pk=id).delete()

    return redirect('/User/hotels/')



def department_add(request):
    data = hotel.objects.all()
    view = {
        "view": data
    }
    print(view)
    return render(request,'department.html',view)


def department_adding(request):
    depart = request.POST['depart']
    print(depart)
    hotel = request.POST['hotel']
    print(hotel)
    user = department(department=depart, hotels_id_id=hotel)
    user.save()
    s = ''' <script>alert('Insertion completed successfully')</script>'''
    return redirect('/User/department_list/')


def department_list(request):
    data = department.objects.all().select_related()
    dep = {
        "dep": data
    }

    return render(request,'depart_lists.html',dep)


def department_update(request,id):

    request.session['id']=id
    data = department.objects.select_related('hotels_id').get(pk=id)


    datas = hotel.objects.all()
    viewz = {
        "view": datas,
        "dep": data,
    }
    print(viewz)

    return render(request, 'update_depart.html',viewz)


def department_updated(request):
    depart = request.POST['depart']
    print(depart)
    hotel = request.POST['hotel']
    print(hotel)
    uid = request.session['id']
    user = department.objects.filter(pk=uid).update(department=depart, hotels_id_id=hotel)
    s = ''' <script>alert('Insertion completed successfully')</script>'''
    return redirect('/User/department_list/')

def delete_depart(request,id):
    department.objects.get(pk=id).delete()

    return redirect('/User/department_list/')


def employee_(request):
    data = hotel.objects.all()
    data = {
        "data": data
    }

    return render(request, 'employee_add.html',data)


def empl(request):
    print("hello")


    print("pppp")
    id = request.POST['idd']
    print(id)

    data= serialize('json', department.objects.filter(hotels_id_id=id))
    print(data)


    return JsonResponse(data,safe=False)

def employee_add(request):
    if request.method == 'POST' and request.FILES['myfile']:
        name = request.POST['name']
        print(name)
        last = request.POST['last']

        hotel = request.POST['hotel']
        print(hotel)
        de = request.POST['depart']
        print("hiiii", de)
        job = request.POST['job']
        work_email = request.POST['work_email']
        work_mobi = request.POST['work_mobi']
        work_emi = request.POST['work_emi']
        gender = request.POST['gender']
        Marital = request.POST['Marital']
        date = request.POST['date']
        address = request.POST['address']
        mail = request.POST['mail']
        mobile = request.POST['mobile']
        username = request.POST['username']
        password = request.POST['password']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        user = employee(first_name=name,last_name=last,pic=filename,job=job,work_email=work_email,work_mobile=work_mobi,work_iemi=work_emi,gender=gender,
                        martial_status=Marital,dob=date,address=address,mail_id=mail,mobile=mobile,user_name=username,password=password,depart_id=de,hotels_id=hotel)
        user.save()
        return redirect('/User/employee_lists/')



def employee_lists(request):
    data = employee.objects.all()
    view = {
        "view": data
    }
    print(view)


    return render(request, 'employee_lists.html',view)

def employee_update(request,id):
    data = employee.objects.filter(pk=id)
    sp = hotel.objects.all()
    print(sp)
    dep = department.objects.all()
    print(dep)
    hotl = {
        "hotl": data,
        "sp": sp,
        "dep": dep

    }
    print(hotl)
    return render(request, 'update_employee.html',hotl)


def employee_updated(request):
    if request.method == 'POST' and request.FILES['myfile']:
        name = request.POST['name']
        print(name)
        uid = request.POST['uid']
        last = request.POST['last']

        hotel = request.POST['hotel']
        print(hotel)
        de = request.POST['depart']
        print("hiiii", de)
        job = request.POST['job']
        work_email = request.POST['work_email']
        work_mobi = request.POST['work_mobi']
        work_emi = request.POST['work_emi']
        gender = request.POST['gender']
        Marital = request.POST['Marital']
        date = request.POST['date']
        address = request.POST['address']
        mail = request.POST['mail']
        mobile = request.POST['mobile']
        username = request.POST['username']
        password = request.POST['password']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        user = employee.objects.filter(pk=uid).update(first_name=name,last_name=last,pic=filename,job=job,work_email=work_email,work_mobile=work_mobi,work_iemi=work_emi,gender=gender,
                        martial_status=Marital,dob=date,address=address,mail_id=mail,mobile=mobile,user_name=username,password=password,depart_id=de,hotels_id=hotel)

        return redirect('/User/employee_lists/')


def employee_delete(request,id):
    employee.objects.get(pk=id).delete()

    return redirect('/User/employee_lists/')

def search(request):
    print("pppp")
    id = request.POST['name']
    print(id)

    data = serialize('json', employee.objects.filter(first_name__contains = id))
    print("emp",data)

    return JsonResponse(data, safe=False)