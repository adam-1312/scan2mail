from django.shortcuts import render
from .forms import InputForm
from django.http import JsonResponse
from .utils import generate_qr    
 
def hello_geeks(request) :
 
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def process_qr(request):
    if request.method == "POST":
        to = request.POST.get("to", "")
        subject = request.POST.get("subject", "")
        body = request.POST.get("body", "")
        
        link, qr = generate_qr(to, subject, body)
        return JsonResponse({"link": link, "qr": qr})
    return JsonResponse({"error": "Invalid request"}, status=400)
