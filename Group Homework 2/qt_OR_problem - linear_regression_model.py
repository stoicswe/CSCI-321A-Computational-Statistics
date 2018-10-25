#! Christopher Ottesen
from projectq.ops import All, CNOT, H, Measure, X, Z
from projectq import MainEngine
from sklearn.linear_model import LogisticRegression
import numpy as np

class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activiation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

def create_bell_pair(quantum_engine):
    # Qubit one is 'Alices' qubit, and will be used to create a message state
    qubit_one = quantum_engine.allocate_qubit()
    # Qubit two is 'Bobs' qubit, and will be used to re-create the message state
    qubit_two = quantum_engine.allocate_qubit()
    H | qubit_one
    CNOT | (qubit_one, qubit_two)

    return qubit_one, qubit_two

def create_message(quantum_engine='', qubit_one='', message_value=0):
    qubit_to_send = quantum_engine.allocate_qubit()
    if message_value == 1:
        X | qubit_to_send

    # entangle the original qubit with the message qubit
    CNOT | (qubit_to_send, qubit_one)
    H | qubit_to_send
    Measure | qubit_to_send
    Measure | qubit_one

    # The qubits are now turned into normal bits we can send through classical channels
    classical_encoded_message = [int(qubit_to_send), int(qubit_one)]

    return classical_encoded_message

def message_reciever(quantum_engine, message, qubit_two):
    if message[1] == 1:
        X | qubit_two
    if message[0] == 1:
        Z | qubit_two
    
    Measure | qubit_two

    quantum_engine.flush()

    received_bit = int(qubit_two)
    return received_bit


def send_receive(bit=0,quantum_engine=''):
    # Create bell pair
    qubit_one, qubit_two = create_bell_pair(quantum_engine)
    # entangle the bit with the first qubit
    classical_encoded_message = create_message(quantum_engine=quantum_engine, qubit_one=qubit_one, message_value=bit)
    # Teleport the bit and return it back
    return message_reciever(quantum_engine, classical_encoded_message, qubit_two)


def phone_mars(message='DataEspresso.com',quantum_engine=''):
    binary_encoded_message = [bin(ord(x))[2:].zfill(8) for x in message]
    received_bytes_list = []
    for letter in binary_encoded_message:
        received_bits = ''
        for bit in letter:
            received_bits = received_bits + str(send_receive(int(bit),quantum_engine))
        received_bytes_list.append(received_bits)
    binary_to_string = ''.join([chr(int(x, 2)) for x in received_bytes_list])
    return str(binary_to_string)

def phone_home(message='DataEspresso.com',quantum_engine=''):
    binary_encoded_message = [bin(ord(x))[2:].zfill(8) for x in message]
    received_bytes_list = []
    for letter in binary_encoded_message:
        received_bits = ''
        for bit in letter:
            received_bits = received_bits + str(send_receive(int(bit),quantum_engine))
        received_bytes_list.append(received_bits)
    binary_to_string = ''.join([chr(int(x, 2)) for x in received_bytes_list])
    return str(binary_to_string)

train = [["0,0,0"],["0,1,1"],["1,0,1"],["1,1,1"]]
y_train = [["0"],["1"],["1"],["1"]]

test = train
y_test = y_train
quantum_engine=MainEngine()
clf = LogisticRegression()
print("Alice:")
print(phone_mars(message="Hey, did you start the machine learning homework Dr. Hu assigned?", quantum_engine=quantum_engine))
print("Bob:")
print(phone_home(message="Sh*t i didnt get to do it yet...let me start!", quantum_engine=quantum_engine))
print(phone_home(message="Send me the data!", quantum_engine=quantum_engine))
print("Training on the data...")
error = 50
epoch = 0
while error > 0:
    index = 0
    data_to_send = train[index]
    data_recieved = phone_mars(message=data_to_send[0], quantum_engine=quantum_engine)
    data_recieved = data_recieved.split(",")
    td = [int(data_recieved[0]), int(data_recieved[1])]
    lb = int(data_recieved[2])

    index2 = np.random.choice([1,2,3])
    data_to_send2 = train[index2]
    data_recieved2 = phone_mars(message=data_to_send2[0], quantum_engine=quantum_engine)
    data_recieved2 = data_recieved2.split(",")
    td2 = [int(data_recieved2[0]), int(data_recieved2[1])]
    lb2 = int(data_recieved2[2])

    td = [td, td2]
    lb = [lb, lb2]
    print(td)
    print(lb)

    clf_model = clf.fit(td, lb)
    clf = clf_model

    error_str = phone_home(message=str(1 - clf.score(td,lb)), quantum_engine=quantum_engine)
    error = float(error_str)
    print("------------------------")
    print("Epoch: ", epoch)
    print("Model Error: ", error)
    epoch += 1

test_x = []
test_y = []
for t in train:
    data_recieved = phone_mars(message=t[0], quantum_engine=quantum_engine)
    td = [int(data_recieved[0], 10), int(data_recieved[1], 10)]
    lb = [int(data_recieved[2], 10)]
    test_x.append(td)
    test_y.append(lb)
pred_y = clf.predict(test_x)

isAccurate = True
for i in range(len(pred_y)):
    if pred_y[i] != test_y[i]:
        isAccurate = False
res = "accurate."
if isAccurate == False:
    res = "not accurate."
print("Bob's model is ", res)