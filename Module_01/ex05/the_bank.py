import re

class Account():
    """Client account"""

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
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
        """Method to allow bank transfer to this account"""
        self.value += amount

class Bank():
    """The bank"""
    def __init__(self):
        self.account = []

    @staticmethod
    def _is_valid_account(account):
        """Verify if account given as argument is valid"""
        found = {
            'name':False,
            'id':False,
            'value':False,
            'zip':False,
            'addr':False
        }
        if isinstance(account, Account):
            if len(account.__dict__) % 2 == 1:
                raise ValueError("Value Error: Corrupted account. Even number of attributes.")
            for attribute in account.__dict__.keys():
                if re.search("^b", attribute):
                    raise ValueError(f"Value Error: Corrupted account. Invalid attribute '{attribute}'.")
                if attribute in found.keys():
                    found[attribute] = True
            if False in found.values():
                missing_values = list(found.keys())[list(found.values()).index(False)]
                if missing_values in ['zip','addr']:
                    if (found['zip'] is False and found['addr'] is True) \
                        or (found['zip'] is True and found['addr'] is False):
                        return True
                raise ValueError(f"Value Error: Corrupted account. Missing attribute '{missing_values}'.")
            return True
        raise TypeError("Type Error: Argument needs to be an Account object.")

    def find_account(self, account_to_find):
        if not isinstance(account_to_find, int) and not isinstance(account_to_find, str):
            return None
        account_found =  next((item for item in self.account if item["id"] == account_to_find), None)\
                if isinstance(account_to_find, int) else next((item for item in self.account if item["name"] == account_to_find), None)
        if account_found is None:
            return None
        return account_found

    def add(self, account):
        """Method to add account to bank"""
        try:
            if self.find_account(account['name']) != None:
                print(ValueError("Value Error: Account name is already in the bank accounts."))
                return
            if self._is_valid_account(account):
                self.account.append(account)
        except Exception as exception:
            print(TypeError(f"{exception} Please make sure you are adding a valid Account object."))

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occurred
        """
        origin_account = self.find_account(origin)
        if origin_account == None:
            print(ValueError("Value Error: Account not found in bank accounts. Are you sure you've added the account to this bank?"))
            return False
        dest_account = self.find_account(dest)
        if dest_account == None:
            print(ValueError("Value Error: Account not found in bank accounts. Are you sure you've added the account to this bank?"))
            return False
        if not isinstance(amount, int) and not isinstance(amount, float):
            print(TypeError("Type Error: Wrong type for amount argument. \
Please make sure it is an int or a float."))
            return False
        origin_index = self.account.index(origin_account)
        dest_index = self.account.index(dest_account)
        if float(self.account[origin_index].value) < float(amount):
            print(ValueError(f"Value Error: You are trying to transfer {float(amount)} \
from {origin_account['name']} account but funds are insufficient."))
            return False
        elif float(amount) < 0:
            print(ValueError("Value Error: You are trying to transfer a negative amount."))
            return False
        else:
            self.account[origin_index].transfer(float(-amount))
            self.account[dest_index].transfer(float(amount))
            return True

    @staticmethod
    def fix_account(account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occurred
        """
        print(f"Fixing account {account['name']}")
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
        if len(account.__dict__) % 2 == 1:
            setattr(account, 'placeholder', 0)
        print("Fixed account.")
        return True
