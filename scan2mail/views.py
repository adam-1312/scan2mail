from django.shortcuts import render
from .forms import InputForm
from django.http import JsonResponse
from .utils import generate_qr    
 
def home(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def process_qr(request):
    if request.method == "POST":
        to = request.POST.get("to", "")
        cc = request.POST.get("cc", "")
        bcc = request.POST.get("bcc", "")
        subject = request.POST.get("subject", "")
        body = request.POST.get("body", "")
        api_key = request.POST.get("apiKey", "")
        alias = request.POST.get("alias", "")
        
        link, qr = generate_qr(to, subject, body, api_key, cc, bcc, alias=alias)
        return JsonResponse({"link": link, "qr": qr})
    return JsonResponse({"error": "Invalid request"}, status=400)
