from operator import truediv


class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_names=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.rewards_member=False
        self.gold_card_points=0
    
    def display_info(self):
        print(vars(self))
        return self
    
    def enroll(self):
        if self.rewards_member==True:   
            print("User already a member")
            return self
        else:
            self.rewards_member=True
            self.gold_card_points=200
            return self

    def spend_pints(self,amount):
        if self.gold_card_points<amount:
            print("not enough point to spend")
            return self
        else:
            self.gold_card_points=self.gold_card_points-amount 
            return self
    
Juan=User("Juan","Campos",'jcaet@gmail.com',30)
Richard=User('Richard','Paulus','rcdfa@gmail.com',21)
Derrick=User('Derrick','Rodrigues','dfasdfa@gmail.com',50)
Juan.display_info().enroll().spend_pints(50).display_info()
Derrick.spend_pints(300).display_info()
Richard.enroll().spend_pints(80).display_info()

