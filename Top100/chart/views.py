from django.shortcuts import render
from .models import Blockchain
from getAddress import address
from getBalance import balance


def index(request):
    for i in range(100):
        Blockchain.objects.create(address=address[i], balance=balance[i])
    results = Blockchain.objects.all()
    context = {'results': results}
    return render(request, 'chart/index.html', context)

def deleteDB():
    Blockchain.objects.all().delete()

deleteDB()
