import serial
import time
 
# シリアルポートの設定
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)  # シリアル接続の安定化のための待機時間
 
def send_and_receive():
    try:
        # データを送信
        ser.write(b'roll\n')
        
        print("Sent: roll")
        # 返信を待機
        while True:
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                if response == "complete":
                    print("Received: complete")
                    break
    except serial.SerialException as e:
        print(f"Serial exception: {e}")
    finally:
        ser.close()
 
if __name__ == "__main__":
    send_and_receive()
