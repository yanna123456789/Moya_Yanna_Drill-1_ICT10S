from pyscript import document 

def compute_average(event):
    #Get the input values and convert to float
    score1 = float(document4.getElementById("score1").value)
    score2 = float(document4.getElementById("score2").value)

    #Compute for the average 
    average = (score1 + score2) / 2

    #Determine if pass/fail
    if average >= 75:
        result = "Passed"
    else:
        result = "Failed"