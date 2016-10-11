from csv import *
def posterior(prior, likelihood, observation):
    probs = [x for x in zip(likelihood, observation)]
    ptrue = 1
    pfalse = 1
    for i in probs:
        if i[1]:
            ptrue *=(i[0][True])
            pfalse *=(i[0][False])
        else:
            ptrue *= (1-i[0][True])
            pfalse *= (1-i[0][False])

    posterior_prob = (ptrue * prior) / ((ptrue * prior) + (pfalse * (1 - prior)))
    return posterior_prob

#prior = 0.05
#likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

#observation = (False, False, True)

#class_posterior_true = posterior(prior, likelihood, observation)
#print("P(C=False|observation) is approximately {:.5f}"
      #.format(1 - class_posterior_true))
#print("P(C=True |observation) is approximately {:.5f}"
      #.format(class_posterior_true)) 
      

def learn_prior(file_name, pseudo_count = 0):
    file = open(file_name)
    training_examples = [tuple(line) for line in reader(file)][1:]

    count = len(training_examples) + (pseudo_count*2)
    spam = 0
    for item in training_examples: 
        if item[-1] == '1':
            spam += 1
    spam += pseudo_count

    return spam/count


def accuracy(predicted_labels, correct_labels):
    predlen = len(predicted_labels)
    corlen = len(correct_labels)
    totalprob = 0
    for i in range(predlen):
        totalprob = totalprob + 1 if predicted_labels[i] == correct_labels[i] else totalprob 
    return totalprob / corlen

#print(accuracy((True, False, True, False),
               #(True, True, False, False)))

