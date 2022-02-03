from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    smith_jane = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )
    bank.fix_account(smith_jane)

    william_john = Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    )
    bank.fix_account(william_john)

    bank.add(smith_jane)
    bank.add(william_john)

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')