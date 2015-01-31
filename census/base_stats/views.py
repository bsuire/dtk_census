from django.shortcuts import render
from models import CensusLearnSql
# Create your views here.

def stats(request):
    
    # read from DB, compute all counts/averages, and organize

    # variable 
    #         \____ val 1 = { count, avg} 
    #          \___ val 2
    #           \__ val 3
    #   
    # TODO : keep valeus in memory? (cache)

    c  = CensusLearnSql.objects.values('class_of_worker').order_by('age').distinct()
    
    data=str(c)
    
    context = {'data': data} 
    return render(request,'stats.html',context)

