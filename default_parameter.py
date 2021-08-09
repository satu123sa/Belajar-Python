# Belajar default parameter

def say_hello(first_name="budi",last_name=""):
    print(f"hello{first_name}-{last_name}")
    
say_hello("Eko")
say_hello(last_name="kurniawan", first_name="Eko")