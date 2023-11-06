gryffindor = 0
hufflepuff = 0
slytherin = 0
ravenclaw = 0 

while True:
    try:
        Q1 = int(input('''
                    Do you like Dawn or Dusk?
                    1) Dawn
                    2) Dusk
                    '''))
        if Q1 in [1, 2]:
            break
        else:
            print("Please choose 1 or 2")
    except ValueError:
        print("Please choose 1 or 2")

if Q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif Q1 ==2:
    hufflepuff += 1
    slytherin += 1

while True:
    try:
        Q2 = int(input('''
                    When I'm dead, I want people to remember me as:
                    1) The Good
                    2) The Great
                    3) the Wise
                    4) The Bold
                    '''))
        if Q2 in [1, 2, 3, 4]:
            break
        else:
            print("Please choose 1 or 2")
    except ValueError:
        print("Please choose 1, 2, 3, or 4")

if Q2 == 1:
    hufflepuff += 2
elif Q2 == 2:
    slytherin += 2
elif Q2 == 3:
    ravenclaw += 2
elif Q2 == 4:
    gryffindor += 2

while True:
    try:
        Q3 = int(input('''
                    Which instrument  most pleases your ear?
                    1) The violin
                    2) The trumpet
                    3) The piano
                    4) The drum
                    '''))
        if Q3 in [1, 2, 3, 4]:
            break
        else:
            print("Please choose 1 or 2")
    except ValueError:
        print("Please choose 1, 2, 3, or 4")

if Q3 == 1:
    slytherin += 4
elif Q3 == 2:
    hufflepuff += 4
elif Q3 == 3:
    ravenclaw += 4
elif Q3 == 4:
    gryffindor += 4

if (
    hufflepuff > slytherin and
    hufflepuff > ravenclaw and
    hufflepuff > gryffindor
):
    print("silly ass hufflepuff kid")
elif (
    slytherin > hufflepuff and
    slytherin > gryffindor and
    slytherin > ravenclaw 
):
    print("ohhh u suck youre in slytherin")
elif (
    ravenclaw > slytherin and
    ravenclaw > hufflepuff and
    ravenclaw > gryffindor
):
    print("ur so boring lol ravenclaw")
elif (
    gryffindor > slytherin and
    gryffindor > hufflepuff and
    gryffindor > ravenclaw
):
    print ("try hard ur in gryffindor")




