from TownsDataset import TownsDataset
from simpleNet import simpleNet
from simpleConv import simpleConv
import torch
from torch.utils.data import DataLoader
import numpy as np
import pickle
from matplotlib import pyplot as plt

train_data = pickle.load(open(r"data\train_data.pkl", "rb"))
train_labels = pickle.load(open(r"data\train_labels.pkl", "rb"))
val_data = pickle.load(open(r"data\val_data.pkl", "rb"))
val_labels = pickle.load(open(r"data\val_labels.pkl", "rb"))


train_dl = DataLoader(dataset=TownsDataset(train_data, train_labels), batch_size=32, shuffle=True)
val_dl = DataLoader(dataset=TownsDataset(val_data, val_labels), batch_size=64)


train_label_count = TownsDataset(train_data, train_labels).num_labels

#weigh the labels for loss function to avoid bias
weight = np.sqrt(1/(train_label_count / sum(train_label_count)))

#prepare training
net = simpleNet()
epochs = 100
train_loss = torch.zeros(epochs)
train_acc = torch.zeros(epochs)

val_loss = torch.zeros(epochs)
val_acc = torch.zeros(epochs)

optimizer = torch.optim.Adam(net.parameters())
loss_fn = torch.nn.CrossEntropyLoss(weight)

#training loop
for epoch in range(epochs):
    net.train()
    for word, label in train_dl:
        prediction = net(word.float())
        loss = loss_fn(prediction, label.long())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss[epoch] += loss.detach()
        lbl_pred = torch.argmax(prediction, dim = 1)
        train_acc[epoch] += sum(lbl_pred == label)
    if epoch % 20 == 0:
        print("Current Epoch: " + str(epoch))

    net.eval()
    #validation loop
    for word, label in val_dl:
        with torch.no_grad():
            prediction = net(word.float())
            loss = loss_fn(prediction, label.long())

        val_loss[epoch] += loss.detach()
        lbl_pred = torch.argmax(prediction, dim = 1)
        val_acc[epoch] += sum(lbl_pred == label)

train_loss /= len(train_dl) * train_dl.batch_size
train_acc /= len(train_dl) *train_dl.batch_size

val_loss /= len(val_dl.dataset)
val_acc /= len(val_dl.dataset)


def plot_training_progress(train_loss: torch.Tensor, train_acc: torch.Tensor, val_loss: torch.Tensor, val_acc: torch.Tensor):
    labels = ['training', 'validation']
    fig, axs = plt.subplots(2, 1, sharex=True)

    axs[0].plot(torch.arange(len(train_loss)), train_loss, val_loss)
    axs[0].legend(labels)
    axs[0].set_title('Loss')
    axs[0].set_ylabel('crossentropy loss')

    axs[1].plot(torch.arange(len(train_acc)), train_acc, val_acc)
    axs[1].legend(labels)
    axs[1].set_title('Accuracy')
    axs[1].set_xlabel('epoch')

    plt.show()

plot_training_progress(train_loss, train_acc, val_loss, val_acc)

torch.save(net.state_dict(), "model\params.model")