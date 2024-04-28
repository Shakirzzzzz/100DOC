class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        # fixed attribute with initial value which can be changed later
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User('001','Shakir' )
user_2 = User('002', 'Rabiya')

user_1.follow(user_2)

# user1.username = 'Shakir'
# print(user1.username)
print(user_1.following)