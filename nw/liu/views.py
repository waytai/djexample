from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article
from .models import Colors, Child, Clothes

# Create your views here.

def stcl(request):
    color1 = Colors.objects.create(colors='red')
    #color1.save()

    color2 = Colors.objects.create(colors='blue')
    #color2.save()

    child1 = Child.objects.create(name='zhangsan')
    child1.favor.add(color1, color2)
    child1.save()

    child2 = Child.objects.create(name='zhangtwo')
    #child2.save()

    child3 = Child.objects.create(name='zhangthree')
    #child3.save()

    color1.child_set.add(child2, child3)
    color1.save()

    clothe1 = Clothes.objects.create(color=color1, description='maoyi')
    clothe2 = Clothes.objects.create(color=color2, description='maoyi')
    color1.clothes_set.create(description='yuyi')
    color1.clothes_set.add(clothe2)

    return HttpResponse('ok')


def pbat(request):
    p1 = Publication(title='The Python Journal')
    p1.save()
    p2 = Publication(title='Science News')
    p2.save()
    p3 = Publication(title='Science Weekly')
    p3.save()
    a1 = Article(headline='Django lets you build Web apps easily')
    a1.save()
    a1.publications.add(p1,p2,p3)
    a1.save()

    aa1 = Article(headline='aa1')
    aa1.save()
    aa2 = Article(headline='aa2')
    aa2.save()
    p1.article_set.add(aa1, aa2)
    p1.save()
    return HttpResponse('ok')
