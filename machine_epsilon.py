# TODO
epsilon = 1.0

while (1.0 + 0.5 * epsilon) != 1.0:
    previous_epsilon = epsilon
    epsilon *= 0.5

print("Machine Epsilonは{}です".format(previous_epsilon))
