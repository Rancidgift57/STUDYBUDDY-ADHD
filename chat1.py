from transformers import AutoTokenizer, AutoModelForCausalLM

# Replace with "meta-llama/Llama-2-7b" or other model sizes if available
model_name = "meta-llama/Llama-2-7b-hf"

# Load the tokenizer and the model in 8-bit precision
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",          # Automatically map layers to available GPUs
    load_in_8bit=True           # Load in 8-bit precision
)