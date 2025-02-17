from extract import ExtractInterface
from year_data import YearData
from year_list import YearList

# class Manual(ExtractInterface):
#
#     def find_years(self, text):
#         n_digites = 0
#         year_start, year_end = 0, 0
#         year = ""
#         year_list = YearList()
#         for i in range(0, len(text)):
#             c = text[i]
#             if c.isnumeric():
#                 if n_digites > 4:
#                     n_digites = 0
#                     year = ""
#                     continue
#                 if n_digites == 0:
#                     year_start = i
#                 n_digites += 1
#                 year += c
#             else:
#                 if n_digites > 0 and n_digites <= 4:
#                     year_end = i - 1
#                     try:
#                         year = int(year)
#
#                         year_data = YearData(year, year_start, year_end)
#                         year_list.add_year(year_data)
#                     except:
#                         raise TypeError("could not parse, year is not a number")
#                 n_digites = 0
#                 year = ""
#         return year_list

import torch.optim as optim
from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

criterion = nn.CrossEntropyLoss()

# optimizer = optim.Adam(net.parameters(), lr=0.001)

batch_size = 4
trainloader_A = torch.utils.data.DataLoader(My_Dataset(ds_A.images[:20], ds_A.labels[:20]), batch_size=batch_size, shuffle=False, num_workers=2)

def train_function(number_of_epochs, trainloader):
    for epoch in range(number_of_epochs):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            print(f'Epoch [{(epoch + 1)}/{number_of_epochs}] loss: {running_loss / len(trainloader)}')

from torch.utils.data import Dataset

class My_Dataset(Dataset):
    def __init__(self, images, labels, transform=None):
        self.images = images
        self.set_labels(labels)
    
    def set_labels(self, labels):
        if len(labels) == 1:
            self.labels = labels * len(self.images)
        else:
            self.labels = labels

    @staticmethod
    def append(images1, images2, labels1, labels2):
        images = []
        labels = []
        
        n = len(images2)
        for i in range(n):
            images.append(images1[i])
            labels.append(labels1[i])
            images.append(images2[i])
            labels.append(labels2[i])
            i += 1
        return My_Dataset(images, labels)

    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]

    @property
    def classes(self):
        return self.images.classes
