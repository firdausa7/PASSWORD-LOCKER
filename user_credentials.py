class Credential:
    credential_list =[]

    def __init__(self,twitter_t,email_e):
        self.twitter_t =twitter_t
        self.email_e =email_e
    def save_credential(self):
        '''
        Function created to save credentials
        '''
        Credential.credential_list.append(self)
    def delete_credential(self):
        '''
        Function added to delete credentials
        '''
        Credential.credential_list.remove(self)
    @classmethod
    def display_credential(cls):
        '''
        a class method involves the whole class the display info display user information
        '''
        return cls.credential_list

