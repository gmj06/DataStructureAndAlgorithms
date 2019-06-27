class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return is_user_in_group_helper(user, group)

def is_user_in_group_helper(user, group):
    # Case when user or group is not provided
    if user == "" or group is None:
        return False

    users = group.get_users()

    if isinstance(users, list):
        if user in users:
            return True

    sub_groups = group.get_groups()
    for sub_group in sub_groups:
        return is_user_in_group_helper(user, sub_group)

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child.add_user("child_user")
parent.add_group(child)


print(is_user_in_group("sub_child_user", parent)) # output - True
print(is_user_in_group("child_users", child)) # output - False
print(is_user_in_group("", child)) # output - False
print(is_user_in_group("No Group", None)) # output - False
    
        