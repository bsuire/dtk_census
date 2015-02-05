from django.shortcuts import render
from django.http import HttpResponse
from models import CensusLearnSql
import json

MAX_NB_VALUES = 100

################################################################
# home(request): 
# ----- RETURNS UI (html) with dropdown select button which is 
# ----- dynamically populated with table's field names

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
# ----- Computes the count and average age for each value.
# ----- RETURNS a JSON containing the name, count, & average_age 
# ----- for the 100 most frequent value, sorted in decreasing order
# ----- + the nb of values and rows clipped

def stats(request,field): # note: fields and variables are used interchangeably 

    print "User requested stats on " + field

    values_aggreg = dict()
    
    values = CensusLearnSql.objects.values('age',field)

    nb_rows_valid = 0

    # iterate through query results to aggregate count and age
    for value in values:
        
        # skip this entry if no age is provided
        if value['age'] is None:
            continue
        
        nb_rows_valid += 1
        
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
       
        # saving in dictionary so that fields can be accessed as objects in JS
        entry = {}   
        entry["name"] = key
        entry["count"] = value[1]
        entry["age"] = 10 * value[0] / value[1]
        
        var_list.append(entry) 
    
    # sort entries by decreasing count 
    var_list.sort(key=lambda k: k["count"], reverse=True) 
    
    # get number of values clipped out (doens't include values of type None, which were filtered out earlier)
    nb_values_hidden = clip(var_list)
    
    # get number of rows clipped out (excluding rows of None type)
    nb_rows_shown = aggregate_count(var_list)
    nb_rows_hidden = nb_rows_valid - nb_rows_shown
    
    # prepare response
    meta = {}
    meta["values_clipped"] = nb_values_hidden
    meta["rows_clipped"] = nb_rows_hidden

    response_data = {} 
    response_data["meta"] = meta
    response_data["data"] = var_list

    # return data to client as JSON 
    return HttpResponse(json.dumps(response_data), content_type="application/json")


################################################################
#            Helper functions
################################################################

# clip(list_rows): 
# ----- Clips list of values if len(list) > 100
# ----- RETURNS the number of values that were clipped

def clip(list_values):
    
    nb_values = len(list_values)
    
    if nb_values <= MAX_NB_VALUES:
        return 0

    else:
        del list_values[ MAX_NB_VALUES : ]
        return nb_values - MAX_NB_VALUES

# aggregate_count(list_rows): 
# ----- RETURNS the total count value for the entire list

def aggregate_count(list_values):
    
    count_total = 0
    
    for val in list_values:
        count_total += val["count"]

    return count_total

