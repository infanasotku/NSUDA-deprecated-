def disable_fullscreen(): 
    import win32con
    import win32gui
    import win32api
    hwnd = win32gui.GetForegroundWindow() 
    win32api.SetWindowLong(hwnd, 
                           win32con.GWL_STYLE, 
                           win32api.GetWindowLong(hwnd, 
                                                  win32con.GWL_STYLE) & ~win32con.WS_MAXIMIZEBOX)

width_shift = -15
height_shift = -30