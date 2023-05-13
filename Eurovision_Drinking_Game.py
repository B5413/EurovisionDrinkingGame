import tkinter as tk
import os

## Dynamically adjust content canvases and create rule buttons when navigation buttons are clicked
def create_content(phase):
    content_canvases = {"home":content_canvas_home, 
                        "commentary":content_canvas_commentary, 
                        "performance":content_canvas_performance, 
                        "scoring":content_canvas_scoring}
    global drinks
    drinks = 0
    drinks_label.config(text=str(drinks))
    # Loop through canvases and remove any that do not match with the phase of the navigation button clicked
    for c in ["home","commentary","performance","scoring"]:
        if c == phase:
            content_canvas = content_canvases[c]
            content_canvas.place(x=325, y=125, width=1200, height=500)
        else:
            content_canvases[c].place_forget()

    # build a contet frame to house the rule buttons
    content_frame = tk.Frame(content_canvas)
    content_frame.place(relwidth=1, relheight=1)
    tk.Label(content_frame, image=images["background"]).place(relx=0.5, rely=0.5, anchor="center")
    
    # Create rule buttons from the rules dictionary
    if phase in rules:
        rules_data = rules[phase]
        if rules_data:
            for i in range(1, len(rules_data)+1):
                rule = rules_data[i][0]
                desc = rules_data[i][1]
                increment = rules_data[i][2]
                rule_label = tk.Label(content_frame, text=rule, font=('Helvetica',16,'bold'), borderwidth=1, relief="raised", bg="#FF0188", fg="white")
                button = tk.Button(content_frame, text=desc, wraplength=275, command= lambda increment=increment: increment_score(increment), font=('Helvetica',13), width=32, height=4, borderwidth=1, bg="white")

                col = (i - 1) % 4 # Calculate the column index
                row = ((i - 1) // 4) * 2  # Calculate the starting row index

                rule_label.grid(row=row, column=col, sticky="nsew", padx=2, pady=(6,0))
                button.grid(row=row+1, column=col, sticky="nsew", padx=2)

# Update the score with appropriate number of drinks when rule buttons are clicked
def increment_score(increment):
        global drinks
        drinks += increment
        drinks_label.config(text=str(drinks))

# Set up the GUI
root = tk.Tk()
root.title("Eurovision Drinking Game")
root.geometry("1525x750")  # Set the window size to 1200x900 pixels
root.resizable(0,0)

# Store rules for each phase in a dictionary, [Title, Descripton, Drinks]
rules = {
        "commentary":{
                        1:["Bad Joke", "The presenter(s) make a joke that falls flat.", 1],
                        2:["New Outfit", "The presenter(s) change into something new.", 1],
                        3:["Rainbow Flag", "A rainbow flag appears, supporting our LGBT Eurovision family!", 1],
                        4:["Confetti", "A whole bunch of confetti turns this into a ticker-tape parade!", 2]},
        "performance":{
                        1:["Rainbow Flag", "A rainbow flag appears, supporting our LGBT Eurovision family!", 1],
                        2:["Confetti", "A whole bunch of confetti turns this into a ticker-tape parade!", 2],
                        3:["Crazy Dancing","Only one person singing? Why not add some crazy dancers to distract the audience!",1],
                        4:["Crowd Selfie","Being filmed with their back to the audience.",1],
                        5:["Innuendo","Sorry, what did they just sing? What are they doing?",1],
                        6:["Key Change","A dramatic Westlife-esque key change in the middle of the song.",1],
                        7:["Language Change","Switching from one language to another, that's just trying to curry favour with the judges.",1],
                        8:["Typography","Using words in visuals.",1],
                        9:["Pyrotechnics","Pyrotechnics fire at some point during the song.",1],
                        10:["Removing Part of Outfit",'"And try to look as if you dont care less, but if you wanna see some more..."',2],
                        11:["Singer From Another Country","You're not from around these parts are you?",2],
                        12:["Smoke Machine",'"We all came out to Montreux..." Smoke on the water, er, stage.',1],
                        13:["Strobes","Lights flashing quickly enough to erase how bad the song is from your brain.",1],
                        14:["Too Many Pyrotechnics","The pyrotechnics set fire to something. Accidentally?",5],
                        15:["Virtual Performers","Some people just lack dimension!",1],
                        16:["Wind Machine","WHOOSH!",1]},
        "scoring":{
                        1:["Bad Joke", "The presenter(s) make a joke that falls flat.", 1],
                        2:["New Outfit", "The presenter(s) change into something new.", 1],
                        3:["Rainbow Flag", "A rainbow flag appears, supporting our LGBT Eurovision family!", 1],
                        4:["Confetti", "A whole bunch of confetti turns this into a ticker-tape parade!", 2],
                        5:["Douze Points","The United Kingdom gets top marks from a country. Huh?",5],
                        6:["Milking It","The spokesperson for the country in question makes too big a meal out of their short time on screen.",1],
                        7:["Pregnant Pause","The spokesperson for the country in question doesn't realise they're live on air.",1],
                        8:["Top points to neighbours!","A country gives maximum marks to a neighbouring country.",1]}
        }

# Create a dictionary for all images to be used in the GUI
dir = os.path.dirname(os.path.abspath(__file__))

images = {"eurovision":tk.PhotoImage(file=os.path.join(dir, "images", "eurovision.png")),
          "background":tk.PhotoImage(file=os.path.join(dir, "images", "background.png")),
          "commentary":tk.PhotoImage(file=os.path.join(dir, "images", "commentary_button.png")),
          "performance":tk.PhotoImage(file=os.path.join(dir, "images", "performance_button.png")),
          "scoring":tk.PhotoImage(file=os.path.join(dir, "images", "scoring_button.png")),
          }
# Create the drink tracking variable
drinks = 0
 
# Create Header section
header_canvas = tk.Canvas(root)
header_canvas.place(x=325, y=0, width=1200, height=125)
header_frame = tk.Frame(header_canvas, bg="#0043FE")
header_frame.place(relwidth=1, relheight=1)
tk.Label(header_frame, text="EUROVISION DRINKING GAME!", anchor="center",font=('Helvetica',55,'bold'), fg="#F9FF07", bg="#0043FE").place(relx=0.5, rely=0.5, anchor="center")

# Create Navigation section
navigation_canvas = tk.Canvas(root)
navigation_canvas.place(x=0, y=0, width=325, height=750)
navigation_frame = tk.Frame(navigation_canvas, bg="#FF0188", highlightbackground = "#03025F", highlightthickness = 5)
navigation_frame.place(relwidth=1, relheight=1)

# Create Eurovision Logo to act as home button
tk.Button(navigation_frame, relief="flat", image=images["eurovision"], command=lambda phase="home": create_buttons(phase), width=280, height=100).grid(row=0, padx=10, pady=10)

# Create Navigation phase Buttons and corresponding labels
for idx, phase in [[1,"commentary"], [2,"performance"], [3,"scoring"]]:
            tk.Label(navigation_frame, text=phase.capitalize(), font=('Helvetica', 20, 'bold'), borderwidth=1, relief="raised", bg="#03025F", fg="white").grid(row=idx * 2 - 1, pady=(10,0), sticky="ew", padx=10)
            tk.Button(navigation_frame, relief="flat", image=images[phase], command=lambda phase=phase: create_content(phase), width=280, height=150).grid(row=idx * 2, )

# Create Content canvases to be formatted in the create content function on naviagtion button press 
content_canvas_home = tk.Canvas(root)
content_canvas_commentary = tk.Canvas(root)
content_canvas_performance = tk.Canvas(root)
content_canvas_scoring = tk.Canvas(root)

# create drinks section
drinks_canvas = tk.Canvas(root)
drinks_canvas.place(x=325, y=625, width=1200, height=125)
drinks_frame = tk.Frame(drinks_canvas, bg="#03025F")
drinks_frame.place(relwidth=1, relheight=1)

# Create Lables to track the drinks
tk.Label(drinks_frame, text="Drinks: ", font=('Helvetica', 70, 'bold'), bg="#03025F", fg="#FF0188").grid(row=0, column=0, sticky="nsew")
drinks_label = tk.Label(drinks_frame, text="0", font=('Helvetica', 70, 'bold'), fg="#FF0188", bg="#03025F")
drinks_label.grid(row=0, column=1, sticky="nsew")

# Default to home content
create_content("home")

# Run the app
root.mainloop()

