"""Generate original monochrome profile illustrations without network access."""
from pathlib import Path
import math
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
STILLS = ASSETS / 'stills'
FRAMES, DURATION, SCALE = 48, 100, 2
TAU = math.tau
FONT_DIRS = [Path(os.environ.get('PROFILE_FONT_DIR', '.')), Path('C:/Windows/Fonts'),
             Path('/usr/share/fonts/truetype/liberation2'), Path('/usr/share/fonts/truetype/dejavu')]


def font(size, bold=False, mono=False):
    names = (['consola.ttf', 'DejaVuSansMono.ttf'] if mono else
             ['arialbd.ttf', 'LiberationSans-Bold.ttf', 'DejaVuSans-Bold.ttf'] if bold else
             ['arial.ttf', 'LiberationSans-Regular.ttf', 'DejaVuSans.ttf'])
    for directory in FONT_DIRS:
        for name in names:
            path = directory / name
            if path.exists():
                return ImageFont.truetype(str(path), size * SCALE)
    return ImageFont.load_default(size=size * SCALE)


class Canvas:
    def __init__(self, width, height):
        self.image = Image.new('RGB', (width * SCALE, height * SCALE), '#0d0d0d')
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = width, height

    def coords(self, values):
        return tuple(round(v * SCALE) for v in values)

    def line(self, points, fill='#444444', width=1):
        self.draw.line(self.coords(points), fill=fill, width=width * SCALE)

    def rect(self, box, fill='#181818', outline='#444444', radius=8, width=1):
        self.draw.rounded_rectangle(self.coords(box), radius=radius * SCALE,
                                   fill=fill, outline=outline, width=width * SCALE)

    def circle(self, x, y, r, fill=None, outline='#666666', width=1):
        self.draw.ellipse(self.coords((x-r, y-r, x+r, y+r)), fill=fill,
                          outline=outline, width=width * SCALE)

    def text(self, xy, text, size=16, fill='#eeeeee', bold=False, mono=False, anchor=None):
        self.draw.text(self.coords(xy), text, font=font(size, bold, mono), fill=fill, anchor=anchor)

    def polygon(self, points, fill='#171717', outline='#777777', width=1):
        scaled = [(round(x*SCALE), round(y*SCALE)) for x, y in points]
        self.draw.polygon(scaled, fill=fill)
        self.draw.line(scaled + [scaled[0]], fill=outline, width=width*SCALE, joint='curve')

    def finish(self):
        return self.image.resize((self.width, self.height), Image.Resampling.LANCZOS)


def card(number, category, title, subtitle):
    c = Canvas(600, 300)
    c.rect((0.5, 0.5, 599, 299), fill='#111111', outline='#363636', radius=14)
    c.text((28, 25), f'{number:02} / {category}', 13, '#aaaaaa', mono=True)
    c.text((26, 57), title, 39, bold=True)
    c.text((28, 106), subtitle, 16, '#b3b3b3')
    c.line((28, 144, 572, 144), '#303030')
    for x in range(300, 580, 28):
        c.line((x, 164, x, 278), '#1c1c1c')
    for y in range(164, 280, 28):
        c.line((300, y, 576, y), '#1c1c1c')
    return c


def anamboatra(t):
    c = card(1, 'CIVIC PLATFORM', 'Anamboatra', 'From citizen reports to field interventions.')
    c.text((28, 177), 'REPORT', 12, '#cccccc', mono=True)
    c.text((28, 199), 'CONNECT', 12, '#cccccc', mono=True)
    c.text((28, 221), 'REPAIR', 12, '#cccccc', mono=True)
    nodes = [(338, 242), (420, 182), (514, 211), (458, 266)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)]
    for i, (a, b) in enumerate(edges):
        x1, y1 = nodes[a]; x2, y2 = nodes[b]
        c.line((x1, y1, x2, y2), '#555555')
        phase = (t + i/len(edges)) % 1
        x, y = x1+(x2-x1)*phase, y1+(y2-y1)*phase
        c.circle(x, y, 5, '#dedede', '#dedede')
    for i, (x, y) in enumerate(nodes):
        r = 10 if i != 1 else 14
        pulse = 4 + 3 * math.sin(TAU*t + i)
        c.circle(x, y, r+pulse, outline='#333333')
        c.circle(x, y, r, '#191919', '#aaaaaa')
        c.circle(x, y, 3, '#ededed', '#ededed')
    return c.finish()


def stick(t):
    c = card(2, 'CONTROL LABORATORY', 'Stick Balancing', 'Physics. Experiments. Reinforcement learning.')
    c.text((28, 178), 'CART / POLE', 12, '#cccccc', mono=True)
    c.text((28, 202), 'LOCAL EXPERIMENTS', 12, '#888888', mono=True)
    c.line((286, 268, 568, 268), '#777777')
    for x in range(300, 570, 20):
        c.line((x, 273, x, 277), '#555555')
    cx = 422 + 47 * math.sin(TAU*t)
    theta = 0.28 * math.sin(TAU*t + 0.55)
    c.line((cx, 248, cx + 78*math.sin(theta), 248-78*math.cos(theta)), '#eeeeee', 4)
    c.circle(cx + 78*math.sin(theta), 248-78*math.cos(theta), 6, '#dddddd', '#dddddd')
    c.rect((cx-28, 247, cx+28, 260), '#333333', '#cccccc', 3)
    c.circle(cx-18, 263, 5, '#111111', '#aaaaaa')
    c.circle(cx+18, 263, 5, '#111111', '#aaaaaa')
    c.circle(cx, 248, 4, '#111111', '#eeeeee')
    c.text((28, 260), 'UNITY + PYTHON', 12, '#888888', mono=True)
    return c.finish()


def ticket(t):
    c = card(3, 'EVENT EXPERIENCES', 'Ticket', 'Discover. Reserve. Keep your ticket.')
    c.text((28, 177), 'GOOD MOMENTS,', 12, '#cccccc', mono=True)
    c.text((28, 199), 'TOGETHER.', 12, '#cccccc', mono=True)
    y = 182 + 5*math.sin(TAU*t)
    c.rect((324, y+10, 548, y+87), '#151515', '#555555', 8)
    c.rect((306, y, 530, y+77), '#202020', '#aaaaaa', 8)
    c.circle(306, y+38, 8, '#111111', '#111111')
    c.circle(530, y+38, 8, '#111111', '#111111')
    c.text((326, y+13), 'ADMIT ONE', 13, '#eeeeee', mono=True)
    c.line((326, y+39, 420, y+39), '#666666')
    c.line((326, y+49, 400, y+49), '#555555')
    for yy in range(8, 73, 7):
        c.line((442, y+yy, 442, y+yy+3), '#777777')
    for i in range(14):
        x = 457+i*4
        c.line((x, y+15, x, y+60), '#cccccc' if i % 3 else '#888888', 1 if i%2 else 2)
    scan = y+16+43*(0.5-0.5*math.cos(TAU*t))
    c.line((452, scan, 514, scan), '#ffffff', 2)
    c.text((28, 260), 'WEB + MOBILE', 12, '#888888', mono=True)
    return c.finish()


def before(t):
    c = card(4, 'ANDROID RITUAL', 'Before You Go', 'A little ritual before heading out.')
    c.text((28, 177), 'YOUR THINGS.', 12, '#cccccc', mono=True)
    c.text((28, 199), 'YOUR PACE.', 12, '#cccccc', mono=True)
    c.text((28, 260), 'OFFLINE / ON DEVICE', 12, '#888888', mono=True)
    c.draw.arc(c.coords((414, 190, 458, 230)), 180, 360, fill='#bbbbbb', width=3*SCALE)
    for i in range(3):
        phase = (t + i/3) % 1
        ease = 0.5-0.5*math.cos(math.pi*phase)
        x = 328 + (436-328)*ease
        y = 179 + 74*ease - 40*math.sin(math.pi*phase)
        shade = round(205*(1-max(0, (phase-0.75)/0.25)))
        color = f'#{shade:02x}{shade:02x}{shade:02x}'
        if i == 0:
            c.circle(x, y, 6, outline=color, width=2)
            c.line((x+6, y, x+22, y), color, 2)
            c.line((x+16, y, x+16, y+5), color, 2)
            c.line((x+21, y, x+21, y+5), color, 2)
        elif i == 1:
            c.rect((x-8, y-11, x+9, y+11), '#1d1d1d', color, 2)
            c.line((x-3, y-8, x-3, y+8), color)
        else:
            c.circle(x-8, y, 6, outline=color, width=2)
            c.circle(x+8, y, 6, outline=color, width=2)
            c.line((x-2, y, x+2, y), color, 2)
    c.polygon([(400, 215), (472, 215), (480, 273), (392, 273)], '#222222', '#cccccc', 2)
    c.line((406, 224, 466, 224), '#555555')
    c.circle(436, 245, 6, outline='#777777')
    return c.finish()


def header(t):
    c = Canvas(1200, 420)
    c.rect((0.5, 0.5, 1199, 419), '#101010', '#363636', 20)
    for x in range(720, 1200, 40): c.line((x, 1, x, 418), '#1b1b1b')
    for y in range(20, 420, 40): c.line((701, y, 1198, y), '#1b1b1b')
    c.line((700, 1, 700, 419), '#292929')
    c.rect((64, 54, 338, 86), '#191919', '#444444', 16)
    c.circle(82, 70, 3, '#dddddd', '#dddddd')
    c.text((96, 61), 'SOFTWARE & WEB DEVELOPER', 12, '#cccccc', mono=True)
    c.text((59, 117), 'TOAANDRI', 88, bold=True)
    c.text((64, 226), 'Thoughtful interfaces.', 25, '#e0e0e0')
    c.text((64, 261), 'Useful software.', 25, '#aaaaaa')
    c.line((64, 323, 636, 323), '#383838')
    c.text((64, 347), 'REACT / NODE.JS / TYPESCRIPT', 13, '#aaaaaa', mono=True)
    c.circle(949, 204, 158, outline='#303030')
    for i, base in enumerate([255, 210, 165]):
        y = base + 5*math.sin(TAU*t+i*0.65)
        corners = [(776,y), (949,y-100), (1122,y), (949,y+100)]
        c.polygon(corners, ['#111111','#191919','#222222'][i], ['#444444','#666666','#999999'][i])
        if i == 2:
            c.polygon([(816,y),(949,y-77),(1082,y),(949,y+77)], '#222222', '#444444')
            c.line((921,y-16,892,y+1,921,y+18), '#eeeeee', 3)
            c.line((977,y-16,1006,y+1,977,y+18), '#eeeeee', 3)
            c.line((960,y-22,940,y+24), '#eeeeee', 3)
    angle = TAU*t-0.8
    c.circle(949+158*math.cos(angle),204+158*math.sin(angle),4,'#eeeeee','#eeeeee')
    c.text((949, 380), 'INTERFACE / LOGIC / DATA', 11, '#aaaaaa', mono=True, anchor='mm')
    return c.finish()


def footer(t):
    c = Canvas(1200,124)
    c.rect((0.5,0.5,1199,123),'#111111','#363636',14)
    c.line((40,38,40,86),'#dddddd',2)
    c.text((62,36),'Misaotra anao nitsidika eto!',23,bold=True)
    c.text((62,68),'Thanks for stopping by.',15,'#aaaaaa')
    c.text((1158,40),'TOAANDRI',16,'#dddddd',mono=True,anchor='ra')
    c.text((1158,73),'ANTANANARIVO / MADAGASCAR',11,'#999999',mono=True,anchor='ra')
    c.line((62,107,1158,107),'#292929')
    x=62+1096*(0.5-0.5*math.cos(TAU*t))
    c.line((max(62,x-30),107,min(1158,x+30),107),'#999999',2)
    c.circle(x,107,2,'#dddddd','#dddddd')
    return c.finish()


def generate():
    STILLS.mkdir(parents=True,exist_ok=True)
    for name, renderer in [('header',header),('project-anamboatra',anamboatra),
                            ('project-stick-balancing',stick),('project-ticket',ticket),
                            ('project-beforeyougo',before),('footer',footer)]:
        frames = [renderer(i/FRAMES) for i in range(FRAMES)]
        frames[0].save(STILLS/f'{name}.png',optimize=True)
        # Shared grayscale palette avoids color shimmer between GIF frames.
        palette = Image.new('P',(1,1))
        palette.putpalette([value for i in range(256) for value in (i,i,i)])
        indexed = [f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
        target=ASSETS/f'{name}.gif'
        indexed[0].save(target,save_all=True,append_images=indexed[1:],duration=DURATION,
                        loop=0,optimize=True,disposal=1)
        print(f'{name}: {target.stat().st_size:,} bytes')


if __name__ == '__main__':
    generate()
