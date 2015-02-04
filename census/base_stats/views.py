from django.shortcuts import render
from django.http import HttpResponse
from models import CensusLearnSql
import json


def home(request):

    context = {} 
    
    # get field names  
    fields = CensusLearnSql._meta.get_all_field_names()
    fields.remove('age')
    fields.remove('id')
    
    # make a user friendly copy of the field names
    fields_pretty = []

    for field in fields:

        field_pretty = field.replace("_"," ").title()
        fields_pretty.append(field_pretty)
    
    fields = zip(fields,fields_pretty)

    context['variables'] = fields

    return render(request,'stats.html',context)



def stats(request,variable):
    
    print "User requested stats on " + variable

    # stats = { (value,age,count), ... }
    stats = get_base_stats(variable)
    
    # sort stats from high to low count
    #TODO return as dict, and use order by to sort in browser?
    #stats.sort(key=lambda tup: tup[2], reverse=True)
    
    # return data as JSON, without rendering
    return HttpResponse(json.dumps(stats), content_type="application/json")


def get_base_stats(field): 

    variables = dict()

    values = CensusLearnSql.objects.values('age',field)
   
    for value in values:
        
        # skip this entry if no age is provided
        # (typically that means the value is also None, 
        # but it may be more accurate to keep two separate counts
        # one for the number of entries, another to compute the average)
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
       
        #variables[key] = value[0]/value[1],value[1]
        #var_list.append(key, value[0]/value[1], value[1]))

        entry = {} 
        entry["name"] = key
        entry["count"] = value[1]
        entry["age"] = value[0]/value[1]
        
        var_list.append(entry) 
    
    return var_list

## get all fields....
#    # get the distinct values for each field
#    for x,field in enumerate(fields):
#    
#        if x == MAX and DEBUG: break   
#     
#        print str(x+1) + '/' + str(len(fields)) + '\t' + field 
#        
#        # stats = { (value,age,count), ... }
#        stats = get_base_stats(field)
#        
#        # sort stats from high to low count
#        stats.sort(key=lambda tup: tup[2], reverse=True)
#        
#        context[field] = stats 
