from django.shortcuts import render,redirect
from .forms import SignUpForm,EmployeeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

# Create your views here.
def SignUp(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            return redirect('login')
        else:
            print('Invalid data')
            return render(request,'BowserApp/sign_up.html',locals())
    return render(request,'BowserApp/sign_up.html',locals())

@login_required
def home_page(request):
    return render(request,'BowserApp/home_page.html')

@login_required
def add_emp_view(request):
    form = EmployeeForm()
    if request.method=='POST':
        form = EmployeeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    return render(request,'BowserApp/forms.html',locals())

@login_required
def Emp_list_view(request):
    emp_list = Employee.objects.all()
    # paginator = Paginator(emp_list,10)
    # page_number = request.GET('page')
    # try:
    #     emp_list = paginator.page(page_number)
    # except PageNotAnInteger:
    #     emp_list = paginator.page(1)
    # except EmptyPage:
    #     emp_list = paginator.page(paginator.num_pages)
    return render(request,'BowserApp/emp_list.html',locals())

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'BowserApp/emp_detail.html'

    def get_context_data(self,**kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        return context

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('emp_list')

class EmployeeUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Employee
    fields = '__all__'
    sucess_message = "Recond Successfully Updated!"
    #success_url = reverse_lazy('emp_list')

    def get_form(self):
        form = super(EmployeeUpdateView, self).get_form()
        form.fields['emp_id'].widget = widgets.Textarea(attrs={'rows':1})
        form.fields['emp_first_name'].widget = widgets.Textarea(attrs={'rows':1})
        form.fields['emp_last_name'].widget = widgets.Textarea(attrs={'rows':1})
        form.fields['emp_date_of_birth'].widget = widgets.DateInput(attrs={'type':'date'})
        form.fields['emp_address1'].widget = widgets.Textarea(attrs={'rows':2})
        form.fields['emp_address2'].widget = widgets.Textarea(attrs={'rows':2})
        form.fields['emp_zip_code'].widget = widgets.Textarea(attrs={'rows':1})
        form.fields['emp_city'].widget = widgets.Textarea(attrs={'rows':1})
        form.fields['emp_mobile_no'].widget = widgets.Textarea(attrs={'rows':1})
        return form
