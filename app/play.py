from engine import run

if __name__ == "__main__":
    for i in range(300):
        temp = run()
        print(temp['champion'].personality())
        if temp == 1000:
            print(temp)
            break
