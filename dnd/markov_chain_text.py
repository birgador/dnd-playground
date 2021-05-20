import random
#import time

with open('files/fr.txt','r') as f:

    read_data = f.readlines()[0]

data = set(read_data.split(','))

# states = {}
# for word in data:
#     for char in word:
#         state

def newWord(words):
    states = {}
    initial_states = {}
    for word in words:
        chunks, chunk_size = len(word),3
        prev_state = ''
        for i in range(chunks-chunk_size+1):
            state = word[i:i+chunk_size].lower()
            if i == 0:
                if state in initial_states:
                    initial_states[state] += 1
                else:
                    initial_states[state] = 1
            else:
                if prev_state not in states:
                    states[prev_state] = {state:1}
                else:
                    if state in states[prev_state]:
                        states[prev_state][state] += 1
                    else:
                        states[prev_state][state] = 1
            prev_state = state

    # Step 1: Start with some initial random state
    
    new_word =''
    while '.' not in new_word and len(new_word)<7+random.randint(-3,5):
        initial_state = random.choices(list(initial_states.keys()),list(initial_states.values()))[0]
        new_word += initial_state
    # # Step 2: Select randomly one of its transition states, considering its weights
        next_state = random.choices(list(states[initial_state].keys()),list(states[initial_state].values()))[0]
        new_word += next_state[-1]
    # # Step 3: Append the new state to your generated text

    # # Step 4: Repeat step one using the new state, until a stop character is found, or until you are happy with your result
        # time.sleep(2.0)
    return new_word


word = newWord(data)

print(word)

