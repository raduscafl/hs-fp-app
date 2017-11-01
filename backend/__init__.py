def process_user_query(query_string):
        population=[]
        query_string=query_string.split(' ')

        city=query_string.index("(disambiguation).")
        population.append("City:" + query_string[city+1])
        i=query_string.index("Population")
        ix=query_string.index("Demonym(s)")
        i=i+2
        population.append("Population:")
        for pop in query_string[i:ix]:
            population.append(pop)
        return population
#process_user_query("Populations (disambiguation). Bucale Elevation 667 m (2,188 ft) Population (2015[4])• Municipality 3,141,991 Demonym(s) Londoner Cockney (colloquial)")
