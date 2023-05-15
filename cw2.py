import json as js
import argparse
import tasks_up_to_four as task
import taskfive as five
import tasksix as six
import time
import sys


def task_five_data(file):
    '''
    Funciton to create a list of dictionries of the necessary data
    for task five.

    Parameters:
        file (file): The file object containing the JSON data.

    Returns:
        dataset (list): A list of dictionaries containing the visitor_uuid,
                        event_type and subject_doc_id of each JSON object
                        in the file parameter.

    '''

    dataset = []
    for i in file:
        json_dict = js.loads(i)
        reduced_data = {}
        reduced_data['visitor_uuid'] = json_dict.get('visitor_uuid')
        reduced_data['event_type'] = json_dict.get('event_type')
        reduced_data['subject_doc_id'] = json_dict.get('subject_doc_id')
        dataset.append(reduced_data)
    return dataset


def task_three_data(file):
    '''
    Funciton to create a list of the necessary data for task three.

    Parameters:
        file (file): The file object containing the JSON data.

    Returns:
        dataset (list): A list of all visitor_useragent values in
                        the file parameter.
    '''
    dataset = []
    for i in file:
        json_dict = js.loads(i)
        if json_dict.get('visitor_useragent') and json_dict.get('event_type') =='read':
            dataset.append(json_dict.get('visitor_useragent'))
    return dataset


def task_two_data(file):
    '''
    Funciton to create a list of the necessary data for task two.

    Parameters:
        file (file): The file object containing the JSON data.

    Returns:
        dataset (list): A list of all visitor_country values in
                        the file parameter.
    '''
    dataset = []
    for i in file:
        json_dict = js.loads(i)
        if json_dict.get('visitor_country') and json_dict.get('event_type') =='read':
            dataset.append(json_dict.get('visitor_country'))
    return dataset


def task_four_data(file):
    '''
    Funciton to create a list a list of dictionries of the necessary
    data for task four.

    Parameters:
        file (file): The file object containing the JSON data.

    Returns:
        dataset (list): A list of dictionaries containing the visitor_uuid
                        and event_readtime of each JSON object in the file
                        parameter.
    '''
    dataset = []
    for i in file:
        json_dict = js.loads(i)
        reduced_data = {}
        reduced_data['visitor_uuid'] = json_dict.get('visitor_uuid')
        reduced_data['event_readtime'] = json_dict.get('event_readtime')
        dataset.append(reduced_data)
    return dataset


if __name__ == '__main__':

    start_time = time.time()

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-u', '--uuid', help='User ID')
    arg_parser.add_argument('-d', '--doc_uuid', help='Document ID')
    arg_parser.add_argument('-t', '--task_id', help='Task ID')
    arg_parser.add_argument('-f', '--file_name', help='File name')

    args = arg_parser.parse_args()

    try:
        if args.file_name is not None:
            file = open(args.file_name)
        else:
            print('Please enter a file name.')
            sys.exit()

    except FileNotFoundError as error:
        print('Could not find file: ', args.file_name, '\nPlease enter valid file name.')
        sys.exit()

    if args.task_id == '2a':

        data = task_two_data(file)
        task.task_two_a(data, task.show_histogram)
    
    elif args.task_id == '2b':

        print('Not yet implemented')
        sys.exit()

    elif args.task_id[0] == '3':

        data = task_three_data(file)
        task.process_browsers(data, task.show_histogram, args.task_id)
    
    elif args.task_id == '4':

        data = task_four_data(file)
        task.task_four(data)

    elif args.task_id == '5d':

        data = task_five_data(file)
        five.also_likes(data, args.doc_uuid,five.also_likes_sort, args.uuid)

    elif args.task_id == '6':

        data = task_five_data(file)
        data = five.also_likes_dict(data, args.doc_uuid, args.uuid)
        six.make_graph(data, args.doc_uuid,args.uuid)

    elif args.task_id == '7':

        print('Not yet implemented.')
        sys.exit()

    print("--- %s seconds ---" % (time.time() - start_time))
