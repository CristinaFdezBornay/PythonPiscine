from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    print("==> Creating corrupted account [Even number of args]")
    smith_jane = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )
    bank.add(smith_jane)
    bank.fix_account(smith_jane)
    bank.add(smith_jane)

    print("\n==> Creating corrupted account [Arg starting by 'b']")
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

    print("\n==> Trying invalid transfer")
    if bank.transfer('William John', 'Smith Jane', 54500.0) is False:
        print('Failed')
    else:
        print('Success')

    print("\n==> Trying valid transfer")
    if bank.transfer('William John', 'Smith Jane', 40.0) is False:
        print('Failed')
    else:
        print('Success')