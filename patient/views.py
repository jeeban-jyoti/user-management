from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import MYSQL

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        profile_picture = request.POST.get('profile_picture','')
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
        address = request.POST.get('address','')
        print(first_name, last_name, profile_picture, username, email, password, confirm_password, address)


        if password != confirm_password:
            print("hello world")
            return render(request, 'signup_patient.html')
        conn, db = MYSQL.mysqlCursor()
        conn.execute(f'use project')
        conn.execute('show tables')
        print(conn.fetchall())
        conn.execute(f'insert into users values ("{first_name}", "{last_name}", "{profile_picture}", "{username}", "{email}", "{password}", "{address}", "patient", false);')
        db.commit()
        db.close()
        return redirect('/patient/login')

    return render(request, 'signup_patient.html')

@csrf_exempt
def login(request):
    response = render(request, 'login_patient.html')
    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        print(email, password)

        conn, db = MYSQL.mysqlCursor()
        conn.execute('use project')
        conn.execute(f'select password from users where email="{email}"')
        if password == conn.fetchall()[0][0]:
            conn.execute(f'update users set access_granted=true where email="{email}"')
            response = redirect(f'/patient/dashboard?email={email}')
        

    return response

def dashboard(request):
    conn, db = MYSQL.mysqlCursor()
    email = request.GET.get('email', default='')
    conn.execute(f'select * from users where email="{email}"')
    data = conn.fetchall()[0]
    return render(request, 'patient_dashboard.html', {"first_name":data[0], "last_name": data[1],"email":data[4], "username": data[3], "address":data[6], "role":data[7] })
