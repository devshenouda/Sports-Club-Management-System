from django.db import models
import datetime



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Team(models.Model):
    STATUS_CHOICES = [
        ('Full team', 'Full team'),
        ('Available team', 'Available team'),
    ]
    
    team_name = models.CharField(max_length=50)
    captain = models.CharField(max_length=50)  # Corrected 'captin' to 'captain'
    team_photo = models.ImageField(upload_to='imgs', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    players_no = models.IntegerField(default=0)
    def __str__(self):
        return self.team_name

# member model
class Member(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Expired soon', 'Expired soon'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    join_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# new starts ========================



# revenue model
class Revenue(models.Model):
    TYPE_CHOICES = [
        ('Subscription', 'Subscription'),
        ('Product Sale', 'Product Sale'),
    ]

    revenue_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # لتخزين المبلغ
    date = models.DateField(default=datetime.date.today)  # لتخزين تاريخ العملية
    description = models.TextField(null=True, blank=True)  # وصف للعملية (اختياري)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)  # إذا كانت العملية مرتبطة بعضو
    product_name = models.CharField(max_length=100, null=True, blank=True)  # إذا كانت العملية مرتبطة بمنتج معين (اختياري)
    quantity = models.IntegerField()  # كمية المنتج إذا كانت عملية بيع منتجات
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # إجمالي الإيرادات
    def __str__(self):
        return f"{self.revenue_type} - {self.amount} on {self.date}"




# product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)  # الكمية المتاحة من المنتج

    def __str__(self):
        return self.name


# subscription model
class Subscription(models.Model):
    # أنواع الاشتراكات (مثل اشتراك شهري أو سنوي)
    SUBSCRIPTION_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)  # ربط الاشتراك بعضو
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # المبلغ المدفوع للاشتراك
    subscription_type = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES)  # نوع الاشتراك (شهري أو سنوي)
    start_date = models.DateField(default=datetime.date.today)  # تاريخ بدء الاشتراك
    end_date = models.DateField()  # تاريخ نهاية الاشتراك
    is_active = models.BooleanField(default=True)  # حالة الاشتراك (مفعل أم لا)
    
    def __str__(self):
        return f"Subscription for {self.member} ({self.subscription_type})"
    
    # دالة لحساب تاريخ انتهاء الاشتراك بناءً على نوع الاشتراك
    def calculate_end_date(self):
        if self.subscription_type == 'Monthly':
            return self.start_date.replace(month=self.start_date.month + 1)  # إضافة شهر واحد
        elif self.subscription_type == 'Yearly':
            return self.start_date.replace(year=self.start_date.year + 1)  # إضافة سنة واحدة
        return self.start_date


# expense model
class Expense(models.Model):
    TYPE_CHOICES = [
        ('Rent', 'Rent'),
        ('Utilities', 'Utilities'),
        ('Salaries', 'Salaries'),
        ('Other', 'Other'),
    ]

    expense_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses' , null=True, blank=True) 

    def __str__(self):
        return f"{self.expense_type} - {self.amount} on {self.date}"





