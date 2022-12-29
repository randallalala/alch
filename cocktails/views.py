from django.shortcuts import render, HttpResponse


cocktails = [
  {
    'name': 'long island tea',
    'ingredients': 'tea',
    'notes': 'ded',
    'alcohol_content': '99%'
  },
  {
    'name': 'bloody mary',
    'ingredients': 'tomato',
    'notes': 'ded',
    'alcohol_content': '55%'
  }
]


def home(request):
    context = {
        'cocktails': cocktails
    }
    return render(request, "cocktails/home.html", context)

def about(request):
    return render(request, "cocktails/about.html",)
  
  # {'name':'about us page'}