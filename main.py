from art import logo, vs
from game_data import data
import random
curret_score = 0
def shuffle_list(data):
     random.shuffle(data)
    


def get_name():

    random_person = random.choice(data)
    return random_person

def follower_count(user):
    followers = user["follower_count"]
    return followers

def compare_followers(a_f, b_f):
    

    if a_f > b_f:
        return "a"
    elif b_f > a_f:
        return "b"
    
       
    #     # return f"You are right Your score is {score} "
    # elif a_follower < b_follower and user_input == "b":
    #     score = score + 1
    #     return f"You are right Your score is {score} "
    # else:
    #     return c
    
          
end_of_program = False
a = get_name()
while not end_of_program:
    print(logo)
    shuffle_list(data)
    
    b = get_name()
    print(f"Compare A : {a['name']} a {a['description']} from {a['country']}", )
    print(vs)
    print(f"Against B : {b['name']} a {b['description']} from {b['country']}", )
    user_input = input("Who has more followers Type 'A' or 'B'").lower()
    a_followers = follower_count(a)
    b_followers = follower_count(b)
    higher_followers = compare_followers(a_followers, b_followers)
    if higher_followers == "a" and user_input == "a":
        curret_score += 1
        a = a
        print(f"You are right Your score is {curret_score}")
    elif higher_followers == "b" and user_input == "b":
         curret_score += 1
         a = b
         print(f"You are right Your score is {curret_score}")
    else:
        print(f"Sorry! You are Wrong Your final score is {curret_score}")
        end_of_program = True





