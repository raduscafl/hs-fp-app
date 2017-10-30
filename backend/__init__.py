


def process_user_query(query_string):

    listos=[]
    query_string=query_string.split(',')

    for x in query_string:
        result = (f'Hello {x}!')
        listos.append(result)
    return listos

# process_user_query('Alex, Bob, Radu')
