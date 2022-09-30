
class Player:
    new_team=[]
    def __init__(self, p):
        self.name = p["name"]
        self.age = p["age"]
        self.position = p["position"]
        self.team = p["team"]
        
    @classmethod
    def get_team(cls,p):
        for a in p:
            Player.new_team.append(cls(a).name)
            Player.new_team.append(cls(a).age)
            Player.new_team.append(cls(a).position)
            Player.new_team.append(cls(a).team)
        print(Player.new_team)
        
       

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]
# print((Player(players[0])).name)
Player.get_team(players) 
