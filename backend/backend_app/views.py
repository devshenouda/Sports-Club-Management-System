from django.shortcuts import render, redirect, get_object_or_404 
from django.db.models import Sum
from collections import defaultdict
from .models import *
from .forms import *
from django.contrib.auth import logout

# =================================
from django.contrib.auth.views import LoginView


from django.contrib.auth.decorators import login_required, user_passes_test

# تحقق مما إذا كان المستخدم هو أدمن


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # بعد تسجيل الدخول، يمكن إعادة التوجيه إلى الصفحة الرئيسية
    else:
        form = AuthenticationForm()

    return render(request, 'pages/login.html', {'form': form})

def custom_logout(request):
    # يمكنك إضافة أي إجراء هنا قبل أو بعد تسجيل الخروج
    logout(request)  # تسجيل الخروج من الجلسة
    
    # إعادة التوجيه إلى صفحة تسجيل الدخول
    return redirect('login')


def is_admin(user):
    return user.is_superuser  # تحقق إذا كان المستخدم هو أدمن

# إضافة الزخارف على الفيوز
@login_required
@user_passes_test(is_admin)
def index(request):
    # ... الكود الحالي

    # =============================
    # هنا ممكن اشيل
    # =============================
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = TeamForm()
        addcat = CategoryForm(request.POST)
        if addcat.is_valid():
            addcat.save()
            addcat = CategoryForm()

    context = {
        'teams': Team.objects.all(),
        'category': Category.objects.all(),
        'form': TeamForm(),
        'formcat': CategoryForm(),
        'allmembers': Member.objects.all().count(),
        'active': Member.objects.filter(is_active='Active').count(),
        'revenues': Revenue.objects.all(),
        'expired': Member.objects.filter(is_active='Expired').count(),
        'expiring_soon': Member.objects.filter(is_active='Expired soon').count(),
    }
    return render(request, 'pages/index.html', context)


def teams(request):
    search = Team.objects.all()
    name = None
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            search = search.filter(team_name__icontains=name)

    context = {
        'teams': search,
        'category': Category.objects.all(),
        'form': TeamForm(),
        'formcat': CategoryForm(),
    }
    return render(request, 'pages/teams.html', context)


def update(request, id):
    team = get_object_or_404(Team, id=id)
    if request.method == 'POST':
        team_save = TeamForm(request.POST, request.FILES, instance=team)
        if team_save.is_valid():
            team_save.save()
        return redirect('index')
    else:
        team_save = TeamForm(instance=team)

    context = {
        'teams': Team.objects.all(),
        'category': Category.objects.all(),
        'formcat': CategoryForm(),
        'form': team_save,
    }
    return render(request, 'pages/update.html', context)


def delete(request, id):
    team_delete = get_object_or_404(Team, id=id)
    if request.method == 'POST':
        team_delete.delete()
        return redirect('index')
    return render(request, 'pages/delete.html', {'team': team_delete})


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = MemberForm()
    return render(request, 'pages/add_member.html', {'form': form})


def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'pages/member_detail.html', {'member': member})


def members_list(request):
    active_members = Member.objects.filter(is_active='Active')
    expired_members = Member.objects.filter(is_active='Expired')
    expiring_soon_members = Member.objects.filter(is_active='Expired Soon')

    context = {
        'teams': Team.objects.all(),
        'category': Category.objects.all(),
        'form': MemberForm(),
        'formcat': CategoryForm(),
        'members': Member.objects.all(),
    }
    return render(request, 'pages/members_list.html', context)


def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('members_list')
    return render(request, 'pages/delete_member.html', {'member': member})


def update_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member_form = MemberForm(request.POST, request.FILES, instance=member)
        if member_form.is_valid():
            member_form.save()
            return redirect('members_list')
    else:
        member_form = MemberForm(instance=member)

    context = {
        'member': member,
        'form': member_form,
    }
    return render(request, 'pages/update_member.html', context)


def revenue_add(request):
    if request.method == 'POST':
        form = RevenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('revenue_list')
    else:
        form = RevenueForm()

    return render(request, 'pages/add_revenue.html', {'form': form})


def revenue_detail(request, id):
    revenue = get_object_or_404(Revenue, id=id)
    return render(request, 'pages/revenue_detail.html', {'revenue': revenue})


def revenue_list(request):
    context = {
        'category': Category.objects.all(),
        'form': TeamForm(),
        'formcat': CategoryForm(),
        'members': Member.objects.all(),
        'revenues': Revenue.objects.all(),
    }
    return render(request, 'pages/revenue_list.html', context)


def update_revenue(request, id):
    revenue = get_object_or_404(Revenue, id=id)
    if request.method == 'POST':
        form = RevenueForm(request.POST, instance=revenue)
        if form.is_valid():
            form.save()
            return redirect('revenue_list')
    else:
        form = RevenueForm(instance=revenue)

    context = {
        'form': form,
        'revenue': revenue,
    }

    return render(request, 'pages/update_revenue.html', context)


def delete_revenue(request, id):
    revenue = get_object_or_404(Revenue, id=id)
    if request.method == 'POST':
        revenue.delete()
        return redirect('revenue_list')
    return render(request, 'pages/delete_revenue.html', {'revenue': revenue})



# expences views ======================== 
def expences_list(request):
    expenses = Expense.objects.all()
    return render(request, 'pages/expences_list.html', {'expenses': expenses})

def expences_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expences_list')
    else:
        form = ExpenseForm()
    return render(request, 'pages/expences_add.html', {'form': form})

def expences_remove(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expences_list')
    return render(request, 'pages/expences_delete.html', {'expense': expense})

def expences_update(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expences_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'pages/expences_update.html', {'form': form})

def expences_show(request, id):
    expense = get_object_or_404(Expense, id=id)
    return render(request, 'pages/expences_show.html', {'expense': expense})



def expences(request):
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    expense_categories = Expense.objects.values('category__name').annotate(amount=Sum('amount'))
    monthly_expenses = Expense.objects.values('date__month').annotate(amount=Sum('amount')).order_by('date__month')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    context = {
        'total_expenses': total_expenses,
        'expense_categories': expense_categories,
        'monthly_expenses': [expense['amount'] for expense in monthly_expenses],
        'months': months,
    }
    return render(request, 'pages/expences.html', context)

