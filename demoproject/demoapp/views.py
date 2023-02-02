from django.shortcuts import render

def about(request):
    about_content = {'about': "Little Lemon is a family-owned\
                    Mediterranean restaurant, focused on traditional\
                    recipes served with a modern twist.\
                    The chefs draw inspiration from Italian,\
                    Greek, and Turkish culture and have a menu\
                    of 12–15 items that they rotate seasonally.\
                    The restaurant has a rustic and relaxed atmosphere\
                    with moderate prices, making it a popular place for a\
                    meal any time of the day."} 

    return render(request, 'about.html', about_content)


def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')