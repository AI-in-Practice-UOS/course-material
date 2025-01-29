
from transformers import TFAutoModelForCausalLM, PreTrainedTokenizerFast


def gpt2_inference(
    model: TFAutoModelForCausalLM, 
    tokenizer: PreTrainedTokenizerFast, 
    message: str, 
    max_length: int
) -> str:
    """Generate text using a GPT-2 model.

    This function takes a fine-tuned GPT-2 model and its tokenizer to generate a response 
    based on an input message. It employs nucleus sampling (`top_k=50`), temperature scaling (`temperature=0.7`), 
    and prevents repeated n-grams (`no_repeat_ngram_size=2`).

    Args:
        model (TFAutoModelForCausalLM): A TensorFlow-based GPT-2 model for causal language modeling.
        tokenizer (PreTrainedTokenizerFast): A tokenizer compatible with GPT-2 (usually loaded via `AutoTokenizer`).
        message (str): The input message to generate a response for.
        max_length (int): The maximum length of the generated response.

    Returns:
        str: The generated text response.
    """

    # tokenize input
    inputs = tokenizer(
        message,
        return_tensors="tf",
        return_attention_mask=True
    )

    # generate text using model
    output = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        do_sample=True,
        top_k=50
    )

    # decode generated text
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded_output
