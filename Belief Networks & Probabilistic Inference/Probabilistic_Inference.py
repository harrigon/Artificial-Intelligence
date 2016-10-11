import itertools

def joint_prob(network, assignment):
    joint_prob = 1
    for i in assignment.keys():
        current = network[i]
        parents_tuple = parents_info(network, assignment, i)

        prob = current['CPT'].get(parents_tuple)

        if assignment[i] == True:
            joint_prob *= prob
        else:
            joint_prob *= (1-prob)
    return joint_prob


def parents_info(network, assignment, current):
    return_tuple = []
    for i in network[current]['Parents']:
        if assignment[i] == True:
            return_tuple.append(True)
        else:
            return_tuple.append(False)

    return tuple(return_tuple)




def query(network, query_var, evidence):


    q2 = query_helper(network, query_var, evidence)
    # q2 = query_helper(network, query_var, evidence)
    evidence[query_var] = True
    q1T = query_helper(network, query_var, evidence)
    evidence[query_var] = False
    q1F = query_helper(network, query_var, evidence)
    #print(q1F, q1T)
    probF = q1F/q2
    probT = q1T/q2
    return (probF, probT)

def query_helper(network, query_var, temp):
    evidence = temp.copy()
    #print(network.keys() - evidence.keys())
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    #if hidden_vars:
        #print("hidden vars", hidden_vars)

    if len(hidden_vars) == 0:
        probT = 0

        probT +=joint_prob(network, evidence)


    else:
        probT = 0
        hidden_vars = network.keys() - evidence.keys()
        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            for i in hidden_assignments:
                evidence[i] = hidden_assignments[i]

                probF = 0
                #orig = joint_prob(temp, evidence)

            probT +=joint_prob(network, evidence)


    return probT

network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001
        }},

    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 0.01,
        }},
}
answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))
answer = query(network, 'Disease', {'Test': False})
print("The probability of having the disease\n"
      "if the test comes back negative: {:.8f}"
      .format(answer[True]))
