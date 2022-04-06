from django.shortcuts import render,redirect

from accounts.models import * #importing all account app models
from recruiter.models import Recruiter
from candidate.models import Candidate

# importing password encryptor
from django.contrib.auth.hashers import make_password, check_password

# importing django login athentications
from django.contrib.auth import authenticate, login, logout

# /////// for login purpose //////////////
from django.contrib.auth.decorators import login_required

# Create your views here.

# home page logic
def index(request):
    return render(request,'index.html',{})

# recruiter signup logic
def recruiter_signup(request):

    # main if condition
    # user already logged in area (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')

        # conditon for login authorization (checking if it is - Admin, recruiter, candidate )
        auth_user=User.objects.get(username__contains=request.user)
        auth_user_extend=Extend_usermodel.objects.get(user_id=auth_user.id)
        print(auth_user_extend.role)

        # admin login condition
        if(auth_user_extend.role =='admin'):
            print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
            print('admin is logged in')
            # return render(request,'admin/dashboard.html',{})
            return redirect('hr_admin.dashboard')       

        # # recruiter login condition
        elif(auth_user_extend.role =='recruiter'):
            print('success rrrrrrrrrrrrrrrrrrrrrrr')
            print('recruiter is logged in')
            # return render(request,'recruiter/dashboard.html',{})
            return redirect('recruiter.dashboard')

        # # candidate login condition
        elif(auth_user_extend.role=='candidate'):
            print('success ccccccccccccccccccccccc')
            print('candidate is logged in')
            # return render(request,'candidate/dashboard.html',{})
            return redirect('candidate.dashboard')

        else:
            print('login failed')
            context={'static_mail':email,'user_error':'Invalid Email & Password'}
            return render(request,'login.html',context)


    else: #main else /////////////////

        # user not logged in area (case 2)

        if request.method=='POST':
            company_name=request.POST.get('company_name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_psd=request.POST.get('confirm_psd')
            checkbox_agree=request.POST.get('agree')
            print(company_name)
            print(email)
            print(password)
            print(confirm_psd)
            print(checkbox_agree)

            if(company_name=='' or email== '' or password=='' or confirm_psd==''):
                print('No value')
                context={'static_username':company_name,'static_mail':email,'user_error':'Please enter valid info...'}
                return render(request,'recruiter_reg.html',context)

            elif(len(password)<6):
                print('Password length too short.')
                context={'static_username':company_name,'static_mail':email,'user_error':'Password length is too short. Require a minimum password length of 6–10 characters.'}
                return render(request,'recruiter_reg.html',context)

            elif(not password==confirm_psd):
                print('Password Missmatch')
                context={'static_username':company_name,'static_mail':email,'user_error':'Password Missmatch'}
                return render(request,'recruiter_reg.html',context)

            elif(not checkbox_agree== 'agree'):
                print('Please agree terms and conditions')
                context={'static_username':company_name,'static_mail':email,'user_error':'Please agree terms and conditions'}
                return render(request,'recruiter_reg.html',context)

            elif User.objects.filter(username=email).exists():
                print('User already exist View')
                context={'static_username':company_name,'static_mail':email,'user_error':'User already exist...'}
                return render(request,'recruiter_reg.html',context)

            else:

                #making password encryption for login purpose(becz django form weak password is not allowed in authentication)
                passEncrypted = make_password(password)

                # auth_user table
                auth_user=User()
                auth_user.username=email
                auth_user.password=passEncrypted # saved password in encrypted format
                auth_user.save()
                print('auth_user table saved as recruiter')

                # User table new field
                usernew_table=Extend_usermodel()
                usernew_table.user=auth_user
                usernew_table.role='recruiter'
                usernew_table.save()
                print('User extend table saved')

                # recruiter table
                recruiter_table=Recruiter()
                recruiter_table.user=auth_user # (table object saving) assigning recruiter table (foriegnkey) <== in auth_user (primarykey) (Get complete table)
                recruiter_table.company_name=company_name
                recruiter_table.email=email
                recruiter_table.agreement=checkbox_agree
                recruiter_table.save()
                print('recruiter table saved')
                return render(request,'login.html',{'reg_success': 'Successfully registered, Please login'})

    return render(request,'recruiter_reg.html',{})



# candidate signup logic
def candidate_signup(request):
    # main if condition
    # user already logged in area (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')

        # conditon for login authorization (checking if it is - Admin, recruiter, candidate )
        auth_user=User.objects.get(username__contains=request.user)
        auth_user_extend=Extend_usermodel.objects.get(user_id=auth_user.id)
        print(auth_user_extend.role)

        # admin login condition
        if(auth_user_extend.role =='admin'):
            print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
            print('admin is logged in')
            # return render(request,'admin/dashboard.html',{})
            return redirect('hr_admin.dashboard')       

        # # recruiter login condition
        elif(auth_user_extend.role =='recruiter'):
            print('success rrrrrrrrrrrrrrrrrrrrrrr')
            print('recruiter is logged in')
            # return render(request,'recruiter/dashboard.html',{})
            return redirect('recruiter.dashboard')

        # # candidate login condition
        elif(auth_user_extend.role=='candidate'):
            print('success ccccccccccccccccccccccc')
            print('candidate is logged in')
            # return render(request,'candidate/dashboard.html',{})
            return redirect('candidate.dashboard')

        else:
            print('login failed')
            context={'static_mail':email,'user_error':'Invalid Email & Password'}
            return render(request,'login.html',context)


    else: #main else /////////////////

        # user not logged in area (case 2)
        if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_psd=request.POST.get('confirm_psd')
            checkbox_agree=request.POST.get('agree')
            print(username)
            print(email)
            print(password)
            print(confirm_psd)
            print(checkbox_agree)

            if(username=='' or email== '' or password=='' or confirm_psd==''):
                print('No value')
                context={'static_username':username,'static_mail':email,'user_error':'Please enter valid info...'}
                return render(request,'candidate_reg.html',context)

            elif(len(password)<6):
                print('Password length too short.')
                context={'static_username':username,'static_mail':email,'user_error':'Password length is too short. Require a minimum password length of 6–10 characters.'}
                return render(request,'candidate_reg.html',context)

            elif(not password==confirm_psd):
                print('Password Missmatch')
                context={'static_username':username,'static_mail':email,'user_error':'password Missmatch'}
                return render(request,'candidate_reg.html',context)
            
            elif(not checkbox_agree== 'agree'):
                print('Please agree terms and conditions')
                context={'static_username':username,'static_mail':email,'user_error':'Please agree terms and conditions'}
                return render(request,'candidate_reg.html',context)

            elif(not email.endswith('@gmail.com')):
                    print('Email format wrong')
                    context={'static_username':username,'static_mail':email,'user_error':'Please enter a valid email'}
                    return render(request,'candidate_reg.html',context)

            elif User.objects.filter(username=email).exists():
                print('User already exist View')
                context={'static_username':username,'static_mail':email,'user_error':'User already exist...'}
                return render(request,'candidate_reg.html',context)

            else:


                #making password encryption for login purpose(becz django form weak password is not allowed in authentication)
                passEncrypted = make_password(password)

                auth_user=User()
                auth_user.username=email
                auth_user.password=passEncrypted # saved password in encrypted format
                # auth_user.role='recruiter'
                auth_user.save()
                print('auth_user table saved as candidate')

                # User table new field
                usernew_table=Extend_usermodel()
                usernew_table.user=auth_user
                usernew_table.role='candidate'
                usernew_table.save()
                print('User extend table saved')

                candidate_table=Candidate()
                candidate_table.user_id=auth_user # (table object saving) assigning recruiter table (foriegnkey) <== in auth_user (primarykey) (Get complete table)
                candidate_table.name=username
                candidate_table.email=email
                candidate_table.agreement=checkbox_agree
                candidate_table.save()
                print('candidate table saved')
                return render(request,'login.html',{'reg_success': 'Successfully registered, Please login'})

    return render(request,'candidate_reg.html',{})


# login logic
def loginpage(request):
    # main if condition
    # user already logged in area (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')

        # conditon for login authorization (checking if it is - Admin, recruiter, candidate )
        auth_user=User.objects.get(username__contains=request.user)
        auth_user_extend=Extend_usermodel.objects.get(user_id=auth_user.id)
        print(auth_user_extend.role)

        # admin login condition
        if(auth_user_extend.role =='admin'):
            print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
            print('admin is logged in')
            # return render(request,'admin/dashboard.html',{})
            return redirect('hr_admin.dashboard')       

        # # recruiter login condition
        elif(auth_user_extend.role =='recruiter'):
            print('success rrrrrrrrrrrrrrrrrrrrrrr')
            print('recruiter is logged in')
            # return render(request,'recruiter/dashboard.html',{})
            return redirect('recruiter.dashboard')

        # # candidate login condition
        elif(auth_user_extend.role=='candidate'):
            print('success ccccccccccccccccccccccc')
            print('candidate is logged in')
            # return render(request,'candidate/dashboard.html',{})
            return redirect('candidate.dashboard')

        else:
            print(user,'user')
            print('login failed')
            context={'static_mail':email,'user_error':'Invalid Email & Password'}
            return render(request,'login.html',context)


    else: #main else /////////////////

        # user not logged in area (case 2)

        if request.method=='POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            print(email)
            print(password)

            if(email== '' or password==''):
                print('No value')
                context={'static_mail':email,'user_error':'Please enter valid info...'}
                return render(request,'login.html',context)

            else:

                user =authenticate(request, username=email, password=password) # check the user is valid
                print(user)

                if user is not None:
                    login(request, user) #login is hold uservalue(request&user), and added to django_section database
                    print(type(user),user)
                    print('User Login succesfull')

                    # conditon for login authorization (checking if it is - Admin, recruiter, candidate )
                    auth_user=User.objects.get(username__contains=user)
                    auth_user_extend=Extend_usermodel.objects.get(user_id=auth_user.id)
                    print(auth_user_extend.role)

                    # admin login condition
                    if(auth_user_extend.role =='admin'):
                        print('success aaaaaaaaaaaaaaaaaaaaaaaaa')
                        print('admin is logged in')
                        # return render(request,'admin/dashboard.html',{})
                        return redirect('hr_admin.dashboard')       

                    # # recruiter login condition
                    elif(auth_user_extend.role =='recruiter'):
                        print('success rrrrrrrrrrrrrrrrrrrrrrr')
                        print('recruiter is logged in')
                        # return render(request,'recruiter/dashboard.html',{})
                        return redirect('recruiter.dashboard')

                    # # candidate login condition
                    elif(auth_user_extend.role=='candidate'):
                        print('success ccccccccccccccccccccccc')
                        print('candidate is logged in')
                        # return render(request,'candidate/dashboard.html',{})
                        return redirect('candidate.dashboard')

                else:
                    print(user,'user')
                    print('login failed')
                    context={'static_mail':email,'user_error':'Invalid Email & Password'}
                    return render(request,'login.html',context)

        # else:
        #     print('invalid email & password')

    return render(request,'login.html',{})
    
def logoutpage(request):
    logout(request)
    return render(request,'login.html')


# # HR admin logic
# @login_required(login_url="/accounts/login")
# def hr_admin(request):
#     return render(request,'hr_admin/profile.html',{})

# # recruiter logic
# @login_required(login_url="/accounts/login")
# def recruiter_profile(request):
#     return render(request,'recruiter/profile.html',{})

# # candidate logic
# @login_required(login_url="/accounts/login")
# def candidate_profile(request):
#     return render(request,'candidate/profile.html',{})
