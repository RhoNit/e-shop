from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customers import Customer
from django.views import View



class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('firstname')
        last_name = post_data.get('lastname')
        phone = post_data.get('phone')
        email = post_data.get('email')
        password = post_data.get('password')

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'password': password
        }

        error_msg = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        # validation
        error_msg = self.validate_customer(customer)

        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'values': values,
                'error': error_msg
            }
            return render(request, 'signup.html', data)

    # validate user
    def validate_customer(self, customer):
        error_msg = None

        if not customer.first_name:
            error_msg = 'First Name is required!'
        elif len(customer.first_name) < 3:
            error_msg = 'First Name must be at least 3 letters long'
        elif not customer.last_name:
            error_msg = 'Last Name is required!'
        elif len(customer.last_name) < 3:
            error_msg = 'Last Name must be at least 3 letters long'
        elif not customer.phone:
            error_msg = 'Phone Number is required...'
        elif len(customer.phone) < 10:
            error_msg = 'Phone Number must be at least 10 digits long'
        elif not customer.email:
            error_msg = 'Please enter your Email ID'
        elif not customer.password:
            error_msg = 'C"\'"mon man !!! You forgot to enter your profile password'
        elif len(customer.password) < 6:
            error_msg = 'Password must be at least 6 characters long'
        elif customer.does_email_exist():
            error_msg = 'Email already exists'

        return error_msg