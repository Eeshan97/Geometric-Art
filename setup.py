import sys
import cx_Freeze
base = None
if sys.platform == "win32":
    base = "Win32GUI"
executables = [
        #                   name of your game script
        cx_Freeze.Executable(script = "main.py", base = base)
]



    
cx_Freeze.setup(
        name = "L-Systems",
        version = '0.1',
        options = {"build_exe": {"packages":["Tkinter","ttk","random","turtle","tkcolorpicker","tkMessageBox","re","time","L_system","FractalsArt","CalligraphyArt", "letters_dictionary","letters_draw","Segmentation","customFractals","PIL","math"],"include_files":["user_guide.txt","resources"]}},
        description = "Fractal Art",
        executables = executables)
