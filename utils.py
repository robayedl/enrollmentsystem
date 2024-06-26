import random

class Utils:
    @staticmethod
    def generate_random_student_id():
        new_id = (random.randint(1, 999999))
        new_id = f"{new_id:06}"
        return new_id
    
    def print_red(text):
        print("\033[91m" + text + "\033[0m")

    def print_green(text):
        print("\033[92m" + text + "\033[0m")

    def print_yellow(text):
        print("\033[93m" + text + "\033[0m")

    def print_blue(text):
        print("\033[94m" + text + "\033[0m")

    # def print_magenta(text):
    #     print("\033[95m" + text + "\033[0m")

    # def print_cyan(text):
    #     print("\033[96m" + text + "\033[0m")

    # def print_white(text):
    #     print("\033[97m" + text + "\033[0m")
