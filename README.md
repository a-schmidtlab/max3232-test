This is a test implementation of ARCELI MAX3232 module in python.
It connects the max3232 module to a Raspberry Pi 5 (debian) and sends "Hello Reuters" via the com port.

## Hardware Requirements
- Raspberry Pi 5
- MAX3232 module
- Jumper wires
- Power supply for Raspberry Pi

## Wiring Instructions
Connect the MAX3232 module to the Raspberry Pi 5 as follows:

1. MAX3232 to Raspberry Pi 5 connections:
   - VCC → 3.3V (Pin 1)
   - GND → Ground (Pin 6)
   - T1IN → GPIO14/TXD (Pin 8)
   - R1OUT → GPIO15/RXD (Pin 10)

Note: The MAX3232 module converts the Raspberry Pi's TTL levels (3.3V) to RS232 levels (±12V).

## Software Setup

1. Enable UART on Raspberry Pi:
   ```bash
   sudo raspi-config
   # Navigate to: Interface Options → Serial Port
   # Disable serial login shell
   # Enable serial hardware
   ```

2. Install required packages:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install -r requirements.txt
   ```

3. Run the test program:
   ```bash
   python3 max3232-test.py
   ```

The program will continuously send "Hello Reuters" through the serial port. If you have connected the MAX3232 to a device or created a loopback connection, you can also see the received data.

## Troubleshooting
- Make sure the UART is enabled in raspi-config
- Verify the wiring connections
- Check if the serial port is available: `ls -l /dev/ttyAMA0`
- Ensure you have the correct permissions: `sudo usermod -a -G dialout $USER`
