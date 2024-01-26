
class RoseDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def pop_item(self, raise_error=False, error_msg=None, default=None):
        if not self.data and raise_error:
            raise KeyError(error_msg) if error_msg else "Dictionary was empty and no default value/message was specified."
        elif not self.data and not raise_error:
            return error_msg if error_msg else "Dictionary was empty and no default value/message was specified."
        else:
            key = list(self.data.keys())[-1]
            value = self.data[key]
            del self.data[key]
            return (key, value) if not default else (key, value) if self.data else default

    def get_item(self, key, raise_error=False, error_msg=None, default=None):
        if raise_error and key not in self.data:
            raise KeyError(error_msg) if error_msg else "Value was not found and no default value/message was specified."
        elif not raise_error and key not in self.data:
            return default if default else "Value was not found and no default value/message was specified."
        else:
            return self.data[key]

d = RoseDictionary()
d["key1"] = "value1"
d["key2"] = "value2"
print(d["key1"]) 
print(d.get_item("key1"))
print(d.get_item("key3", default="Default Value"))
d.get_item("key3") 
print(d.pop_item())
print(d.get_item("key1", error_msg="error message"))
print(d.get_item("key2", error_msg="error message2"))
d.pop_item() 
try:
    d.get_item("key3", default="Default Value", raise_error=True, error_msg="Hi")
except KeyError as e:
    print(f"Key error raised with message : {e}")
