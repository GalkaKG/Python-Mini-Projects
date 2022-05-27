from nltk.chat.util import Chat, reflections
from termcolor import colored

pairs = [
    [
        r'(.*)(room|suit|apartment|studio)',
        [colored("Okay %2, for how many people ?", "magenta")]
    ],
    [
        r"(.*)(2|3|4|5|6)",
        [colored("Perfect! Which month?", "yellow")]
    ],
    [
        r"(.*)(May|June|July|August|September)",
        [colored("How long you will stay?Type days or weeks with letters:", "red")]
    ],
    [
        r"(.*)(January|February|March|April|October|November|December)(.*)",
        [colored("Sorry, we are closed at that month.", "red")]
    ],
    [
        r"(.*)(one|two|three|four|five|six|seven|eight|ten|days|day|week|weeks)(.*)",
        [colored("Lovely! We have a last one left, exactly for you!", "blue")]
    ],
    [
        r"(.*)(close|open|work|working)(.*)",
        [colored("Our hotel works only for the summer season. It opens in May and closing in September.", "red")]
    ],
    [
        r"(.*)(price|much|cost)",
        [colored('One room is 200€ per night.\nThe suit is 300€ per night.\nThe apartment is 300€ per night.\n'
                 'The studio is 100€ per night.', "yellow")]
    ],
    [
        r"(.*)(location|find|place|where|hotel)",
        [colored('Black sea, Bulgaria', "yellow")]
    ],
    [
        r"quit",
        [colored("Thank you for booking with me. I wish you the best holiday ever!!!", "cyan")]
    ],
    [
        r"(.*)",
        [colored('You are welcome to "Sunrise" hotel!', "magenta")]
    ],
]

# default message at the start of chat
print(colored("Please type in English language to start a conversation. "
      "Type quit and leave.\n\nHi, I'm hotel 'Sunrise' reception BOT\nHow can I help you?", "cyan"))
# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()
