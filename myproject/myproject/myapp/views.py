from django.shortcuts import render

# Create your views here.
#from django.template.loader import render_to_string
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
import MySQLdb
from books.models import Publisher,Dreamreal, Online
#import codecs
def index(request):
	return HttpResponse("Index page")
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def test(request, id):
    return HttpResponse("test is is  %s." % id)
def testValue(request, value):
    return HttpResponse("test is is  %s." % value)

def helloHtml(request):
     today = datetime.datetime.now().date()
     #return render(request, "C:/Users/AGL/python37/myproject/myproject/myapp/hello.html", {"today" : today})
     return render(request, "hello.html", {"today" : today})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now 
    return HttpResponse(html)

def current_datetime2(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def template(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)

# def readTemplate(request):

#    today = datetime.datetime.now().date()
#     # Simple way of using templates from the filesystem.
#     # This is BAD because it doesn't account for missing files!
#     # \Users\AGL\python37\myproject\myproject\myapp\hello.html
#     #C:/Users/AGL/python37/myproject/myproject/myapp/hello.html
#     #fp = open('hello.html','r')
#     fp=open("C:/Users/AGL/python37/myproject/myproject/myapp/hello.html")
#     t = Template(fp.read())
#     fp.close()
#     html = t.render(Context({"today" : today}))
#     return HttpResponse(html)

def includeTemplate(request):
	today=datetime.datetime.now().date()
	return render(request,'templates/mypage.html',{"current_section":today})

def book_list(request):
	db = MySQLdb.connect(user='python37_usr', db='python37',  passwd='python37_db', host='localhost')
	cursor = db.cursor()
	cursor.execute('SELECT name FROM books ORDER BY name')
	names = [row[0] for row in cursor.fetchall()]
	db.close()
	return render(request, 'book_list.html', {'names': names })

def crudops(request):
   #Creating an entry
   
   publisher = Publisher(
     name='Apress', address='2855 Telegraph Avenue',
     city='Berkeley', state_province='CA', country='U.S.A.',
     website='http://www.apress.com/'
   )
   publisher.save()
   
   #Read ALL entries
   objects = Publisher.objects.all()
   res ='Printing all Publisher entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   # #Read a specific entry:
   # sorex = Publisher.objects.get(name = "Apress1")
   # res += 'Printing One entry <br>'
   # res += sorex.name
   
   #Delete an entry
   #res += '<br> Deleting an entry <br>'
  # sorex.delete()
   
   #Update
   publisher = Publisher(
     name='Apress1', address='2855 Telegraph Avenue',
     city='Berkeley', state_province='CA', country='U.S.A.',
     website='http://www.apress.com/'
   )
   
   publisher.save()
   res += 'Updating entry<br>'
   
   publisher = Publisher.objects.get(name = 'Apress1')
   publisher.name = 'thierry'
   publisher.save()
   Publisher.objects.filter(id=27).update(name='Apress Publishing')
   Publisher.objects.all().update(country='USA')

   return HttpResponse(res)

def datamanipulation(request):
   res = ''
   
   #Filtering data:
   qs = Publisher.objects.filter(name = "Apress")
   res += "Found : %s results<br>"%len(qs)
   
   #Ordering results
   qs = Publisher.objects.order_by("name")
   
   for elt in qs:
      res += elt.name + ', '+elt.address+ '<br>' 
   return HttpResponse(res)

def linkingModel(request):
     dr1 = Dreamreal()
     dr1.website = 'company1.com'
     dr1.name = 'company1'
     dr1.mail = 'contact@company1'
     dr1.phonenumber = '12345'
     dr1.save()
     dr2 = Dreamreal()
     dr1.website = 'company2.com'
     dr2.website = 'company2.com'
     dr2.name = 'company2'
     dr2.mail = 'contact@company2'
     dr2.phonenumber = '56789'
     dr2.save()
     # Now some hosted domains
     on1 = Online()
     on1.company = dr1
     on1.domain = "site1.com"
     on2 = Online()
     on2.company = dr1
     on2.domain = "site2.com"
     on3 = Online()
     on3.domain = "site3.com"
     dr2 = Dreamreal.objects.all()[2]
     on3.company = dr2
     on1.save()
     on2.save()
     on3.save()








