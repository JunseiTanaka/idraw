from pyaxidraw import axidraw   # Import the module


ad = axidraw.AxiDraw()          # Create class instance
ad.options.mode = "plot"
ad.plot_setup("dot_3.svg")
# Load file & configure plot context
# Plotting options can be set, here after plot_setup().
ad.options.pen_pos_down = 45
ad.options.pen_pos_up = 20
ad.options.pen_pos_down = 45
ad.options.pen_pos_up = 20
ad.options.pen_rate_lower = 50
ad.options.pen_rate_raise = 75
ad.options.speed_pendown= 100
ad.options.speed_penup = 100
ad.options.model = 5     #arrow A3
ad.options.units = 1            # set working units to cm.
ad.plot_run()

ad.interactive()                # Enter interactive context
if not ad.connect():            # Open serial port to AxiDraw;
    quit()                      #   Exit, if no connection.
                                # Absolute moves follow:

ad.moveto(1,1)                  # Pen-up move, back to origin.
ad.delay(5000)

ad.plot_setup("dot_3.svg")
ad.options.pen_pos_down = 45
ad.options.pen_pos_up = 20
ad.plot_run()
ad.moveto(0,0)                  # Pen-up move, back to origin.
ad.disconnect()                 # Close serial port to AxiDraw
