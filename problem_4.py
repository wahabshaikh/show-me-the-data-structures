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

    if user in group.get_users():
        return True

    groups = group.get_groups()
    for sub_group in groups:
        result = is_user_in_group(user, sub_group)
        if result == True:
            return True

    return False



parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


''' Test case 1: User present in the group '''
print(is_user_in_group(sub_child_user, sub_child))
# Expected output: True


''' Test case 2: User present in the subgroup '''
print(is_user_in_group(sub_child_user, child))
# Expected output: True

print(is_user_in_group(sub_child_user, parent))
# Expected output: True


''' Test case 3: User NOT present '''
print(is_user_in_group("Wahab Shaikh", parent))
# Expected output: False
