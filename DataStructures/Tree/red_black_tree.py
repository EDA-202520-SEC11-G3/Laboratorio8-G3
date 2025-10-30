from DataStructures.Tree import rbt_node as rb

RED = 0
BLACK = 1

def new_map():
    return {"root":None, "type":"RBT"}

def is_red(my_node):
    return my_node is not None and my_node["color"] == RED

def exchange_info(n1, n2):
    k1 = n1["key"]
    k2 = n2["key"]
    v1 = n1["value"]
    v2 = n2["value"]
    n1["key"] = k1
    n1["value"] = v1
    n2["key"] = k2
    n2["value"] = v2

def flip_node_color(node):
    node["color"] = BLACK if node["color"] == RED else RED
    return node

def flip_colors(node):
    flip_node_color(node)
    if node["left"] is not None:
        flip_node_color(node["left"])
    if node["right"] is not None:
        flip_node_color(node["right"])
    return node

def default_compare(key, element):
    if key == element["key"]:
        return 0
    elif key > element["key"]:
        return 1
    return -1

def rotate_left(h):
    x = h["right"]
    h["right"] = x["left"]
    x["left"] = h
    x["color"], h["color"] = h["color"], RED
    return x

def rotate_right(h):
    x = h["left"]
    h["left"] = x["right"]
    x["right"] = h
    x["color"], h["color"] = h["color"], RED
    return x

def put(my_tree, key, value):
    my_tree["root"] = insert_node(my_tree["root"], key, value)
    return my_tree

def insert_node(root, key, value):
    if root is None:
        return {"key": key, "value": value, "color": RED, "left": None, "right": None}
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    return root

def get(my_tree, key):
    return get_node(my_tree["root"], key)

def get_node(root, key):
    if root is None:
        return None
    if key == root["key"]:
        return root["value"]
    if key < root["key"]:
        return get_node(root["left"], key)
    return get_node(root["right"], key)

def contains(my_tree, key):
    return get(my_tree, key) is not None

def size(my_tree):
    return size_tree(my_tree["root"])

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def is_empty(my_tree):
    return my_tree["root"] is None

def key_set(my_tree):
    keys = []
    key_set_tree(my_tree["root"], keys)
    return keys

def key_set_tree(root, keys):
    if root is None:
        return
    key_set_tree(root["left"], keys)
    keys.append(root["key"])
    key_set_tree(root["right"], keys)

def value_set(my_tree):
    values = []
    value_set_tree(my_tree["root"], values)
    return values

def value_set_tree(root, values):
    if root is None:
        return
    value_set_tree(root["left"], values)
    values.append(root["value"])
    value_set_tree(root["right"], values)

def get_min(my_tree):
    return get_min_node(my_tree["root"])

def get_min_node(root):
    if root is None or root["left"] is None:
        return root["key"] if root else None
    return get_min_node(root["left"])

def get_max(my_tree):
    return get_max_node(my_tree["root"])

def get_max_node(root):
    if root is None or root["right"] is None:
        return root["key"] if root else None
    return get_max_node(root["right"])

def height(my_tree):
    return height_tree(my_tree["root"])

def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def keys(my_tree, key_initial, key_final):
    keys = []
    keys_range(my_tree["root"], key_initial, key_final, keys)
    return keys

def keys_range(root, key_initial, key_final, keys):
    if root is None:
        return
    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, keys)
    if key_initial <= root["key"] <= key_final:
        keys.append(root["key"])
    if root["key"] < key_final:
        keys_range(root["right"], key_initial, key_final, keys)

def values(my_tree, key_initial, key_final):
    values = []
    values_range(my_tree["root"], key_initial, key_final, values)
    return values

def values_range(root, key_initial, key_final, values):
    if root is None:
        return
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, values)
    if key_initial <= root["key"] <= key_final:
        values.append(root["value"])
    if root["key"] < key_final:
        values_range(root["right"], key_initial, key_final, values)