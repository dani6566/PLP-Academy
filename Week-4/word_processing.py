def process_text_file(input_filename, output_filename):
      
    try:
        # Read all the text from the file into a variable
        with open(input_filename, 'r') as input_file:
            raw_text = input_file.read()
            
    except FileNotFoundError:
        # If the program can't find the file, it prints an error message and stops the function.
        print(f"ERROR: The file '{input_filename}' was not found. Make sure it exists!")
        return
        
    # Count the words in the original text
    
    # The .split() method breaks the text into a list of words.
    word_list = raw_text.split()
    word_count = len(word_list)
    
    #Convert the entire text to uppercase 
    processed_text = raw_text.upper()

    # --- Step 4: Write the processed text and count to the output file 
    try:
        with open(output_filename, 'w') as output_file:
            # First, write the final word count.
            output_file.write(f"TOTAL WORDS FOUND: {word_count} \n\n")
            
            # Next, write the entire uppercase block of text.
            output_file.write(processed_text)

        print(f"Success! The file was processed.")
        print(f"Word Count: {word_count}")
        print(f"Results saved to '{output_filename}'.")

    except Exception as e:
        print(f"An error occurred while writing the output file: {e}")


# The main part of the script that runs when you execute the file 
if __name__ == "__main__":
    INPUT_FILE_NAME = './input.txt'
    OUTPUT_FILE_NAME = './output.txt'

    process_text_file(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
