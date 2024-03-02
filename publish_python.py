import serial
import time

# Define the serial port and baud rate
serial_port = 'COM5'  # Change this to match your Arduino's serial port
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Open a file to write the received messages
file_path = 'arduino_messages.txt'
with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        # Read message from the serial port
        message = ser.readline().decode().strip()
        print("[INFO] --- time: ", time.ctime())
        # Print the received message
        print(message)

        # Write the message to the file
        file.write(message + '\n')

        # Flush the file to ensure data is written immediately
        file.flush()

# Close the serial port
ser.close()
