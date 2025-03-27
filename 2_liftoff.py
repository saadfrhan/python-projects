import time

def launch_countdown(max = 10):
    for number in range(max, 0, -1):
        print(number, end=' ')

        print(flush=True)

        time.sleep(1)

    print('Liftoff!')

def main():
    launch_countdown()

if __name__ == "__main__":
    main()