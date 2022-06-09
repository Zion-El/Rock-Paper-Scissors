class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.track = [tracks]
        self.tracks = self.track
        self.score = score

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        if type(new_age) == int:
            self.age = new_age
        else:
            print('Input a whole number')

    def add_track(self, add_track):
        self.track.append(add_track)

    def get_score(self):
        print(self.score)

