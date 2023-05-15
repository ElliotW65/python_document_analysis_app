import graphviz

def make_graph(data, doc_id, user_id=None):
    '''
    Function to create a graphiz digraph plotting the also likes
    functionlaity specified in tasks 5 and 6.

    Parameters:
        data (dict): A dictionary where keys are users ids and the
                        values are a list of documents they have read.
        doc_id (string): id of the base document in the also likes search.
        user_id (string): id of the base user in the also likes search.
        
    
    Returns:
        A PDF of the rendered graph in the same directory

    '''

    dot = graphviz.Digraph()

    for key in data.keys():

        if key == user_id:
            dot.attr('node', shape='box')
            dot.node(key, key[-4:], style='filled', color='.3 .9 .7')
        else:
            dot.attr('node', shape='box')
            dot.node(key, key[-4:])

        for i in data[key]:
            if i == doc_id:
                dot.attr('node', shape='circle')
                dot.node(i, i[-4:],style='filled', color='.3 .9 .7')
                dot.edge(key,i)
            else:
                dot.attr('node', shape='circle')
                dot.node(i, i[-4:])
                dot.edge(key,i)


    dot.render('Also Likes Graph', view=True)
