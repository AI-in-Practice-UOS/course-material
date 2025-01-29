from transformers import AutoModel, AutoTokenizer

# load from hugging face
model = AutoModel.from_pretrained("hf_model")
tokenizer = AutoTokenizer.from_pretrained("hf_model")

# save
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")

# load
model = AutoModel.from_pretrained("./model")
tokenizer = AutoTokenizer.from_pretrained("./model")

