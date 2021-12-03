import re

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        self.value = None
        Account.ID_COUNT += 1

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        txt = "Account"
        for attribute, value in self.__dict__.items():
            txt = txt + f"\n{attribute} : {value}"
        txt += '\n'
        return txt

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def _is_valid_account(self, account):
        """Verify if account given as argument is valid"""
        if isinstance(account, Account):
            if len(account.__dict__) % 2 == 0:
                raise ValueError("Value Error: Corrupted account. Even number of attributes.")
            for attribute in account.__dict__.keys():
                if re.search("^b", attribute):
                    raise ValueError(f"Value Error: Corrupted account. Invalid attribute '{attribute}'.")
            for attribute in ['name', 'id', 'value', 'zip', 'addr']:
                if attribute not in dir(account):
                    raise ValueError(f"Value Error: Corrupted account. Missing attribute '{attribute}'.")
            return True
        else:
            raise TypeError("Type Error: Argument needs to be an Account object.")

    def add(self, account):
        """Method to add account to bank"""
        try:
            if self._is_valid_account(account):
                self.account.append(account)
        except Exception as exception:
            print(TypeError(f"{exception} Please make sure you are adding a valid Account object."))
            if isinstance(account, Account):
                self.fix_account(account)

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occurred
        """
        if not isinstance(origin, int) and not isinstance(origin, str):
            print(TypeError("""Type Error: Wrong type for origin argument.
            Please make sure it is a valid Account name or Account id."""))
            return False
        elif not isinstance(dest, int) and not isinstance(dest, str):
            print(TypeError("""Type Error: Wrong type for dest argument.
            Please make sure it is a valid Account name or Account id."""))
            return False
        if isinstance(origin, int) or isinstance(origin, str):
            origin_account =  next((item for item in self.account if item["id"] == origin), None)\
                if isinstance(origin, int) else next((item for item in self.account if item["name"] == origin), None)
            if origin_account is None:
                print(ValueError("""Value Error: Origin account not found in bank accounts.
                Are you sure you've added the account to this bank?"""))
                return False
        if isinstance(dest, int) or isinstance(dest, str):
            dest_account =  next((item for item in self.account if item["id"] == dest), None)\
                if isinstance(dest, int) else next((item for item in self.account if item["name"] == dest), None)
            if dest_account is None:
                print(ValueError("""Value Error: Dest account not found in bank accounts.
                Are you sure you've added the account to this bank?"""))
                return False
        if not isinstance(amount, int) and not isinstance(amount, float):
            print(TypeError("""Type Error: Wrong type for amount argument.
            Please make sure it is an int or a float."""))
            return False
        else:
            origin_index = self.account.index(origin_account)
            dest_index = self.account.index(dest_account)
            if float(self.account[origin_index].value) < float(amount):
                print(ValueError(f"""Value Error: You are trying to transfer {float(amount)}
                 from {origin_account['name']} account but funds are insufficient."""))
            elif float(amount) < 0:
                print(ValueError("Value Error: You are trying to transfer a negative amount."))
            else:
                self.account[origin_index].transfer(float(-amount))
                self.account[dest_index].transfer(float(amount))

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occurred
        """
        print(f"Fixing account \n{account}")
        keys_to_change = {}
        for attribute in account.__dict__.keys():
            if re.search("^b", attribute):
                new_key = attribute[1:]
                while re.search("^b", new_key):
                    new_key = new_key[1:]
                keys_to_change[attribute] = new_key
        for old_key, new_key in keys_to_change.items():
            account.__dict__[new_key] = account.__dict__.pop(old_key)
        for attribute in ['name', 'id', 'value', 'zip', 'addr']:
            if attribute not in dir(account):
                if attribute == 'name':
                    setattr(account, attribute, "Account " + account['id'])
                if attribute == 'value':
                    setattr(account, attribute, 0)
                if attribute == 'zip':
                    setattr(account, attribute, 00000)
                if attribute == 'addr':
                    setattr(account, attribute, 'No address')
        if len(account.__dict__) % 2 == 0:
            setattr(account, 'placeholder', 0)
        print(f"Attempting to add fixed account to the bank \n{str(account)}")
        self.add(account)
