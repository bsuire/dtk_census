from django.shortcuts import render
from django.http import HttpResponse
from models import CensusLearnSql
import json

################################################################
# home(request): 
# ----- RETURNS UI (html) with dropdown select button which is 
# ----- dynamically populated with table's field names
################################################################

def home(request):

    context = {} 
    
    # get field names (query for DB's meta)  
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

    # render calls templating engine before sending back html
    return render(request,'stats.html',context)


################################################################
# stats(request,field): 
# ----- Acts as an API for AngularJS http/data requests.
# ----- Gets all the field_value,age pairs from the database.
# ----- Computes the number of occurences of each value,
# ----- as well as the average age of people corresponding.
# ----- RETURNS a JSON containing a list of dictionaries 
# ----- with keys: field_value, count, average_age.
################################################################

def stats(request,field): # note: fields and variables are used interchangeably 

    print "User requested stats on " + field

    values_aggreg = dict()
    
    values = CensusLearnSql.objects.values('age',field)
   
    # iterate through query results to aggregate count and age
    for value in values:
        
        # skip this entry if no age is provided
        # (typically that means the variable's value is also None,
        # but I have not verified this assumption)
        if value['age'] is None:
            continue
        
        # variable is already in dictionary. Update...
        if value[field] in values_aggreg:
            
            (age_sum,count) = values_aggreg[value[field]]
            age_sum += value['age'] 
            count += 1
            
        # new entry. Initialize...
        else:
            age_sum = value['age']
            count = 1
        
        values_aggreg[value[field]] = age_sum,count
    

    # aggregation complete, now compute averages
    
    var_list = []
    
    for key, value in values_aggreg.iteritems():
       
        # saving as dictionary so that fields can be accessed as objects in JS
        entry = {}   
        entry["name"] = key
        entry["count"] = value[1]
        entry["age"] = value[0]/value[1]
        
        var_list.append(entry) 
    
    # return data to client as JSON 
    return HttpResponse(json.dumps(var_list), content_type="application/json")

