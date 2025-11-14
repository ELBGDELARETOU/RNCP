def all_thing_is_obj(object: any) -> int:
    tp = type(object).__name__
    if tp == "str":
        tp = object + " is in the kitchen"
    if tp == "int":
        print("Type not found")
        return 42
    print(tp.capitalize(), " : ", type(object))
    return 42

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))