'''implement a class called player that represent a cricket player.the player class should have a
method called paly()which print"the player is playing cricket.Derive two classes Batsman and
Bowler, from the player class.overide the play() method in each derived class to print"The batsman
is batting"and"the"bowler is bowling", respectively.write a prderideo create object of both the
Batsman and Bowler classes and call the play()method for each objects.'''


# define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

# define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

# define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

# call the play() method for each object
batsman.play()
bowler.play()
class player:
  def play(self):
    super().play()
    print("The bowler is bowling")
s=bowler
s.play