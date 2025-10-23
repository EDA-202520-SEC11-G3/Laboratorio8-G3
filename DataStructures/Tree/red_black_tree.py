from DataStructures.Tree import rbt_node as rb

RED = 0
BLACK = 1

def new_map():
    return {"root":None, "type":"RBT"}

def is_red(my_node):
    """
    Informa si un nodo es rojo
    Args:
        my_node: El nodo a revisar

    Returns:
        True si el nodo es rojo, False de lo contrario
    Raises:
        Exception
    """
    return my_node["color"] == RED

def exchange_info(n1, n2):
    k1=rb.get_key(n1)
    k2=rb.get_key(n2)
    v1=rb.get_value(n1)
    v2=rb.get_value(n2)
    n1["key"]=k1
    n1["value"]=v1
    n2["key"]=k2
    n2["value"]=v2

def flip_node_color(node):
    if is_red(node):
        node["color"]=BLACK
    else:
        node["color"]=RED
    return node
    
def flip_colors(node):
    flip_node_color(node)
    if node["left"] is not None:
        flip_colors(node["left"])
    if node["right"] is not None:
        flip_colors(node["right"])
    return node

def default_compare(key, element):
   if key == rb.get_key(element):
      return 0
   elif key > rb.get_key(element):
      return 1
   return -1

def put(my_tree, key, value):
    node=rb.new_node(key, value)
    insert_node(my_tree["root"], node)
    pass    

def rotate_left(node):
    l_key=node["key"]
    l_value=node["value"]
    node=node["left"]
    node["right"]=rb.new_node(l_key,l_value)
    return node

def rotate_right(node):
    r_key=node["key"]
    r_value=node["value"]
    node=node["right"]
    node["right"]=rb.new_node(r_key,r_value)
    return node

def insert_node(tree, node):
    if tree:
        pass