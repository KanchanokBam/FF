from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import SignUpForm 
import random

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ทำการล็อกอินผู้ใช้ที่สมัครสำเร็จ
            messages.success(request, 'Your account has been created successfully!')  # แสดงข้อความสำเร็จ
            return redirect('/')  # ไปที่หน้าแรก
        else:
            messages.error(request, 'There was an error in your signup form. Please try again.')  # แสดงข้อความเมื่อเกิดข้อผิดพลาด
    else:
        form = SignUpForm()  # ฟอร์มเปล่า
    
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # เปลี่ยน 'next-page' เป็น URL ของหน้าหลังจากเข้าสู่ระบบ
            else:
                messages.error(request, 'error')
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})


@login_required(login_url='/signin/')
def page1(request):
    return render(request, 'home.html')

MENU_ITEMS = [
    {"name": "Spaghetti Carbonara", "type": "Main Course", "description": "Classic Italian pasta with creamy sauce.", "price": "200 THB"},
    {"name": "Tom Yum Goong", "type": "Soup", "description": "Spicy and sour Thai soup with shrimp.", "price": "150 THB"},
    {"name": "Caesar Salad", "type": "Appetizer", "description": "Fresh romaine lettuce with Caesar dressing.", "price": "120 THB"},
    {"name": "Mango Sticky Rice", "type": "Dessert", "description": "Sweet mango served with sticky rice and coconut milk.", "price": "100 THB"},
    {"name": "Green Curry Chicken", "type": "Main Course", "description": "Thai green curry with chicken and vegetables.", "price": "180 THB"},
]

@login_required
def random_menu(request):
    # เลือกเมนูแบบสุ่ม
    random_dish = random.choice(MENU_ITEMS)
    return render(request, 'random.html', {'dish': random_dish})


def logout_view(request):
    logout(request)  # ฟังก์ชัน Logout จาก Django
    return redirect('signin')  # หลัง Logout ให้เปลี่ยนเส้นทางไปที่หน้า Login

