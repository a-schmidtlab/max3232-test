This is a test implementation of ARCELI MAX3232 module in python.
It connects the max3232 module to a Raspberry Pi 5 (debian) and sends "Hello Reuters" via the com port.

## Hardware Requirements
- Raspberry Pi 5
- MAX3232 module
- Jumper wires
- Power supply for Raspberry Pi
- USB to Serial adapter (for Windows monitoring)

## Wiring Instructions
Connect the MAX3232 module to the Raspberry Pi 5 as follows:

1. MAX3232 to Raspberry Pi 5 connections:
   - VCC → 3.3V (Pin 1)
   - GND → Ground (Pin 6)
   - T1IN → GPIO14/TXD (Pin 8)
   - R1OUT → GPIO15/RXD (Pin 10)

2. MAX3232 to USB Serial adapter connections:
   - GND (MAX3232) → GND (USB adapter)
   - R2OUT (MAX3232) → RX (USB adapter)
   - T2IN (MAX3232) → TX (USB adapter)

Note: The MAX3232 module converts the Raspberry Pi's TTL levels (3.3V) to RS232 levels (±12V).

## Software Setup

1. Enable UART on Raspberry Pi:
   ```bash
   sudo raspi-config
   # Navigate to: Interface Options → Serial Port
   # Disable serial login shell
   # Enable serial hardware
   ```

2. Install required system packages:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv python3-full
   ```

3. Create and activate a virtual environment:
   ```bash
   # Create a virtual environment in the project directory
   python3 -m venv venv
   
   # Activate the virtual environment
   source venv/bin/activate
   ```

4. Install Python requirements (with virtual environment activated):
   ```bash
   pip install -r requirements.txt
   ```

5. Run the test program (with virtual environment activated):
   ```bash
   python max3232-test.py
   ```

## Windows Setup for Signal Monitoring

1. Connect the USB to Serial adapter to your Windows PC

2. Install drivers (if not automatically installed):
   - For most USB-Serial adapters, Windows will automatically install drivers
   - If not, check the manufacturer's website for drivers

3. Find the COM port number:
   - Open Device Manager (right-click Start → Device Manager)
   - Look under "Ports (COM & LPT)"
   - Note the COM port number (e.g., COM3, COM4)

4. Monitor the serial connection (choose one method):

   Option 1 - Using PuTTY:
   - Download and install PuTTY from https://www.putty.org/
   - Open PuTTY
   - Select "Serial" as connection type
   - Enter your COM port (e.g., COM3)
   - Set Speed to 9600
   - Click "Open"

   Option 2 - Using Arduino IDE:
   - Download and install Arduino IDE
   - Open Tools → Serial Monitor
   - Select your COM port
   - Set baud rate to 9600
   - You should see the "Hello Reuters" messages

   Option 3 - Using RealTerm:
   - Download RealTerm from https://sourceforge.net/projects/realterm/
   - Set Port to your COM port
   - Set Baud to 9600
   - Click "Open"

Note: Remember to always activate the virtual environment with `source venv/bin/activate` before running the program.
To deactivate the virtual environment when you're done, simply type `deactivate`.

## Troubleshooting
- Make sure the UART is enabled in raspi-config
- Verify the wiring connections
- Check if the serial port is available: `ls -l /dev/ttyAMA0`
- Ensure you have the correct permissions: `sudo usermod -a -G dialout $USER`
- If you get permission errors accessing the serial port, you may need to log out and log back in for the group changes to take effect
- On Windows, if you can't see the COM port, try:
  - Unplugging and replugging the USB adapter
  - Installing/reinstalling the drivers
  - Checking Device Manager for error symbols
- If you see garbled text in the terminal:
  - Double-check the baud rate is set to 9600
  - Verify the wiring connections are secure
  - Make sure GND is properly connected between devices
