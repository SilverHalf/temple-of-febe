import drawsvg as draw
import json
import os

FONT_SIZE = 12
FONT='Segoe UI'
SECOND_WIDTH = 10
ROW_HEIGHT = 25
VERTICAL_TEXT_AJUST = 4
LABEL_COLOR = 'white'

def timeline_from_file(
        file: str,
        mechanicsFile: str,
        start_time: int = 0,
        end_time: int= 600,
        output_file: str = "output.svg"):

    # Parsing and organizing data
    mechanics = load_json(mechanicsFile)
    data = load_json(file)
    duration = data["duration"]
    rows = data["rows"]
    label_width = data["label_width"]

    # Setting image dimensions and creating canvas
    totalrows = len(rows) + 1
    total_x = min(duration, end_time - start_time) * SECOND_WIDTH + label_width
    total_y = totalrows * ROW_HEIGHT
    d = draw.Drawing(total_x, total_y)

    # start from second row because first one is the time scale
    row_num = 1
    for row in rows:
        # Creating label for row
        d.append(draw_text(row, 0, ROW_HEIGHT*row_num, label_width, font_size=16, vertical_adjust=6, **data["label-args"]))
        # Iterating over mechanics in the row
        for mechanic in rows[row]["mechanics"]:
            # Creating mechanic elements (shapes and text) and adding to the drawing
            result = draw_mechanic(mechanics[mechanic["name"]], mechanic["start"], row_num, label_width, start_time, end_time)
            for element in result:
                d.append(element)
        row_num += 1

    # Drawing time scale and adding it to the figure
    timelineItems = draw_timeline(duration, total_x, total_y, label_width, start_time, end_time, **data["timeline-args"])
    for item in timelineItems:
        d.append(item)

    d.save_svg(output_file)

def draw_mechanic(mechanic: dict, startSeconds: int, row: int, label_width: int, start: int, end: int):
    '''Creates the graphical elements for a mechanic.'''

    x = (startSeconds-start)* SECOND_WIDTH + label_width
    # Skipping mechanics that begin before the start time
    if x < label_width:
        return []

    y = row * ROW_HEIGHT
    if "duration" in mechanic.keys():
        duration = mechanic["duration"]

        # Skipping mechanics that end after the end time
        if startSeconds + duration > end:
            return []

        # drawing mechanic and text
        width = duration * SECOND_WIDTH
        text = mechanic["text"]
        r = draw.Rectangle(x, y, width, ROW_HEIGHT, **mechanic["rect-args"])
        text = draw_text(text, x, y, width, **mechanic["text-args"])
        return r, text
    else:
        # drawing mechanic
        c = draw.Circle(x, y +ROW_HEIGHT/2, ROW_HEIGHT/4, **mechanic["circle-args"])
        line = draw.Line(x, y, x, y+ROW_HEIGHT, **mechanic["line-args"])
        return c, line

def draw_text(
        text: str, 
        x: int, 
        y: int, 
        width: int,
        font_size = FONT_SIZE,
        vertical_adjust: int = VERTICAL_TEXT_AJUST, **kwargs):
    '''Creates a text element'''
    
    text = draw.Text(text,
        font_size,
        x + width/2,
        y + ROW_HEIGHT/2 + vertical_adjust, **kwargs)
    return text

def load_json(jsonfile: str) -> dict:
    with open(jsonfile, 'r') as jsonfile:
        return json.load(jsonfile)

def draw_timeline(
        durationSeconds : int,
        total_x: int,
        total_y: int,
        label_width: int,
        start: int, end: int, **kwargs):
    
    length = min(total_x,  (end - start)*SECOND_WIDTH + label_width)

    items = []
    items.append(draw.Line(0, ROW_HEIGHT, length, ROW_HEIGHT, **kwargs))
    items.append(draw.Line(label_width, 0, label_width, total_y, **kwargs))
    color = kwargs["stroke"]

    for time in range(start + 1, min(end, durationSeconds)):
        x = label_width + (time-start)*SECOND_WIDTH
        if time % 10 == 0:
            items += large_time_marker(x, time,color)
        elif time % 5 == 0:
            items.append(medium_time_marker(x,color))
        else:
            items.append(small_time_marker(x,color))

    return items

def large_time_marker(x: float, time: float, color: str):

    line = draw.Line(x, ROW_HEIGHT*0.6, x, ROW_HEIGHT, stroke=color, stroke_width=1.5)
    text = draw_text(str(time), x, 0, 0, font_size = 10, vertical_adjust= 0, fill=color, style="font-family:Segoe UI;text-anchor:middle")
    
    return line, text

def medium_time_marker(x: float, color: str):
    line = draw.Line(x, ROW_HEIGHT*0.8, x, ROW_HEIGHT, stroke=color, stroke_width=0.5)
    
    return line

def small_time_marker(x: float, color: str):
    line = draw.Line(x, ROW_HEIGHT*0.9, x, color, stroke=LABEL_COLOR, stroke_width=0.3)
    
    return line

if __name__ == "__main__":
    dir_path = os.path.join(os.path.dirname(__file__), "data", "phases")
    for file in os.listdir(dir_path):
        if file.endswith(".json"):
            timeline_from_file(os.path.join(dir_path, file))
