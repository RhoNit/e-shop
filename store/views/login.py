from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customers import Customer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Customer.get_customer_by_email(email)
        err_msg = None
        if user:
            flag = check_password(password, user.password)
            if flag:
#                request.session['customer_id'] = user.id
#                request.session['email'] = user.email
                return redirect('homepage')
            else:
                err_msg = 'Email or Password is invalid'
        else:
            err_msg = 'Email or Password is invalid'

        return render(request, 'login.html', {'error': err_msg})


# def logout(request):
#    request.session.clear()
#    return redirect('login')