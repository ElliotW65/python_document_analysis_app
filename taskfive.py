from collections import defaultdict

def doc_readers(doc_id, user_id, data):
    '''
    Function to create a set of all the readers of the document passed
    in as a parameter in the data also provided as an argument.

    Parameters:
        doc_id (string): A document id to search for in the data.
        user_id (string): A user id to specify that the user ids of the
                          readers returned should not match the id passed in
                          by the user.
        data (dict): A dictionary of the JSON data to be searched.
    
    Returns:
        visitirs (set): A set of all the readers of the specified document
                        not including the user id passed in as a parameter.

    '''

    visitors = set([i['visitor_uuid'] for i in data if i['visitor_uuid'] !=user_id and i['event_type'] =='read' and i['subject_doc_id'] == doc_id])

    return visitors

def reader_docs(id, data):
    '''
    Function to create a set of all the document ids of the documents
    read by the reader specified in the id parameter.

    Parameters:
        id (string): A user id to search for in the data.
        data (dict): A dictionary of the JSON data to be searched.
    
    Returns:
        docs (set): A set of all the documents read by the reader
                    specified by the id parameter.

    '''

    docs = set([i['subject_doc_id'] for i in data if i['event_type'] =='read' and i['visitor_uuid'] == id])
    
    return docs


def also_likes_sort(dict):
    '''
    Function to sort the dictionary passed in as a parameter by highest
    to lowest value.

    Parameters:
        dict (dict): Dictionary of key value pairs to be sorted.
    
    Returns:
        sort_result (dict): An order dictionary of key value pairs in
                            descending order.

    '''
    
    result = defaultdict(int)

    for i in dict.keys():
        for n in dict[i]:
            result[n] += 1
    
    sort_result = sorted(result.items(), key=lambda x:x[1], reverse=True)

    return sort_result

def also_likes_dict(data, doc_id, user_id = None):
    '''
    Function to return dictionary where the keys are user uuids and the
    values are a list of all of the documents they have read.

    Parameters:
        data (dict): Dictionary of JSON data to be searched.
    
    Returns:
        docs (dict): A dictionary where the keys are user uuids and the
                        values are a list of all of the documents they
                        have read.

    '''

    readers = doc_readers(doc_id,user_id, data)

    docs = {n:reader_docs(n,data) for n in readers if n != user_id}

    if user_id is not None:
        docs[user_id] = {doc_id}

    return docs

def also_likes(data, doc_id, sort, user_id = None):
    '''
    Function to produce an ordered dictionary of key value pairs.

    Parameters:
        data (dict): Dictionary of data to be sorted.
        doc_id (string): The document id to be the focus of the
                            also likes search.
        sort(function): The sorting function to be used to carry
                        out the sorting or the dictionary.
        user_id (optional string): The id of a user.
    
    Returns:
        count (dict): A dictionary of key value pairs where the key
                        is a document id and the value is the number
                        of other readers who have read it.

    '''
    # Check to see if uuid exists in dataset, if not, set to None.
    for i in data:
        if i.get(user_id):
            user_id_test = user_id
        else:
            user_id_test = None

    likes = also_likes_dict(data, doc_id, user_id_test)

    count = sort(likes)

    for i in count:
        print(i[0], ' ', i[1])

    return count


