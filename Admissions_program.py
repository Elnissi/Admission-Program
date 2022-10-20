scores = input("Kindly Enter Your Scores")
splits = scores.split()
convert = [int(x) for x in splits]

score_length = len(splits)

sum = 0
for x in convert:
    sum += x
    
aggregate_score = round(sum / score_length)

if (aggregate_score >= 0) and (aggregate_score <= 49):
    print("NO ADMISSION!")
elif (aggregate_score >= 50) and (aggregate_score <= 54):
    print("You are eligible for admission into the Agriculutural Science Department!")
elif (aggregate_score >= 55) and (aggregate_score <= 60):
    print("You are eligible for admission into the Botany or Zoology Daepartment!")
elif (aggregate_score >= 61) and (aggregate_score <= 70):
    print("You are eligible for admission into the Psychology or Statistics Department!")
elif (aggregate_score >= 71) and (aggregate_score <= 74):
    print("You are eligible for admission into the Pharmacy,Physiology, Pharmacology or Nursing Department!")
elif (aggregate_score >= 75) and (aggregate_score <= 79):
    print("You are eligible for admission into the Banking & Finance, Insurance or Accountancy Department!")
elif (aggregate_score >= 80):
    print("You are eligible for admission into the Medicine or Law Department!")

