import random

position = []

p1_score = 0
p2_score = 0
p3_score = 0
p4_score = 0
name = []
p1_name = input("Enter player 1 name : ")
p2_name = input("enter player 2 name : ")
p3_name = input("enter player 3 name : ")
p4_name = input("enter player 4 name : ")
name.append(p4_name)
name.append(p3_name)
name.append(p2_name)
name.append(p1_name)

max_score = 50 

while(p1_score < max_score or p2_score < max_score or p3_score < max_score or p4_score < max_score):

    def dice():
        return random.randrange(1,7)


    #Player 1
    print(p1_name, " turn")

    if(p1_score < max_score):
        value1 = input('press r to roll the dice : ')

        if (value1 =="r"):
            dice1 = dice()
            print ("dice score:", dice1)
            if(p1_score + dice1 <= max_score):
                p1_score = p1_score + dice1
             

    print("Highest Score : ", p1_score)
    print("------------------------------")


    #Player 2

    print(p2_name," turn")
    if(p2_score < max_score):
        value2 =input("press r to roll the dice :")

        if (value2 =="r"):
            dice2 = dice()
            print ("dice score",dice2)
            if(p2_score + dice2 <= max_score):
                p2_score = p2_score + dice2
            


    print("Highest score :",p2_score)
    print("------------------------------")    



    #Player 3

    print(p3_name," turn")
    if(p3_score < max_score):
        value3 =input("press r to roll the dice :")

        if (value3 =="r"):
        
            dice3 = dice()
            print ("dice score",dice3)
            if(p3_score + dice3 <= max_score):
                p3_score = p3_score + dice3
                

    print("Highest score :",p3_score)
    print("------------------------------")    



    #Player 4

    print(p4_name," turn")
    if(p4_score < max_score):
        value4 =input("press r to roll the dice :")

        if (value4 =="r"):
        
            dice4 = dice()
            print ("dice score",dice4)
            if(p4_score + dice4 <= max_score):
                p4_score = p4_score + dice4
               

    print("highest score :",p4_score)
    print("------------------------------")


    if(p1_score == max_score):
        position.append(1)
        p1_score +=1

    if(p2_score == max_score):
        position.append(2)
        p2_score +=1
    if(p3_score == max_score):
        position.append(3)
        p3_score +=1
    if(p4_score == max_score):
        position.append(4)
        p4_score +=1
    
    


print("====================================")

print("\t\tGAME OVER")
print("1st -> ", name[position[3]-1])
print("2nd -> ", name[position[2]-1])
print("3rd -> ", name[position[1]-1])
print("4th -> ", name[position[0]-1])