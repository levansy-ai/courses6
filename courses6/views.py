from django.shortcuts import render
from .data import courses6
# Create your views here.
def courses_list(request):
    return render(request, 'list.html', {"items_course":courses6})

def course_detail(request, course_id):
    item_course = None
    for item in courses6:
        if item['id'] == course_id:
            item_course = item
            break

    return render(request, 'detail.html', {"items_course":courses6, "item_course":item_course})