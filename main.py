import random
import chef_gpt


if __name__ == "__main__":
    CUISINES = ["Portugese", "Chinese", "French", "Germany", "British", "Danish", "Japanese"]
    cuisine = random.choice(CUISINES)
    chef_gpt.create_recipe(cuisine)