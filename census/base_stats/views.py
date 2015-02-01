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

    # get field names  
    fields = CensusLearnSql._meta.get_all_field_names()
    fields.remove('age')
    
    # get the distinct values for each field
    for field in fields:
        f = field

        values = CensusLearnSql.objects.values(field).order_by().distinct()
        
        # get count and average age for each valu
        for value in values:
            v = value

            if value[field] is not None:

                kwargs = {
                    '{0}'.format(field):  value[field] 
                }
                
                ages = CensusLearnSql.objects.values('age').filter(**kwargs)
                
                # takes twice as long if obtaining count from query
                #count = ages.count()
                
                count = 0
                average = 0
                for age in ages:
                    count += 1
                    average += age['age']

                
                average /= count
                
                print field
                print value[field]
                print count
                print average

                
            # used to make sure that all ages field values are None when country_of_birth is None
                #ages=dict(ages[0])
                #for key,value in ages.items():
                #    print key,value
                #    if value is None:
                #          del ages[key]
                #          print "popped"

        
        break

            
    c = 'hello'

    data=str(c)
    
    context = {'data': data} 
    return render(request,'stats.html',context)

