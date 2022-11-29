from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseForbidden
def main(request):
    return render(request, "main.html")

def base(request):
    return render(request, 'base.html')