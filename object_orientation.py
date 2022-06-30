''' this program demontrates how classes and object orientation work'''

class Enemy:
    '''the enemy objects are what the player fights in the game'''
    
    def __init__(self, name, health):
        '''the init function is called when a new object is instantiated 
           It begins and ends with 2 underscores'''
        #set name
        self._name = name
        
        #set health
        self._health = health
        
        #append the new enemy into the enemy_list
        enemy_list.append(self)
        
        #villianous laugh 
        print(f"Mwa hahahaha, {self.get_name()} dusty")
    
    def get_name(self):
        '''This function returns the name of teh enemy object'''
        
        return self._name
    
   
   
    def get_health(self):
        '''ths is a getter function that returns the health of the enemy'''
        
        return self._health 
    
    def attacked(self, damage):
        '''this function is called when the enemy is attacked.
           the damage value is deducted from the health value'''
        
        self._health -=damage
        
        if self._health <=0:
            print("RIP mahomie")
            
        else:
            print("ouchhhy")
    
    
#create a list to store all enemy objects
enemy_list = []
    
#create a new enemy object 
enemy = Enemy("Charliekeithbad.php",1)
enemy = Enemy("Ethan Adams",1000000)


def display_enemies():
    '''this function loops through the enemy_list and displays all their names & health'''
    
    for e in enemy_list:
       # if self._health >=2 :
            
        print(f"{e.get_name()} has {e.get_health()} health left")
        
display_enemies()