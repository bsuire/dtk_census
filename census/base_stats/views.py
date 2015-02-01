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
    # TODO : keep values in memory? (cache)

    context = {} 
    
    # get field names  
    fields = CensusLearnSql._meta.get_all_field_names()
    fields.remove('age')
    
    # get the distinct values for each field
    for field in fields:

        variables = dict()

        values = CensusLearnSql.objects.values('age',field).order_by()
        #print values
       
        for value in values:
            #print value

            if value['age'] is None:
                continue
            
            # variable is already in dictionary
            if value[field] in variables:
                
                (average,count) = variables[value[field]]
                average += value['age']
                count += 1
                
            # new entry
            else:
                average = value['age']
                count = 1
            
            variables[value[field]] = average,count

        
        # aggregation complete, now compute averages
        for key, value in variables.iteritems():
            
            variables[key] = value[0]/value[1],value[1]
            print key,variables[key]
       
            
    c = variables

    data=str(c)
    
    context = {'data': data} 
    return render(request,'stats.html',context)

