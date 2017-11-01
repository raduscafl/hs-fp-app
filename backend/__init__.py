def process_user_query(query_string):
    population=[]
    query_string=query_string.strip().split()
    query_string = [x.replace('•', ' ') for x in query_string]
    query_string = [i for i in query_string if i != ' ']

    city=query_string.index("(disambiguation).")
    population.append("City:" + query_string[city+1])
    country=query_string.index("Country")
    population.append("Country:" + query_string[country+1])
    i=query_string.index("Population")
    #ix=query_string.index("Demonym(s)")
    population.append("Population:" + query_string[i+3])
    #for pop in query_string[i:ix]:
        #population.append(pop)
    return population

    #ss=query_string[:900]
    #ss.index





process_user_query(r'''''')
