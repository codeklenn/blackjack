leaderboards = {} 

#function for writing the score to the leaderboards.
def writeHighscore(name,score):
    #an append is used and will only add the score in the leaderboards
    fh = open("scores.txt", "a")
    #new line is used before so that will will be shown below the scores
    fh.write("\n"+name+","+ str(score))
    fh.close()

def readHighscore():
    fh = open("scores.txt", "r")
    #for loop for reading each line of scores.txt
    for line in fh:
        #split() for splitting the values and returning it into a list
        user_score = line.split(",")
        #name for getting the first element of the list [name,score] = name
        name = user_score[0]
        #score for getting the second element of the list [name,score] = score
        score = user_score[1]
        #assign a name (key) to score (value)
        leaderboards[name] = int(score)
    fh.close()
    #return the leaderboards that will be used when the function is called in the main file.
    return leaderboards
