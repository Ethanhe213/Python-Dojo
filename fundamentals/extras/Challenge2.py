class Player:
    def __init__(self, p):
        self.name = p["name"]
        self.age = p["age"]
        self.position = p["position"]
        self.team = p["team"]
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_jason =Player(jason)
player_kevin=Player(kevin)
player_kyrie=Player(kyrie)
