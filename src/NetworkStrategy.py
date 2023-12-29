import random


class Neuron():
    next = []
    weight = 0.0

    def __init__(self, next, weight):
        self.weight = weight
        self.next = next


    def activateNeuron(self, activation):
        for neuron in self.next:
            neuron.activateNeuron(self.weight * activation)


class EndNeuron():
    answer = None
    activation = 0.0

    def __init__(self, answer):
        self.answer = answer

    def activateNeuron(self, activation):
        self.activation += activation



class Network():
    neurons = []
    knownAnswers = []
    synapseMax = 5
    synapseMin = 0
    size = 0
    layer = 0


    def __init__(self, size, layer):
        self.size = size
        self.layer = layer
        # create the initial layer
        self.neurons.append(self.createNeuronLayer(size))
        # create the hidden layers
        for x in range(layer):
            self.neurons.append(self.createNeuronLayer(size * (layer - x) // 20))
        # create the end layer
        self.neurons.append(self.createEndNeuronLayer(size // 20))
        # relate the neurons
        for i in range(layer + 1):
            for n in self.neurons[i]:
                n.next += random.choices(self.neurons[i+1], k=random.randint(self.synapseMin, self.synapseMax))


    def createNeuronLayer(self, size):
        nlist = []
        for _ in range(size):
            neuron = Neuron([], random.random())
            nlist.append(neuron)
        return nlist


    def createEndNeuronLayer(self, size):
        nlist = []
        for _ in range(size):
            neuron = EndNeuron(None)
            nlist.append(neuron)
        return nlist


    def learn(self, input, answer):
        self.resetEndNeurons()
        if answer.lower() in self.knownAnswers:
            # strengthen
            print("a")
        else:
            # build a new path to an empty end neuron
            self.knownAnswers.append(answer.lower())
            self.activateNeurons(input)
            biggest = 0
            SetNeuron = None
            for neuron in self.neurons[self.layer + 1]:
                if neuron.activation > biggest:
                    biggest = neuron.activation
                    SetNeuron = neuron
                    print(neuron.activation)
            SetNeuron.answer = answer


    def compare(self, input, answer):
        self.resetEndNeurons()
        self.activateNeurons(input)
        biggest = 0
        SetNeuron = None
        for neuron in self.neurons[self.layer + 1]:
            if neuron.activation > biggest:
                biggest = neuron.activation
                SetNeuron = neuron
        if SetNeuron.answer == answer:
            return 1
        else:
            return 0

    def activateNeurons(self, input):
        for i in range(self.size):
            self.neurons[0][i].activateNeuron(input[i])


    def resetEndNeurons(self):
        for neuron in self.neurons[self.layer + 1]:
            neuron.activation = 0.0
