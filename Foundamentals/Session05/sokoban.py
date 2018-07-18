# Set function ( dat bien )
map = {
    "size_x" : 5,
    "size_y" : 5
}

player = {"x":2,"y":4}

boxes = [
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3}
]

destinations =[
    {"x":2,"y":1},
    {"x":3,"y":2},
    {"x":4,"y":3}
]

playing = True 

# Set map

while playing :



    for y in range (map["size_y"]) :
        for x in range(map["size_x"]) :
            
            destination_is_here = False
            for des in destinations :
                if des['x']==x and des['y']==y :
                    destination_is_here = True

            box_is_here = False
            for box in boxes :
                if box['x'] == x and box['y'] == y :
                    box_is_here = True 

            
            
            player_is_here = False


            if x== player['x'] and y == player['y'] :
                    player_is_here = True 
            

            if player_is_here == True :
                print("P ",end="")
            elif box_is_here == True :
                print("B ",end="")
            elif destination_is_here == True :
                print("D ",end="")
            else :
                print("- ",end="")
            
        
        print()
    
    
    # check win
    win = True 
    for box in boxes :
        if box not in destinations :
            win = False 
    
    if win == True :
        print ("You win !!!!")
        break

    # input
    move = input("Your move : ").lower()

    dx = 0
    dy = 0
    count = 0

    # Set move 
    if move =="w" :
        dy = -1
    elif move =="s" :
        dy = 1
    elif move =="a" :
        dx = -1
    elif move =="d" :
        dx = 1
    else :
        print("Ezzz")
        playing = False 

    if 0 <= player['x'] +dx < map['size_x'] \
        and 0 <= player['y'] +dy < map['size_y'] :
            player ['x'] += dx

            player ['y'] += dy 
    
    for box in boxes :

        if player['x'] == box ['x'] \
        and player['y'] == box ['y'] :
            box['x'] += dx
            box['y'] += dy

    # cach 1
    # for box in boxes :
    #     for des in destinations :
    #         if box['x'] == des['x'] \
    #         and box['y'] == des['y'] :
    #             count += 1
    #             if count == 3 :
    #                 print ("you win")
    #                 playing = False

        


    



