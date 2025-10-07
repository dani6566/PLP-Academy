import numpy as np          # For numerical operations and arrays
import pandas as pd         # For data manipulation and tables (DataFrames)
import matplotlib.pyplot as plt # For creating plots and graphs
import requests             # For fetching data from the web (APIs)


print("\n NumPy:")

# creates an array starting at 1 and ending before 11 (so, 1 to 10).
numbers_array = np.arange(1, 11)

print(f"  Created Array (1 to 10): {numbers_array}")

# Calculate the mean (average) of the array
array_mean = numbers_array.mean()

print(f"  Calculated Mean (Average): {array_mean:.2f}")


# PANDAS
print("\n Pandas")

# Create a small dataset using a Python dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Score': [85.5, 92.0, 78.5, 95.0]
}

# Load the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

print(df.head(3)) # Display only the first three rows

# Display summary statistics (like count, mean, min, max) 
print("\n  Summary Statistics for Numerical Data:")
print(df.describe())


# TASK 3: REQUESTS(Fetching Web Data)
print("\n Requests Demo:")

# The URL of a public test API endpoint (returns a sample blog post)
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

print(f"  Fetching data from: {api_url}")

try:
    # Make the HTTP GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the JSON response text into a Python dictionary
        data = response.json()
        
        # Extract and print a key piece of information (the 'title' of the post)
        title = data.get('title', 'Title Not Found')
        print(f"  Successfully fetched post title:")
        print(f"  Title: '{title}'")
    else:
        print(f"  Error: Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"  An error occurred during the request: {e}")


# MATPLOTLIB 

print("\n Matplotlib:")

# Data for the plot
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 1, 5, 3]

# Create the plot
plt.figure(figsize=(8, 4)) 

# Plot the data as a line graph
plt.plot(x_data, y_data, marker='o', linestyle='-', color='indigo')

# Add labels and a title for clarity
plt.title("Simple Line Graph Demonstration")
plt.xlabel("X Axis (Index)")
plt.ylabel("Y Axis (Value)")

# Add a grid to make the points easier to read
plt.grid(True)

# Show the plot window 
print("  Displaying the simple line graph (a new window/figure will open).")
plt.show()
