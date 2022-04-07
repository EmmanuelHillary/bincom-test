from django.shortcuts import render

def poll_results(request):
    return render(request, "poll_results.html")

def lga_results(request):
    return render(request, "lga_results.html")