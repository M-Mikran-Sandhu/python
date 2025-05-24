from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a small GPT model
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Chat history for context (optional for basic use)
chat_history = ""

print("Mini ChatGPT - type 'exit' to quit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history += f"User: {user_input}\nBot:"
    input_ids = tokenizer.encode(chat_history, return_tensors="pt").to(device)

    # Generate a response (limit tokens to prevent long replies)
    output = model.generate(
        input_ids,
        max_length=input_ids.shape[1] + 50,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id,
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract only the bot's latest reply
    bot_reply = response[len(chat_history):].split("User:")[0].strip()
    print("Bot:", bot_reply)

    # Update chat history
    chat_history += f" {bot_reply}\n"
