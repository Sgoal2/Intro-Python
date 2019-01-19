# Write a class to hold player information, e.g. what room they are in
# currently.
# class Player:
#     def __init__(self, startLocation):
#         self.location = startLocation
#     def change_location(self, new_location):
#         self.location = new_location
#     def __repr__(self):
#         return "Current Location: {}".format(self.location)
#     def __str__(self):
#         return "Current Location: {}".format(self.location)

class Player:
    def __init__(self, startLocation):
        self.location = startLocation
    def change_location(self, new_location):
        self.location = new_location
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)    