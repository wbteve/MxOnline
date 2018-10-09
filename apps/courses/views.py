from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Course


from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class CourseListView(View):
    @staticmethod
    def get(request):
        all_courses = Course.objects.all().order_by("-add_time")
        # 热门
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]
        #排序
        sort = request.GET.get("sort","")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        #对课程进行分页
        try:
            page = request.GET.get("page",1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses,6,request=request)
        courses = p.page(page)

        return render(request, "course-list.html", {
            "all_course": courses,
            "sort": sort,
            "hot_courses": hot_courses,
            # "search_keywords": search_keywords
        })

class CourseDetailView(View):
    @staticmethod
    def get(request):
        all_courses = Course.objects.all()
        return render(request, "course-list.html", {
            "all_course": all_courses,
            # "sort": sort,
            # "hot_courses": hot_courses,
            # "search_keywords": search_keywords
        })

class CourseInfoView(View):
    @staticmethod
    def get(request):
        all_courses = Course.objects.all()
        return render(request, "course-list.html", {
            "all_course": all_courses,
            # "sort": sort,
            # "hot_courses": hot_courses,
            # "search_keywords": search_keywords
        })

class CommentsView(View):
    @staticmethod
    def get(request):
        all_courses = Course.objects.all()
        return render(request, "course-list.html", {
            "all_course": all_courses,
            # "sort": sort,
            # "hot_courses": hot_courses,
            # "search_keywords": search_keywords
        })

class AddCommentsView(View):
    @staticmethod
    def get(request):
        all_courses = Course.objects.all()
        return render(request, "course-list.html", {
            "all_course": all_courses,
            # "sort": sort,
            # "hot_courses": hot_courses,
            # "search_keywords": search_keywords
        })

class VideoPlayView(View):
    @staticmethod
    def get(request):
        all_courses = Course.objects.all()
        return render(request, "course-list.html", {
            "all_course": all_courses,
            # "sort": sort,
            # "hot_courses": hot_courses,
            # "search_keywords": search_keywords
        })