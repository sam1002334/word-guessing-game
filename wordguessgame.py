import random

# Library that we use in order to choose random words from a list of words
name = input("What is your name? ")

# Here the user is asked to enter their name first
print("Good Luck!", name)
choice = 'y'
while choice=='y':

    words = [
        'rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'geeks',
        'technology', 'algorithm', 'data', 'network',
        'database', 'security', 'hardware', 'software',
        'internet', 'website', 'application', 'developer',
        'engineering', 'analysis', 'design', 'system',
        'performance', 'optimization', 'debugging', 'server',
        'cloud', 'virtualization', 'architecture', 'integration',
        'automation', 'testing', 'framework', 'component',
        'protocol', 'interface', 'program', 'script',
        'language', 'compiler', 'editor', 'IDE',
        'version', 'repository', 'collaboration', 'deployment',
        'maintenance', 'upgrade', 'configuration', 'user',
        'experience', 'interface', 'usability', 'performance',
        'scalability', 'reliability', 'availability', 'data',
        'storage', 'management', 'backup', 'restore',
        'recovery', 'monitoring', 'logging', 'analytics',
        'metrics', 'reporting', 'visualization', 'dashboard',
        'api', 'endpoint', 'request', 'response',
        'authentication', 'authorization', 'session', 'token',
        'encryption', 'decryption', 'hashing', 'cipher',
        'protocol', 'communication', 'transmission', 'latency',
        'bandwidth', 'throughput', 'load',
        'scaling', 'cluster', 'container', 'orchestration',
        'microservices', 'service', 'dependency',
        'versioning', 'migration', 'refactoring', 'design',
        'pattern', 'principle', 'best practices', 'guidelines',
        'standards', 'compliance', 'regulation', 'policy',
        'privacy', 'vulnerability', 'threat'
    ]

    # Function will choose one random word from this list of words
    word = random.choice(words)

    print("Guess the characters")

    guesses = ''

    # Any number of turns can be used here
    turns = 8

    while turns > 0:
        # Counts the number of times a user fails
        failed = 0

        # All characters from the input word taking one at a time.
        for char in word:
            # Comparing that character with the character in guesses
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        print()

        if failed == 0:
            # User will win the game if failure is 0
            # and 'You Win' will be given as output
            print("You Win")
            # This prints the correct word
            print("The word is:", word)
        choice = input("Do you want to play again : y/n")


        # If user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("Guess a character: ")

        # Every input character will be stored in guesses
        guesses += guess

        # Check input with the character in word
        if guess not in word:
            turns -= 1
            # If the character doesn’t match the word
            # then “Wrong” will be given as output
            print("Wrong")
            # This will print the number of turns left for the user
            print("You have", turns, 'more guesses')

            if turns == 0:
                print("You Lose")
                print("The word was:", word)
                choice = input("Do you want to play again : y/n")
