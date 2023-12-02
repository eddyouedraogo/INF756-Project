from threading import Lock

mutex = Lock()
class Mouse:
    
    def __init__(self, id, intelligence, health, mental, current_room):
        self.id = id
        self.intelligence = intelligence
        self.health = health
        self.mental = mental
        self.current_room = current_room
        self.objective_consumed = False
    
    def __repr__(self) -> str:
        return f"Mouse intelligence level is {self.intelligence} health is {self.health} mental is {self.mental} and current room is {self.current_room}"
    
    def take_step(self, room, action, objectives):
        self.update_attributes(action, room)
        self.current_room = room
        objective_id = room.get("objective_id")
        
        if (objective_id):
            self.interact_with_objective(objectives, objective_id, room)
        return
    
    def interact_with_objective(self, objectives, objective_id, room):
        for objective in objectives:
            if objective.get("objective") == objective_id:
                self.update_attributes(objective, room)
        return

    def eat(self):
        print("Eating")
        return

    def drink(self):
        print("Drinking")
        return
    
    def update_attributes(self, rule, room):
        self.intelligence = self.update_attribute(self.intelligence, rule.get("effect_on_intelligence"))
        self.health = self.update_attribute(self.health, rule.get("effect_on_health"))
        self.mental = self.update_attribute(self.mental, rule.get("effect_on_mental"))

        if rule.get("objective") in [1,3,6]:
            with mutex: 
                room["objective_id"] = None
            self.objective_consumed = True
        else:
            self.objective_consumed = False

    def update_attribute(self, current_value, to_be_added):
        res = current_value + to_be_added
        if res > 10:
            return 10
        elif res <= 0:
            return 0
        else: 
            return res