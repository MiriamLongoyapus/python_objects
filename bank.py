class Bank:
    def __init__(self,account_number,account_holder,account_type):
     self.account_number=account_number
     self.account_holder=account_holder
     self.account_type=account_type
    def saving_account(self):
     return f"dear customer your {self.account_number} has balance of 50,000"
    