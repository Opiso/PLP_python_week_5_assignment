from main import Player, Coach, Car, Plane, Boat
# Player instance
rashford = Player("2022/2023", "Marcus Rashford", "Forward", "England", 20)
print(rashford.introduce())
print(rashford.score_goal())
print(rashford.club_motto())

# Coach instance
ten_hag = Coach(2022/2023, "Erik ten Hag", "Coach", "Netherlands", 15)
print(ten_hag.introduce())
print(ten_hag.motivate_team())


# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Call move() on each, polymorphically
for v in vehicles:
    print(v.move())
