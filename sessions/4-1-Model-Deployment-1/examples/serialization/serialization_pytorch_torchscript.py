import torch

model = None # your model

# export and save
model_scripted = torch.jit.script(model)
model_scripted.save("model_scripted.pth")

# load
model = torch.jit.load("model_scripted.pth")
model.eval() # for inference

