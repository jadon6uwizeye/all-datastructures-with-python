from collections import namedtuple

User = namedtuple('user', 'username email pwd')

print(' type of type =>', type(User))

someone = User('jadon6', 'jado@me.com', '123456789')

print(' type of someone =>', type(someone))
print(someone)

print(' username =>', someone.username)

# comvert someone to dict
someone_dict = someone._asdict()
print(' type of someone_dict =>', type(someone_dict))
print(someone_dict)

someone._replace(pwd='3479')
print(someone)

someone = someone._replace(pwd='3479')
print(someone)

# convert someone to list
someone_list = list(someone)

