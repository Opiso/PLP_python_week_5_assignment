class ManchesterUnited:
    def __init__(self, season, name, role, nationality):
        self.season = season
        self.name = name
        self.role = role
        self.nationality = nationality

    def introduce(self):
        return f"{self.name} is a {self.role} from {self.nationality} representing Manchester United."

    def club_motto(self):
        return "Glory Glory Man United!"

class Player(ManchesterUnited):
    def __init__(self, season, name, role, nationality, goals=0):
        super().__init__(season, name, role, nationality)
        self.season = season
        self.role = role
        self.goals = goals

    def score_goal(self):
        self.goals += 1
        return f"{self.name} scores! Total goals in {self.season} season: {self.goals}"

    def introduce(self):
        return f"{self.name} played as a {self.role} for Manchester United in {self.season} season"

class Coach(ManchesterUnited):
    def __init__(self,season, name, role, nationality, experience_years):
        super().__init__(season, name, role, nationality)
        self.experience_years = experience_years

    def motivate_team(self):
        return f"Coach {self.name} says: 'Let’s bring home the FA cup, lads!' 💪"

    def introduce(self):
        return f"{self.name}, with {self.experience_years} years of coaching experience, led Manchester United to a major trophy success in 6 years."



# Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

