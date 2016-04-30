# This is a simple Mad Libs project.

print "Mat Libs is starting."

# Input user's name
name = raw_input("name:")

#Input 3 adjectives
adjectives1 = raw_input("Enter an adjective:")
adjectives2 = raw_input("Enter an adjective:")
adjectives3 = raw_input("Enter an adjective:")

#Input 3 verbs
verbs1 = raw_input("Enter a verb:")
verbs2 = raw_input("Enter a verb:")
verbs3 = raw_input("Enter a verb:")

#Input 4 nouns
nouns1 = raw_input("Enter a noun:")
nouns2 = raw_input("Enter a noun:")
nouns3 = raw_input("Enter a noun:")
nouns4 = raw_input("Enter a noun:")

# Input each of the following variables
animal = raw_input("Enter an animal:")
food = raw_input("Enter a food:")
fruit = raw_input("Enter a fruit:")
number = raw_input("Enter a number:")
superhero = raw_input("Enter a superhero:")
country = raw_input("Enter a country:")
dessert = raw_input("Enter a dessert:")
year = raw_input("Enter a year:")

#The template for the story
STORY = "This morning I woke up and felt %s because _ was going to finally %s over the big _ %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to _ to the rythym of the %s, which made all of the %ss very _. %s tried to _ into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping _ into a puddle of %s. %s then fell asleep and woke up in the year _, in a world where %ss ruled the world."

print STORY % (adjectives1, adjectives2, adjectives3, verbs1, verbs2, verbs3, nouns1, nouns2, nouns3, nouns4, animal, food, fruit, number, superhero, country, dessert, year
)