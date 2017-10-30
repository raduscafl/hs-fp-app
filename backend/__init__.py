


def process_user_query(query_string):
    listos=[]
    query_string=query_string.split(' ')
    for x in query_string:
        if x[0].isupper():
            result = (f'Hello {x}!')
            listos.append(result)
    return set(listos)
#process_user_query('Alex si Bob ')
