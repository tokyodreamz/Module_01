import inspect


def introspection_info(obj):

    obj_type = type(obj).__name__

    all_attributes_methods = dir(obj)

    attributes = [attr for attr in all_attributes_methods if not callable(getattr(obj, attr))]

    methods = [method for method in all_attributes_methods if callable(getattr(obj, method))]

    module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'Built-in'


    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return result


number_info = introspection_info(42)
print(number_info)


class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value


my_obj = MyClass(10)

my_obj_info = introspection_info(my_obj)
print(my_obj_info)