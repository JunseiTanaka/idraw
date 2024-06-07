from pyaxidraw import axidraw   # Import the module
import os
import serial
import time

#TODO: serial port automatic detect
#TODO: Failed to connect to AxiDraw

# シリアルポートの設定
ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
time.sleep(2)  # シリアル接続の安定化のための待機時間


# Function to plot a given SVG file
def plot_svg(file_name, ad):
    ad.options.mode = "plot"
    ad.plot_setup(file_name)
    # Load file & configure plot context
    # Plotting options can be set, here after plot_setup().
    ad.options.pen_pos_down = 55
    ad.options.pen_pos_up = 20
    ad.options.pen_rate_lower = 50
    ad.options.pen_rate_raise = 75
    ad.options.speed_pendown = 100
    ad.options.speed_penup = 100
    ad.options.model =  5    # AxiDraw A3
    ad.options.units = 1            # set working units to cm.
    ad.options.reordering = 0
    ad.plot_run()

    ad.interactive()                # Enter interactive context
    if not ad.connect():            # Open serial port to AxiDraw;
        print("No connection, Exit prgram")
        quit()                      #   Exit, if no connection.
    ad.pendown()

    """                            # Absolute moves follo
    ad.moveto(0, 0)                 # Pen-up move, back to origin.
    ad.penup()
    ad.delay(5000)
    ad.disconnect()                 # Close serial port to AxiDraw
    """
    
def get_path_svg_files(path_svg_dir_path = "/home/jimay/Downloads/idraw/src/path_svg/"):
    # List of SVG files to plot
    path_svg_files = []
    # 指定されたディレクトリ内のファイルを取得
    for filename in os.listdir(path_svg_dir_path):
        # ファイルが.svg拡張子を持つか確認
        if filename.endswith(".svg"):
            # ファイルの絶対パスをリストに追加
            path_svg_files.append(path_svg_dir_path + str(os.path.join(filename)))

        path_svg_files.sort()
        
    return path_svg_files


path_svg_files = get_path_svg_files()
ad = axidraw.AxiDraw()          # Create class instance

try:
    # Plot each SVG file in sequence
    for path_svg_file in path_svg_files:

        ser.write(b'roll\n')
        print("Sent: roll")
        
        while True:
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                if response == "complete":
                    print("Received: complete")
                    print(f"Start axi draw of {path_svg_file}")
                    plot_svg(path_svg_file, ad)
                    break
                
except serial.SerialException as e:
    print(f"Serial exception: {e}")
    
except KeyboardInterrupt as e:
    print(f"Ctl-C")
    
finally:
    ser.close()
    ad.disconnect()
