from django.shortcuts import render

# Create your views here.
def templates(request):
	return render(request, "html/index.html")
