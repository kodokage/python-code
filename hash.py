scores = {}
top_scorer = []
result_f = open('results.txt')

for line in result_f:
    (name, score) = line.split()
    scores[score] = name
    # top_scorer.append(score)
    

result_f.close()
# top_scorer.sort(reverse = True)
print("The top scores were: ")

for each_score in sorted(scores.keys(), reverse=True):
    print ('Surfer ' + scores[each_score] + ' scored ' + each_score)

# for top_score in top_scorer:
#     print(scores[top_score] + ' scored ' +top_score)
