# class Duck:
#     def walk(self):
#         print("this duck is walking ")
#     def talk(self):
#         print("this duck is clucking ")
    
# class Chicken:
#     def walk(self):
#         print("this chicken  is walking ")
#     def talk(self):
#         print("this chicken is  clucking ")

# class Person:
#     def catch(self , duck):  # deck if object here 
#         duck.walk()          # calling the walk method 
#         duck.talk()          # calling the talk method 
#         print(" you caught the critter !")


# duck = Duck()
# chicken = Chicken()
# person  = Person()

# person.catch(duck)
# print()
# person.catch(chicken)



#-----------practice ----------------
class Duck:
    def walk(self):
        print("this duck is walking ")
    def talk(self):
        print("this duck is clucking ")
    
class Chicken:
    def walk(self):
        print("this chicken  is walking ")
    def talk(self):
        print("this chicken is  clucking ")
class Person:
    def catch(self , s1 , s2): 
        s1.walk()          
        s1.talk()   
        s2.walk()          
        s2.talk()   
        print(" you caught the critter !")

duck = Duck()
chicken = Chicken()
person  = Person()
person.catch(duck , chicken)
