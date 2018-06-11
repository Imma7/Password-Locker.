class Credential:

    credential_list = []

    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password
        Credential.credential_list.append({'account': self.account, 'username': self.username, 'password': self.password})

    def save_account(self):
        '''
        save_account method saves account objects into credential_list
        '''

        Credential.credential_list.append(self)


    @classmethod
    def view_account(cls):
        print('-'*40)
        print("Existing Accounts: ")
        print('-'*40)
        print("Account Name || UserName || Password")
        for i in cls.credential_list:
            print(f" {i['account']} || {i['username']} || {i['password']}")
            

    

    @classmethod
    def delete_account(cls, acc):
        for a in cls.credential_list:
            if a['account'] == acc:
                cls.credential_list.remove(a)
    