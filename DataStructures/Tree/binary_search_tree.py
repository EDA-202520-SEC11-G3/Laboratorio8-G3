from DataStructures.Tree import bst_node as n
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as al


def new_map():
    """Create a new empty BST container.

    The map is represented as a dict with a single key "root" whose value
    is either None or a bst_node created by `bst_node.new_node`.
    """
    return {"root": None}


def node_size(node):
    if node is not None:
        return node["size"]
    else:
        return 0


def insert_node(node, key, value):
    """Recursive helper that inserts key/value into subtree rooted at node.

    Returns the (possibly new) root node of the subtree.
    """
    if node is None:
        return n.new_node(key, value)

    if key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = insert_node(node["right"], key, value)
    else:
        # update existing key
        node["value"] = value

    # update size
    node["size"] = 1 + node_size(node["left"]) + node_size(node["right"])
    return node


def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst.get("root"), key, value)
    return my_bst


def get(my_bst, key):
    node = my_bst["root"]
    while node is not None:
        if node["key"] is not None:
            if key == node["key"]:
                return node["value"]
            elif key < node["key"]:
                node = node["left"]
            else:
                node = node["right"]
    return None


def size_tree(tree):
    node = tree["root"]
    return node_size(node)


def size(my_bst):
    if my_bst is None:
        return 0
    return size_tree(my_bst)

def contains(my_bst, key):
    if get(my_bst, key) != None:
        return True
    return False

def is_empty(my_bst):
    if size(my_bst) == 0:
        return True
    return False

def key_set(my_bst):
    key_list = sll.new_list()
    return key_set_tree(my_bst.get("root"), key_list)

def key_set_tree(my_bst, key_list):
    if my_bst is not None:
        if my_bst.get("key") is None:
            return key_list
        else:
            sll.add_first(key_list, my_bst["key"])
            key_set_tree(my_bst["left"], key_list)
            key_set_tree(my_bst["right"], key_list)
    return key_list

"""def remove(my_bst, key):
    return remove_node(my_bst.get("root"), key)

def remove_node(root, key):
        if root["key"] is not None:
            if key == root["key"]:
                
            else:
                remove_node(root["left"], key)
                remove_node(root["right"], key)"""

def value_set(my_bst):
    value_list = sll.new_list()
    return value_set_tree(my_bst.get("root"), value_list)

def value_set_tree(my_bst, value_list):
    if my_bst is not None:
        if my_bst.get("value") is None:
            return value_list
        else:
            sll.add_first(value_list, my_bst["value"])
            key_set_tree(my_bst["left"], value_list)
            key_set_tree(my_bst["right"], value_list)
    return value_list

def get_min(my_bst):
    return get_min_node(my_bst.get("root"))

def get_min_node(root):
    if root is not None:
        min = 0
        while root is not None:
            min = root["value"]
            root = root["left"]
        return min
    return None

def get_max(my_bst):
    return get_max_node(my_bst.get("root"))

def get_max_node(root):
    if root is not None:
        max = 0
        while root is not None:
            min = root["value"]
            root = root["right"]
        return max
    return None

def delete_min(my_bst):
    return delete_min_tree(my_bst.get("root"))

def delete_min_tree(root):
    if root is not None:
        while True:
            if root["left"]["left"] is None:
                root["left"] = None
                return root
            root = root["left"]
    return root

def delete_max(my_bst):
    return delete_max_tree(my_bst.get("root"))

def delete_max_tree(root):
    if root is not None:
        while True:
            if root["right"]["right"] is None:
                root["right"] = None
                return root
            root = root["right"]
    return root

def floor(my_bst, key):
    return floor_key(my_bst, key)

def floor_key(my_bst, key):
    lst = key_set(my_bst)
    min = float('inf')
    key_next = key
    i = 0
    node = lst["first"]
    while i in range(lst["size"]):
        if abs(node["info"] - key) < min:
            min = abs(node["info"] - key)
            key_next = node["info"]
        elif abs(node["info"] - key) == min:
            min = abs(node["info"] - key)
            if node["info"] < key_next:
                key_next = node["info"]
        node = node["next"]
        i += 1
    return key_next

def ceiling(my_bst, key):
    return ceiling_key(my_bst, key)

def ceiling_key(my_bst, key):
    lst = key_set(my_bst)
    max = float('-inf')
    key_next = key
    i = 0
    node = lst["first"]
    while i in range(lst["size"]):
        if abs(node["info"] - key) < max:
            max = abs(node["info"] - key)
            key_next = node["info"]
        elif abs(node["info"] - key) == max:
            max = abs(node["info"] - key)
            if node["info"] > key_next:
                key_next = node["info"]
        node = node["next"]
        i += 1
    return key_next

def height(my_bst):
    return height_tree(my_bst.get("root"))

def height_tree(root):
    left = 0
    right= 0
    root2 = root
    if root is not None:
        while root is not None:
            left += 1
            root = root["left"]
        while root2 is not None:
            right += 1
            root2 = root2["right"]
    if left > right:
        return left
    return right

def keys(my_bst, key_inital, key_final):
    lst = sll.new_list()
    return keys_range(my_bst, key_inital, key_final, lst)

def keys_range(root, key_i, key_f, lst):
    dataSet = key_set(root)
    node = dataSet["first"]
    i = 0
    while i in range(dataSet["size"]):
        if node["info"]> key_i and node["info"]< key_f:
            sll.add_first(lst, node["info"])
        node = node["next"]
        i += 1
    return lst

def values(my_bst, key_inital, key_final):
    lst = sll.new_list()
    return values_range(my_bst, key_inital, key_final, lst)

def values_range(root, key_i, key_f, lst):
    dataSet = value_set(root)
    node = dataSet["first"]
    i = 0
    while i in range(dataSet["size"]):
        if node["info"]> key_i and node["info"]< key_f:
            sll.add_first(lst, node["info"])
        node = node["next"]
        i += 1
    return lst