from app.models import Category,Product

def getAllCategory():
    return Category.objects.all()

