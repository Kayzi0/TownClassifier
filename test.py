import torch
from simpleNet import simpleNet
import pickle
from TownsDataset import TownsDataset
from torch.utils.data import DataLoader
from decoder import decodeLabels, decodeTown

test_data = pickle.load(open(r"data\test_data.pkl", "rb"))
test_labels = pickle.load(open(r"data\test_labels.pkl", "rb"))
test_dl = DataLoader(dataset=TownsDataset(test_data,test_labels), batch_size= 64, shuffle=True)

net = simpleNet()
net.load_state_dict(torch.load("model\params.model"))
net.eval()


test_acc = 0.
show_pred_number = 10

for word, label in test_dl:
    with torch.no_grad():
        prediction = net(word.float())
        lbl_pred = torch.argmax(prediction, dim = 1)
        test_acc += sum(lbl_pred == label)
        

for i in range(show_pred_number):
    word_decode = decodeTown(word[i])
    label_decode = decodeLabels(int(label[i]))
    pred_decode = decodeLabels(int(lbl_pred[i]))
    print("Town Name: " + str(word_decode) + ";" +
            " Location: " + str(label_decode) + ";" +
            " Prediction: " + str(pred_decode))

test_acc /= len(test_dl.dataset)

print("Accuracy: " + str(float(test_acc)))

