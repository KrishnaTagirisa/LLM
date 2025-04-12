from ctransformers import AutoModelForCausalLM

model_path =r"/Users/krishnatagirisa/PyWS/LLM/llama-2-7b-chat.Q3_K_M.gguf"



model = AutoModelForCausalLM.from_pretrained(
    model_path,
    model_type="llama",
    gpu_layers=0  # Run on CPU
)
response = model("Tell me a joke about AI.")
print(response)