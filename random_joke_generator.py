import random

def get_random_joke():
    """
    Returns a random programming or Python joke from a predefined list.
    """
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
        "Why do Python programmers wear glasses? Because they can't C#.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Debugging: Removing the needles from the haystack, only to realize you put them there in the first place.",
        "What's a programmer's favorite place to hang out? Foo Bar.",
        "Why did the web developer break up with the database? They had commitment issues.",
        "What do you call a developer who's always angry? A full-stack overflow.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "Why did the Python program break up with the C++ program? It couldn't handle the pointers.",
        "What's a Python developer's favorite martial art? Py-thon!",
        "Why did the programmer quit his job? He didn't get arrays.",
        "My code works, I have no idea why.",
        "My code doesn't work, I have no idea why.",
        "Knock, knock. Who's there? Kilo. Kilo who? Kilo-byte me!",
        "What's a programmer's favorite snack? Microchips.",
        "How do you comfort a JavaScript bug? You console it.",
        "Why are a programmer's eyes always red? Because they don't like 'em, they just type 'em.",
        "Why was the computer cold? It left its Windows open!"
    ]
    
    # Use random.choice to select a random element directly from the list
    return random.choice(jokes)

# Main part of the script
if __name__ == "__main__":
    print("🐍 Welcome to the Python Joke Dispenser! 💻\n")
    print(get_random_joke())
    print("\n--- End of Joke ---")
