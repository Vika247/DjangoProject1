from django.shortcuts import render, HttpResponse, Http404
from .models import Item
def home(request):
    #return HttpResponse('Hello')
    return render(request, "index.html")

def about(request):
    context={
        "name": "Виктория",
        "surename": "Артамонова",
        "oname": "Васильевна",
        "phone": "123456789",
        "email": "1234@mail.com",

    }
    return render(request, "about.html", context)

items = [
    {"id":1, "name": "Кросовки adibas", "quantity": 5},
    {"id":2, "name": "Куртка кожаная", "quantity": 2},
    {"id":3, "name": "Coca-Cola 1 литр", "quantity": 12},
    {"id":4, "name": "Кортофель фри", "quantity": 0},
    {"id":5, "name": "Кепка", "quantity": 124},
]

def items(request):
    #context ={
    #    'items': items
    #}
    #MOD = [f.name for f in Item._meta._get_fields()]
    #itemss = [ list(i.values()) for i in list(Item.objects.all().values())]
    itemss = Item.objects.all().values()
    return render(request, "items.html", {'items': itemss
        #"MOD" : MOD
    })
    #return render(request, "items.html", context)

    #item_result = "ol"
    #for item in items:
        #item_result +="<li>"+f"<a href = '/item/{item['id']}'>"+item['name']+"</a>"+"</li>"
    #items_result+=</ol>
    #return HttpResponse(items_result)

def item_page(requst, id):
    #context = {
    #    'items': items,
    #    'id': id,
    #}
    #return render(requst, "item.html", context)
    ###itemss = Item.objects.values()
    itemm =  Item.objects.get(id = id)
    return render(requst, "item.html", {#"items": itemss,
                                        "itemm": itemm
    })