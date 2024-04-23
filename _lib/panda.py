# raw query -> return dictionary result
def raw_query(querystr, param):
    from django.db import connection
    result = []
    with connection.cursor() as cursor:
        try:
            cursor.execute(querystr, param)
            dataset = cursor.fetchall()
    
            columnNames = [column[0] for column in cursor.description]
    
            for data in dataset:
                result.append( dict(zip( columnNames, data)))
        finally:
            cursor.close()
            
    return result


def panda_uuid():
    import uuid
    return str(uuid.uuid4().hex).upper()


def raw_query_0(querystr):
    from django.db import connection
    result = []
    with connection.cursor() as cursor:
        try:
            cursor.execute(querystr)
            dataset = cursor.fetchall()
    
            columnNames = [column[0] for column in cursor.description]
    
            for data in dataset:
                result.append( dict(zip( columnNames, data)))
        finally:
            cursor.close()
            
    return result

def panda_today():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get():
        from django.db import connection
        cursor = connection.cursor()
        #cursor.execute("SET sort_buffer_size = 262144256000000")
        cursor.execute("SHOW VARIABLES LIKE '%sort_buffer_size%'")
        row = cursor.fetchall()
        print(row) 

def check_type(a): #to check result return if it is dictionary or list
    type1 = print(type(a)) 
    return type1

def list_index_val(list): #to check list with index associated to the value
    for (i, v) in enumerate(list, start=0):
        pp = print(i, v)
    return pp

def dict_key_val(dict): # to check dict with key associated to the value
    for k, v in dict.items():
        pp = print(k, v)
    return pp

def dict_key(dict, val): #to check dictionary key based on value
    dict_key = print(list(dict.keys())[list(dict.values()).index(val)])
    return dict_key


