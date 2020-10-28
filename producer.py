import random
import string

instantMessage = []
charactercount = []
# you will be updating the number down below to get desire messages.
generate_message = 10

def randStr(chars = string.ascii_uppercase + string.digits):
    # 3 is a minimum length and 25 is the max length of random messages. You can update this to get the desire length
    N = random.randint(3,25)
    msg = ''.join(random.choice(chars) for _ in range(N))
    charactercount.append(sum(len(i) for i in msg))
    instantMessage.append(msg)





for i in range(generate_message):
    randStr()


