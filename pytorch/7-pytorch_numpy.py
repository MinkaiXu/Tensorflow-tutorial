import torch
import numpy as np

np_data = np.arange(6).reshape((3, 2))
torch_data = torch.from_numpy(np_data)

print(np_data)
print(torch_data)