class User:
    user_list = []

    def __init__ (self,first_name,last_name,e_mail):

      self.first_name =first_name
      self.last_name =last_name
      self.e_mail = e_mail

    def save_user(self):
        User.user_list.append(self)
    def delete_user(self):
        User.user_list.remove(self)
    @classmethod
    def display_users(cls):
        return cls.user_list
