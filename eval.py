import argparse
import numpy as np
import pandas as pd
import torch

from train import a

vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o'])

d = {}
for e, u in enumerate(vowels):
    d[e] = u


def g2(x, p, desired_len):
    z = np.zeros(desired_len)
    z[p.index(x)] = 1
    return z

def b2(u, p, desired_len):
    gt = []
    gr = []
    for v in range(len(u) - 4):
        if u[v+2] not in vowels:
            continue
        
        h2 = vowels.index(u[v+2])
        gt.append(h2)
        r = np.concatenate([g2(x, p, desired_len) for x in [u[v], u[v+1], u[v+3], u[v+4]]])
        gr.append(r)

    return np.array(gr), np.array(gt) # features, classes

def new_text(output_file, data, predictions_list):
    
    count = 0
    new_text = []

    for character in data:
        if character in vowels:
            new_text.append(d[predictions_list[count]])
            count += 1
        elif character == '<s>' or character == '<e>':
            pass
        else:
            new_text.append(character)

    with open(output_file, 'w') as f:
        f.write(''.join(new_text))


def calculate_accuracy(real_v, predicted_v):
    total = len(real_v)
    yay = 0
    for v1, v2 in zip(real_v, predicted_v):
        if v1 == v2:
            yay +=1
    
    return(yay/total*100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str)
    parser.add_argument("train_data", type=str)
    parser.add_argument("test_data", type=str)
    parser.add_argument("output", type=str)
    args = parser.parse_args()

    # Load a model produced by train.py
    model = torch.load(args.model)
    model.eval() # from the internet, no idea what it does tbh

    # Load the test data
    tokenized_test_data = a(args.test_data)

    # Create evaluation instances compatible with the training instances
    tokenized_train_data = a(args.train_data)
    desired_len = len(tokenized_train_data[1])

    tokenized_test_data = a(args.test_data)
    arrays_test_data = b2(tokenized_test_data[0], tokenized_test_data[1], desired_len)

    tensor_test_data_features = torch.from_numpy(arrays_test_data[0])

    # Use the model to predict instances
    outputs = model(tensor_test_data_features.float()) # .float() to solve "RuntimeError: expected scalar type Float but found Double"
    predictions = pd.Series(outputs.squeeze(0).argmax(dim=1).numpy()) # from demo4
    predictions_list = predictions.tolist()

    # Write the text with the predicted (as opposed to the real) vowels back into an output file.
    test_characters = tokenized_test_data[0]
    new_text(args.output, tokenized_test_data[0], predictions_list)

    print('The text with the predicted vowels is saved in ' + args.output)

    # Print the accuracy of the model to the terminal.
    real_deal = arrays_test_data[1]
    real_deal_list = real_deal.tolist()
    accuracy = calculate_accuracy(real_deal_list, predictions_list)

    print('Accuracy: ' + str(accuracy) + '%')
