class RoseDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def pop_item(self, raise_error=False, error_msg=None, default=None):
        if not self.data:
            return self.handle_empty_dictionary(raise_error, error_msg, default)

        key = list(self.data.keys())[-1]
        value = self.data.pop(key)
        return (key, value) if not default else (key, value) if self.data else default

    def get_item(self, key, raise_error=False, error_msg=None, default=None):
        if raise_error and key not in self.data:
            return self.handle_key_error(error_msg)
        elif not raise_error and key not in self.data:
            return default if default else self.handle_value_not_found_error(error_msg)
        else:
            return self.data[key]

    def handle_empty_dictionary(self, raise_error, error_msg, default):
        if raise_error:
            raise KeyError(error_msg) if error_msg else "Dictionary was empty, and no default value/message was specified."
        else:
            return error_msg if error_msg else "Dictionary was empty, and no default value/message was specified."

    def handle_key_error(self, error_msg):
        raise KeyError(error_msg) if error_msg else "Value was not found, and no default value/message was specified."

    def handle_value_not_found_error(self, error_msg):
        return error_msg if error_msg else "Value was not found, and no default value/message was specified."

# Example usage:
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
    print(f"Key error raised with message: {e}")
