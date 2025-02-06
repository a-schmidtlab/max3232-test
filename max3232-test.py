#!/usr/bin/env python3

import serial
import time
import sys

def main():
    try:
        # Configure the serial port
        print("Opening serial port...")
        ser = serial.Serial(
            port='/dev/ttyAMA0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        print(f"Serial port opened successfully: {ser.name}")
        print(f"Current settings: {ser}")

        counter = 0
        while True:
            # Send "Hello Reuters" message
            message = f"Hello Reuters {counter}\r\n"
            print(f"Attempting to send: {message.strip()}")
            bytes_written = ser.write(message.encode())
            print(f"Bytes written: {bytes_written}")
            ser.flush()  # Ensure all data is sent
            
            # Wait briefly for any response
            time.sleep(0.1)
            
            # Check for any response
            if ser.in_waiting:
                try:
                    received = ser.readline().decode().strip()
                    print(f"Received: {received}")
                except UnicodeDecodeError:
                    raw_data = ser.readline()
                    print(f"Received raw data (hex): {raw_data.hex()}")
            else:
                print("No data received")
            
            counter += 1
            time.sleep(1)

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'ser' in locals():
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    main()
