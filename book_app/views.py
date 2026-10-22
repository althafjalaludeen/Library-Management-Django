from django.shortcuts import render

from django.views.generic import View

from django.http import JsonResponse


class GoodMorningView(View):
    def get(self, request):
        data = {
            "message" : "Good Morning"
        }
        return JsonResponse(data)

class LibraryView(View):
    def get(self, request):
        data = {
            "Library": "Central Library",
            "Location": "Idukki",
            "Status": "Open"
        }
        return JsonResponse(data)

class BookView(View):
    def get(self, request):
        data = {
            "Book_Name": "Django for Beginners",
            "Author": "William S. Vincent",
            "Price": 650
        }
        return JsonResponse(data)

class StudentView(View):
    def get(self, request):
        data = {
            "Name": "Anu",
            "Course": "Python Django",
            "Batch": "June 2026",
            "Institution": "Luminar Technolab"
        }
        return JsonResponse(data)

class BooksView(View):
    def get(self, request):
        data = {
            "Books": [
                "Python",
                "Django",
                "Java",
                "React",
                "MySQL"
            ]
        }
        return JsonResponse(data)
class EmployeeView(View):
    def get(self, request):
        data = {
            "id":"123",
            "name":"Althaf Jalaludeen",
            "place":"Thiruvalla",
            "designation":"Developer",
            "Contact": "8089293596",
            "Experience":"1 yr",
            "Qualification":"BTech",
        }
        return JsonResponse(data)