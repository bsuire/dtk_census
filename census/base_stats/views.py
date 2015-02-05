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

    nb_rows_valid = 0

    # iterate through query results to aggregate count and age
    for value in values:
        
        # skip this entry if no age is provided
        # (typically that means the variable's value is also None,
        # but I have not verified this assumption)
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
       
        # saving as dictionary so that fields can be accessed as objects in JS
        entry = {}   
        entry["name"] = key
        entry["count"] = value[1]
        entry["age"] = value[0]/value[1]
        
        var_list.append(entry) 
    
    # sort entries by decreasing count 
    var_list.sort(key=lambda k: k["count"], reverse=True) 
    
    # get number of values clipped out (doens't include values of type None, which were filtered out earlier)
    nb_values_hidden = clip(var_list)
    
    # get number of rows clipped out (excluding rows of None type)
    nb_rows_shown = aggregate_count(var_list)
    nb_rows_hidden = nb_rows_valid - nb_rows_shown
    
    meta = {}
    meta["values_clipped"] = nb_values_hidden
    meta["rows_clipped"] = nb_rows_hidden

    print "Nb of values that were clipped out: " + str(nb_values_hidden)
    print "Nb of rows that were clipped out: " + str(nb_rows_hidden)
    print "Total number of VALID rows: " + str(nb_rows_valid)
    print "Sanity check: nb_shown + nb_hidden = ? " + str(nb_rows_shown + nb_rows_hidden)
    
    response_data = {} 
    response_data["meta"] = meta
    response_data["data"] = var_list

    # return data to client as JSON 
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def clip(list_rows):
    
    nb_rows = len(list_rows)
    
    if nb_rows <= 100:
        return 0

    else:
        del list_rows[100:]
        return nb_rows - 100


def aggregate_count(list_rows):
    
    count_total = 0
    
    for row in list_rows:
        count_total += row["count"]

    return count_total








