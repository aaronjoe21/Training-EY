class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def delete_user(self, user_list, user_name):
        return [u for u in user_list if u.name != user_name]

# Test
u1 = User("Vaishnavi")
u2 = User("Rahul")
admin = Admin("Admin")
users = [u1, u2]
users = admin.delete_user(users, "Rahul")
print([u.name for u in users])
