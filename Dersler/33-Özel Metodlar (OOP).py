class Movie:
    def __init__(self, movie, duration):
        self.movieName = movie
        self.duration = duration
        print("Object has been created.")

    def getinfo(self):
        print(f"Movie name is {self.movieName} and duration is {self.duration}.")


m1 = Movie("SM", "2 hours 36 minutes")
m1.getinfo()

# We created a simple class. Now lets try to some print functions it.

print(m1)

# Now lets create another class.


class Song:
    def __init__(self, name, duration):
        self.songName = name
        self.duration = duration
        print("Object has been created.")

    def getinfo(self):
        print(f"Song name is {self.songName} and duration is {self.duration}.")

    # We are going to change the output when we use print(object).
    def __str__(self):
        a = f"{30*'-'}\nThis is the new output.\n{30*'-'}"
        return a

    # This time we are going to change the output when we use print(len(object)) but return type must be integer.
    def __len__(self):
        return self.duration

    # Now we are going to change the output when we delete the object.
    def __del__(self):
        print("Object has been deleted.")


s1 = Song("Bitti Rüya", 4)
s1.getinfo()

print(s1)
print(len(s1))

del s1
