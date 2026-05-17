import agent
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    if len(sys.argv) < 3:
        print("Too few arguments, please try again")
        return
    query = sys.argv[1]
    reading_level = sys.argv[2]
    result = agent.run(query, reading_level)
    print(f"{result}")

if __name__ == "__main__":
    main()
