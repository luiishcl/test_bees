Feature: Register on Deposit 
  As a BEES user,
  I want to access deposit
  So I can manager the deposit register

    @deposits @create
    Scenario: Register a Deposit
        Given stay on "Deposits" session
        When create a new deposit
        """
            {
                "name": "Deposit_A",
                "address": "Rua Orlando Viana",
                "city": "Campinas",
                "state": "Sao Paulo",
                "zipcode": "13044900"
            }
        """
        Then the deposits were created successful


    @deposits @edit
    Scenario: Edit a Deposit
        Given stay "Editing deposit" session
        When edit a deposit
        """
            {
                "name": "Deposit_Edited",
                "address": "wall street",
                "city": "city_edited",
                "state": "NY",
                "zipcode": "71601"
            }
        """
        Then the deposits were edited successful


    @deposits @delete
    Scenario: Destroy a Deposit
        Given pick up a deposits
        When destroy it
        Then deposit is removed