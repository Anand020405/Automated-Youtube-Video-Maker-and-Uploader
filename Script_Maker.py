from gpt4all import GPT4All

IDEA_FILE = "ideas.txt"

def Script_Maker(File_name = IDEA_FILE):
    model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", device = 'gpu')

    with open(File_name, 'r') as Idea_file:
        ideas = Idea_file.read()


    prompt = f"Write 5 points to narrate on the topic {ideas} and i want the entire script to be strictly strictly less than 50 words and refine the grammar for the points"

    output = model.generate(prompt, max_tokens=1000, temp=0.7)
    with open(f"Scripts/script.txt", 'w') as Script:
        Script.write(output)
    
    print(f"Script done.")

if __name__ == "__main__":
    Script_Maker()