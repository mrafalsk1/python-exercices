import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("physics")
    parser.add_argument("chemistry")
    parser.add_argument("maths")

    args = parser.parse_args()

    print(args.physics)
    print(args.maths)
    print(args.chemistry)

    
    print("Result:", (
        int(args.physics) + int(args.chemistry) + int(args.maths)
    ) / 3)

    # python3 cmd.py --physics 60 --chemistry 70 --maths 90