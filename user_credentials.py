class Info:
    info_list = []

    def __init__(self,twitter_t,email_e):
        self.twitter_t =twitter_t
        self.email_e = email_e
    def save_info(self):
        '''
        Function created to save credentials
        '''
        Info.info_list.append(self)
    def delete_info(self):
        '''
        Function added to delete credentials
        '''
        Info.info_list.remove(self)
    @classmethod
    def display_info(cls):
        '''
        a class method involves the whole class the display info display user information
        '''
        return cls.info_list
