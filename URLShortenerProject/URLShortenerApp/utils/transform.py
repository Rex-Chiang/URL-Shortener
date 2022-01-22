from random import choice
from string import ascii_letters, digits

base_chars = ascii_letters + digits

def create_random_code(chars = base_chars):
    return "".join([choice(chars) for _ in range(6)])

def create_short_url(model):
    random_code = create_random_code()
    model_instance = model.__class__

    while model_instance.objects.filter(short_url = random_code).exists():
        random_code = create_random_code()

    return random_code