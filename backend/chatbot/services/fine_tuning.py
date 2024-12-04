import google.generativeai as genai
import time
import json
import os

# Path to your data.json file
data_json_path = '../../data.json'

# Step 1: Load the data from the data.json file
def load_data_from_json(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data

# Step 2: Prepare the training data from the JSON content
def prepare_training_data(data):
    # Convert data into the format expected by the tuning function (text_input and output)
    training_data = []
    
    for entry in data:
        # Assuming that your data has 'input_message' and 'generated_text' keys
        # If not, you should adjust this based on your data structure
        training_data.append({
            "text_input": entry["input_message"], 
            "output": entry["generated_text"]
        })
    
    return training_data

# Step 3: Fine-tune the model using the prepared data
def fine_tune_model(training_data):
    # Define the base model (the model you want to fine-tune)
    base_model = "models/gemini-1.5-flash-001-tuning"
    
    # Fine-tune the model with the training data
    operation = genai.create_tuned_model(
        display_name="increment",
        source_model=base_model,
        epoch_count=20,
        batch_size=4,
        learning_rate=0.001,
        training_data=training_data
    )

    # Wait for the fine-tuning operation to complete
    for status in operation.wait_bar():
        time.sleep(10)

    # Get the result of the operation
    result = operation.result()
    print(result)
    
    return result

# Step 4: Generate content using the fine-tuned model
def generate_content_with_tuned_model(model_name, input_text):
    # Create a model instance using the fine-tuned model
    model = genai.GenerativeModel(model_name=model_name)
    
    # Generate content based on the input text
    result = model.generate_content(input_text)
    print(result.text)  # Output the result
    
# Main execution
def main():
    # Load data from the data.json file
    data = load_data_from_json(data_json_path)
    
    # Prepare the training data from the loaded JSON data
    training_data = prepare_training_data(data)
    
    # Fine-tune the model with the prepared training data
    result = fine_tune_model(training_data)
    
    # Generate content using the fine-tuned model
    generate_content_with_tuned_model(result.name, "III")  # Example input

if __name__ == "__main__":
    main()
