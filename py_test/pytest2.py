from pyaxidraw import axidraw   # Import the module

# Function to plot a given SVG file
def plot_svg(file_name):
    ad = axidraw.AxiDraw()          # Create class instance
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
    ad.options.reordering = 1
    ad.plot_run()

    ad.interactive()                # Enter interactive context
    if not ad.connect():            # Open serial port to AxiDraw;
        quit()                      #   Exit, if no connection.
                                    # Absolute moves follo
    ad.penup()
    ad.moveto(0, 0)                 # Pen-up move, back to origin.
    ad.penup()
    ad.delay(5000)
    ad.disconnect()                 # Close serial port to AxiDraw


# List of SVG files to plot
svg_files = ["dot_374_515.svg"]

# Plot each SVG file in sequence
for svg_file in svg_files:
    plot_svg(svg_file)
