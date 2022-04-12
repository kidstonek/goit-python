
def get_fullname (first_name, last_name, middle_name=None):
    if middle_name == None:
        return first_name + " " + last_name
    else:
        return first_name + " " + middle_name + " " + last_name


print(get_fullname("Андрей", "Васильченко", "Сергеевич"))