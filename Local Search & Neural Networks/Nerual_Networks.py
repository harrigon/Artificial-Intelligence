def learn_perceptron(weights, bias, training_examples, learning_rate, max_epochs):

    for epoch in range(1, max_epochs + 1):
        # print("-" * 20, "epoch:", epoch, 20 * "-")
        # print("weights: ", weights)
        # print("bias: ", bias)
        seen_error = False
        for input, target in training_examples:
            a = bias
            for i in range(len(input)):
                a += input[i]*weights[i]

            if a >= 0:
                output = 1
            else:
                output = 0
            # print("input: {} output: {} target: {}".format(
            #    input, output, target))
            if output != target:
                seen_error = True
                # Now update the weights and bias
                for i in range(len(weights)):
                    weights[i] = weights[i] + learning_rate*input[i]*(target - output)
                # weights =
                bias = bias + learning_rate*(target - output)
                # print("updating the weights and bias to: ", weights, bias)

        if not seen_error:
            def perceptron(input_vector):
                a = bias
                for i in range(len(input_vector)):
                    a += input_vector[i]*weights[i]

                if a >= 0:
                    output = 1
                else:
                    output = 0
                return output
            return perceptron

# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#   ((0, 0), 0),
#   ((0, 1), 0),
#   ((1, 0), 0),
#   ((1, 1), 1),
#   ]
# max_epochs = 50
#
# classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
# if not classifier:
#   print("No model could be learnt.")
# else:
#   print(classifier((0,0)))
#   print(classifier((0,1)))
#   print(classifier((1,0)))
#   print(classifier((1,1)))
#   print(classifier((2,2)))
#   print(classifier((-3,-3)))
#   print(classifier((3,-1)))

# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#   ((0, 0), 0),
#   ((0, 1), 0),
#   ((1, 0), 0),
#   ((1, 1), 1),
#   ]
# max_epochs = 50
#
# classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
# if not classifier:
#   print("No model could be learnt.")
# else:
#   print(classifier((0,0)))
#   print(classifier((0,1)))
#   print(classifier((1,0)))
#   print(classifier((1,1)))
#   print(classifier((2,2)))
#   print(classifier((-3,-3)))
#   print(classifier((3,-1)))
#
# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#   ((0, 0), 0),
#   ((0, 1), 1),
#   ((1, 0), 1),
#   ((1, 1), 0),
#   ]
# max_epochs = 50
#
# classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
# if not classifier:
#   print("No model could be learnt.")
# else:
#   print(classifier((0,0)))
#   print(classifier((0,1)))
#   print(classifier((1,0)))
#   print(classifier((1,1)))
#   print(classifier((2,2)))
#   print(classifier((-3,-3)))
#   print(classifier((3,-1)))
#
# weights = [1, 1]
# bias = -2
# learning_rate = 0.5
# examples = [
#   ((0, 4), 0),
#   ((-2, 1), 1),
#   ((3, 5), 0),
#   ((1, 1), 1),
#   ]
# max_epochs = 50
#
# classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
# if not classifier:
#   print("No model could be learnt.")
# else:
#   print(classifier((0,4)))
#   print(classifier((-2,1)))
#   print(classifier((3,5)))
#   print(classifier((1,1)))
#   print(classifier((4,4)))
#   print(classifier((-3,6)))
#   print(classifier((3,-1)))
