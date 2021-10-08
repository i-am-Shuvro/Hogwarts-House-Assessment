# Greetings
print(
    "Welcome to Hogwarts School of Witchcraft and Wizardry! \nAttend this questionnaire session honestly & carefully for the best house-allocation for you. "
    "\n[N.B: Your answers will be analyzed to allot you one among the 4 prestigious houses of Hogwarts: Gryffindor, Hufflepuff, Ravenclaw and Slytherin.]")

# Quetion for Gryffindor
x = int(input(("\n(a) Suppose you are about to witness a road accident. A blind old man with a wound on "
               "his foot is crossing the road and a truck is rushing \ntowards him. No one is there to help "
               "the old man. How do you react?"
               "\n\t1. Rush to the blind man and take him to the side of the road asap."
               "\n\t2. Rescue him from that spot and take him to the hospital. Stay beside him in the hospital and help him to reach his home safely."
               "\n\t3. Rescue him from that spot. Help him to reach the hospital and call his family members."
               "\nWhat will be your answer? Choose between option 1 to option 3: ")))

# Defining percentage for Gryffindor
if x == 1:
    X = 25
elif x == 2:
    X = 100
else:
    X = 75

# Quetion for Hufflepuff
y = int(input(
    ("\n(b) Suppose you see a police officer misbehaving with a homeless person. He is also using physical violence. "
     "It is known for a fact that the homeless \nperson has done nothing wrong, but the cop is misusing his powers. "
     "No one in public dares to stand up for the helpless. How would you approach it?"
     "\n\t1. Approach the cop and humbly try to tell him to stop as what he's doing is against law. Secretly record the whole conversation and if the cop refuses your saying blackmail him with the voice record."
     "\n\t2. Take out your phone and go live on facebook, and interrogate the cop immediately. As cameras are like the ‘New guns’ of the 21st century, the cop will be scared and leave the homeless alone."
     "\n\t3. Do nothing; decide not to get into any trouble."
     "\n\t4. Offer the cop some cash in exchange for leaving the poor person alone"
     "\nWhat will be your answer? Choose between option 1 to option 4: ")))

# Defining percentage for Hufflepuff
if y == 1:
    Y = 100
elif y == 2:
    Y = 75
elif y == 3:
    Y = 25
else:
    Y = 50

# Quetion for Ravenclaw
z = int(input((
    "\n(c) You have an online exam the next day. And you are terribly sick. At the sametime you have to do well in the exam to maintain a good grade. \nThe teacher knows you as an honest one.What would you do to overcome this situation?"
    "\n\t1. As you have studied through the whole semester you have ideas. So, you'll see through the lecture videos.You'll not perform any unfair means in the exam and you'll not cheat."
    "\n\t2. You'll receive the lecture videos. You'll not perform any unfair means in the exam and you'll not cheat."
    "\n\t3. Even if you can't study you'll not cheat in the exam."
    "\n\t4. You won't break your teacher's trust and give a fair exam."
    "\nWhat will be your answer? Choose between option 1 to option 4: ")))

# Defining percentage for Ravenclaw
if z == 1:
    Z = 100
elif z == 2:
    Z = 75
elif z == 3:
    Z = 25
else:
    Z = 50

# Quetion for Slytherin
s = int(input((
    "\n(d) You've just completed graduation and you are looking for a job.You have some relatives who can help you to get the job. \nSo what would be yours to pursue the job?"
    "\n\t1. You want to achieve a higher post in a job with the help of your successful relatives and don't want to attain any competitive trial."
    "\n\t2. You just want to sneak in the job anyway and don't care about the post. So,along with your relatives you'll do anything possible to grab it."
    "\n\t3. You'll bribe the company and convince them to get that job."
    "\n\t4. You'll get into that company somehow and do every possible thing to reach the peak of success."
    "\nWhat will be your answer? Choose between option 1 to option 4: ")))

# Defining percentage for Slytherin
if s == 1:
    S = 100
elif s == 2:
    S = 75
elif s == 3:
    S = 25
else:
    S = 50

# Final assessment for house allocation
if X < 75 and Y < 75 and Z < 75 and S < 75:
    # Satisfying the 50-50 condition to declare a hatstall
    a = int(input(
        "Suppose you are playing a soccer match and your Team is losing it . You are the captain of the match and you have 15 minutes left. At least  you have to draw the match by scoring one goal. \nWhat would be your game-plan?"
        "\n\t1. Keep patience ,cheer the teammates, play with all your skills and finish the game fairly whatever the result comes. You are brave enough to accept any result."
        "\n\t2. You'll want to win the game somehow or other because losing is something you never learnt.You'll make tricky game-plans with your cleverness.You'll foul and tell your teammate to play rough and win it in any possible way."
        "\nWhat will be your answer? Choose between option 1 or option 2: "))
    print("\nYou are declared a hatstall! Best of luck!")
elif X > Y and X > Z and X > S:
    print("\nCongratulations! You are selected for Gryffindor.")
elif Y > X and Y > Z and Y > S:
    print("\nCongratulations! You are selected for Hufflepuff")
elif Z > Y and Z > X and Z > S:
    print("\nCongratulations! You are selected for Ravenclaw")
elif S > Y and S > Z and S > X:
    print("\nCongratulations! You are selected for Slytherin")
else:
    print("\nYou are declared a hatstall! Best of luck!")
# Code ends here
