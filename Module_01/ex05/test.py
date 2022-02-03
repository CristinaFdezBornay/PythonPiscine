from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    print("==> [Bank] Adding not an account.")
    bank.add(1)

    print("\n==> [Bank] Adding a corrupted account.")
    william_john = Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        bref="lol",
    )
    bank.add(william_john)
    bank.fix_account(william_john)
    bank.add(william_john)

    print("\n==> [Bank] Adding account with repeated name.")
    william_john = Account(
        'William John',
        value=0.0,
        zip='03540'
    )
    bank.add(william_john)

    print("\n==> [Bank] Adding a corrupted account.")
    smith_jane = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )
    bank.add(smith_jane)

    print("\n==> [Transfer] Invalid because of the corrupted account")
    print('Failed') if bank.transfer('William John', 'Smith Jane', 1) is False else print('Success')

    bank.fix_account(smith_jane)
    bank.add(smith_jane)

    print("\n==> [Transfer] Invalid because of name not a string")
    print('Failed') if bank.transfer(123, 'Smith Jane', 10) is False else print('Success')


    print("\n==> [Transfer] Invalid because of the amount")
    print('Failed') if bank.transfer('William John', 'Smith Jane', 54500.0) is False else print('Success')

    print("\n==> [Transfer] Valid")
    print('Failed') if bank.transfer('William John', 'Smith Jane', 40.0) is False else print('Success')