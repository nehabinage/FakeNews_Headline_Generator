# FakeNews_Headline_Generator
This program generates the sentence using random words listed for entertainment purpose.

# Pseudocode
1. START the program
2. IMPORT the 'random' module
3. CREATE a list of Indian subjects
Example: ["Shahrukh Khan", "Virat Kohli", "Nirmala Sitharaman", "A Mumbai Ca t", "A Group of Monkeys"]
4. CREATE a list of Indian actions
Example: ["launches", "cancels", "dances with", "eats", "declares war on"]
5. CREATE a list of Indian places or things
Example: ["at Red Fort", "in Mumbai local train", "a plate of samosas", "ins ide Parliament", "at Ganga ghat"]
6. START a loop (use while loop) that keeps running until the user says "no"
    a. RANDOMLY choose one item from each list (subject, action, place)
    b. COMBINE the three chosen words into one sentence using string formatting Example format: "BREAKING: (subject) (action) (place)!"
    c. PRINT the final fake news headline
    d. ASK the user if they want to generate another headline (yes/no)
    e. IF user says "no", END the loop
7. PRINT a goodbye message
8. END the program


# Concepts that used in this project	
1. lists	--->     To store groups of words like names, actions, and places
2. random.choice()	---> To pick one item randomly from a list
3. print () --->	To show the fake headline on screen
4. input () --->	To ask the user if they want another headline
5. while loop --->	To repeat the process until the user says "no"
6. string concatenation or f-strings --->	To form a sentence using selected words

