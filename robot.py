import time

def robot_loop():
    while True:
        print("Amber light ON (5s)")
        time.sleep(5)
        print("Amber light OFF\n")

        print("Green light ON (10s)")
        time.sleep(10)
        print("Green light OFF\n")

        print("Red light ON (20s)")
        time.sleep(20)
        print("Red light OFF\n")

        print("=== End of 35-second cycle ===\n")

# Start the loop
robot_loop()