import torch

def create_model():
    return None # your model building code
model = create_model()

# save
torch.save(model.state_dict(), "model.pth")

# load
model = create_model()
model.load_state_dict(
    torch.load("model.pth", weights_only=True))
model.eval() # for inference

