import torch
from simpleNet import simpleNet
import pickle
from TownsDataset import TownsDataset
from torch.utils.data import DataLoader

test_data = pickle.load(open(r"data\test_data.pkl", "rb"))
test_labels = pickle.load(open(r"data\test_labels.pkl", "rb"))
test_dl = DataLoader(dataset=TownsDataset(test_data,test_labels), batch_size= 64)

net = simpleNet()
net.load_state_dict(torch.load("model\params.model"))
net.eval()


test_acc = 0.

for word, label in test_dl:
    with torch.no_grad():
        prediction = net(word.float())
        lbl_pred = torch.argmax(prediction, dim = 1)
        test_acc += sum(lbl_pred == label)

test_acc /= len(test_dl.dataset)

print(test_acc)

