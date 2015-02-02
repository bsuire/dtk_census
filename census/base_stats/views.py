from django.shortcuts import render
from models import CensusLearnSql
# Create your views here.

DEBUG = False
MAX = 8

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
    fields.remove('id') 

    # get the distinct values for each field
    for x,field in enumerate(fields):
    
        if x == MAX and DEBUG: break   
     
        print str(x+1) + '/' + str(len(fields)) + '\t' + field 
        
        # stats = { (value,age,count), ... }
        stats = get_base_stats(field)
        
        # sort stats from high to low count
        stats.sort(key=lambda tup: tup[2], reverse=True)
        
        context[field] = stats 
    
    return render(request,'stats.html',context)



def get_base_stats(field): 

    variables = dict()

    values = CensusLearnSql.objects.values('age',field)
   
    for value in values:

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
    
    var_list = []
    
    for key, value in variables.iteritems():
        
        var_list.append((key, value[0]/value[1], value[1]))

        #variables[key] = value[0]/value[1],value[1]
        #print key,variables[key]
    
    return var_list 

def sort_stats(field,stats):
    # stats = {(value,age,count_max), ... , (value,age,count_min)}
    #data.sort(key=lambda tup: tup[2])  # sorts in place 
    pass






