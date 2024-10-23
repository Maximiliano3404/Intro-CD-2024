
def hello_world():
    print("Hello world")
    return True

def get_minimum(my_list):
    im_value = my_list[0]
    for element in my_list:
        if min_value >= element:
            min_value = element
    return min_value

hello_world()