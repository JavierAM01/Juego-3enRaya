from play import main as play
from train import main as train
from stats import main  as stats


def main():
    print("Chose one option:")
    print(" 1) Play")
    print(" 2) Train")
    print(" 3) Stats")
    x = input(" > ")

    if x == "1":
        play.main()
    elif x == "2":
        train.main()
    else:
        stats.main()


if __name__ == '__main__':
    main()