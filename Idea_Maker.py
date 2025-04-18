from gpt4all import GPT4All


IDEA_FILE = "ideas.txt"

def Ideas(File_name = IDEA_FILE):
    '''
    Creating ideas for youtube video
    '''

    model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", device = 'gpu')
    prompt = f"Give me an title for an Youtube shorts that is easy to narrate on. I want the topic to be interesting and attention grabbing."
    output = model.generate(prompt, max_tokens=150, temp=0.7)
    
    index_start = output.index('"')
 
    output = output[index_start:]
    
    with open("ideas.txt", "w") as idea_file:
        idea_file.write(output)
    print("Ideas File Updated")

if __name__ == "__main__":
    Ideas()