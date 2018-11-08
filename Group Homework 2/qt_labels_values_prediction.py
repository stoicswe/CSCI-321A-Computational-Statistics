#! Christopher Ottesen
from projectq.ops import All, CNOT, H, Measure, X, Z
from projectq import MainEngine
import numpy as np


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


def send_full_message(message='DataEspresso.com',quantum_engine=''):
    # Convert the string into binary values
    binary_encoded_message = [bin(ord(x))[2:].zfill(8) for x in message]
    #print('Message to send: ', message)
    #print('Binary message to send: ', binary_encoded_message)

    received_bytes_list = []
    for letter in binary_encoded_message:
        received_bits = ''
        for bit in letter:
            received_bits = received_bits + str(send_receive(int(bit),quantum_engine))
        received_bytes_list.append(received_bits)

    binary_to_string = ''.join([chr(int(x, 2)) for x in received_bytes_list])
    #print('Received Binary message: ', received_bytes_list)
    #print('Received message: ', binary_to_string)
    return binary_to_string

# build a dictionary of dictionaries st d = { fw1 : {sw1 : p1, sw2: p2, .. }, .. }

# Using the simulator as quantum engine
def predict_data(data, probs, count=100):
    quantum_engine=MainEngine()
    print("Data")
    print(data)
    print("Probs")
    print(probs)
    print("Sending ===>")
    rx = []
    ry = []
    count = 10
    for i in range(count):
        percent = (i/count)*100
        if percent % count/count == 0:
            print("{0}% Completed...".format(percent))
        #w = np.random.choice(data)
        w = np.random.choice(data, 1, p=probs)[0] # record the values for comparison with predicted
        rx.append(send_full_message(message=w,quantum_engine=quantum_engine).split(",")[0])
        ry.append(send_full_message(message=w,quantum_engine=quantum_engine).split(",")[1])
    # prep the data to learn on it...
    # ["A,B","B,D","B,C"], sent from this
    # dataset at random from alice...
    # the resulting dataset that is generated
    # is a 2D dictionary that contains the
    # words as the keys and the counts as the
    # values. First level is the label, the second
    # is the word and the occurances of that combination
    learn = {}
    for i in range(len(rx)):
        for j in range(len(rx)):
            if i == j:
                if rx[i] in learn.keys():
                    if ry[j] in learn[rx[i]].keys():
                        learn[rx[i]][ry[j]] += 1
                    else:
                        learn[rx[i]][ry[j]] = 1
                else:
                    learn[rx[i]] = {ry[j] : 1}
    print("Recieved <===")
    print("Collected Data:")
    print(learn)

    # calculate the probs for each "event" that occurs
    fl_k = learn.keys()
    for fk in fl_k:
        sl_k = learn[fk].keys()
        for sk in sl_k:
            learn[fk][sk] = learn[fk][sk] / count

    # predict the word based on a random word that alice decides to send to bob
    w_predict = send_full_message(message=np.random.choice(list(learn.keys())),quantum_engine=quantum_engine)
    prob_dict = learn[w_predict]
    print("Probabilities:")
    print(prob_dict)
    print("Prediction on word: {0} results in expected word: {1}".format(w_predict, np.random.choice(list(prob_dict.keys()), 1, p=list(prob_dict.values()))))

# call the function to predict on a data:
predict_data(["Read,A","Read,B","Read,C","Read,D","Read,E"], [0.05, 0.3, 0.4, 0.2, 0.05])
predict_data(["Watch,Movie","Read,Book","See,Shows","Read,Magazine","Listen,Song"], [0.05, 0.3, 0.4, 0.2, 0.05])
#predict_data(["A,B","B,D","B,C"])