class Credential:

    credential_list = []

    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password
        Credential.credential_list.append({'account': self.account, 'username': self.username, 'password': self.password})

    def save_account(self):
        Credential.credential_list.append(self)