from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth.decorators import user_passes_test
from .models import Document
from .forms import DocumentUploadForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import user_passes_test

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        return render(request, 'registration/register.html', {'form': form})
@login_required
def dashboard(request):
    profile = request.user.userprofile  # предполагается, что профиль уже существует
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile, user=request.user)
    return render(request, 'dashboard.html', {'form': form})





def document_list(request):
    # Выбираем все документы, сортированные от новейшего к старейшему
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'documents/document_list.html', {'documents': documents})



# Проверка: доступно только суперпользователям
def superuser_required(user):
    return user.is_superuser

@user_passes_test(superuser_required)
def document_upload(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.uploaded_by = request.user
            doc.save()
            return redirect('document_list')
    else:
        form = DocumentUploadForm()
    return render(request, 'documents/document_upload.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'documents/document_confirm_delete.html', {'document': document})


