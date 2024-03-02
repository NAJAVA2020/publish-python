import serial
import time

# Define the serial port and baud rate
serial_port = 'COM5'  # Change this to match your Arduino's serial port
baud_rate = 9600
convert_to_csv = __import__("convert_to_csv").convert_to_csv
push_to_git = __import__("push_to_git").push_to_git
# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Open a file to write the received messages
file_path = 'arduino_messages.txt'
with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        # Read message from the serial port
        print("[INFO] --- Received message from the Arduino ---")
        message = ser.readline().decode().strip()
        # Print the received message
        print(message)

        # Write the message to the file
        file.write(message + '\n')

        # Flush the file to ensure data is written immediately
        file.flush()

        # Convert the text file to CSV file
        convert_to_csv()

        # Push the changes to the git repository
        push_to_git()

# Close the serial port
ser.close()
