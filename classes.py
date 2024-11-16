import datetime

class Victim:
    """
    This class represents the victim
    """

    def __init__(self):
        self.now = datetime.datetime.now()
        self.formated_time = self.now.strftime("%H:%M:%S")
        self.colour = ""


def main():
    ...


if __name__ == "__main__":
    main()
