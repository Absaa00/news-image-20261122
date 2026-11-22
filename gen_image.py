#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news front page (1024x1024 PNG).

Fresh code written in this session. Offline, deterministic: same input
produces byte-identical output. Run: python3 gen_image.py
Writes entry.png next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 234)
INK = (20, 20, 20)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
TEAL = (14, 92, 92)
GOLD = (176, 132, 30)
RULE = (120, 110, 95)
LIGHT = (238, 232, 218)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, fill=INK, leading=6):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def headline(draw, x, y, text, fnt, max_w, fill=INK, leading=2):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def kicker(draw, x, y, text, fill):
    f = font(SANS_B, 17)
    draw.text((x, y), text.upper(), font=f, fill=fill)
    return y + 24


def panel(draw, box, edge):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=WHITE, outline=edge, width=2)
    draw.line([(x0, y0), (x1, y0)], fill=edge, width=5)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 28  # margin

    # ---- Masthead ----
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.text((m, 14), "THE WORLD TODAY", font=font(SERIF_B, 62),
           fill=(244, 238, 222))
    d.text((m, 88), "SUNDAY  22  NOVEMBER  2026  —  THE WORLD'S NEWS IN ONE PAGE",
           font=font(SANS_B, 19), fill=(212, 175, 90))
    _rt = "No. 326"
    d.text((W - m - d.textlength(_rt, font=font(SANS, 18)), 92), _rt,
           font=font(SANS, 18), fill=(200, 205, 215))
    d.rectangle([0, 128, W, 134], fill=RED)

    # ---- Lead: Gulf on edge (full width) ----
    y = 146
    panel(d, (m, y, W - m, y + 268), RED)
    px, py = m + 20, y + 12
    py = kicker(d, px, py, "Lead — Middle East", RED)
    py = headline(d, px, py, "GULF ON EDGE AS IRAN HITS US BASE",
                  font(SERIF_B, 40), W - 2 * m - 40)
    py = headline(d, px, py, "AND TARGETS BAHRAIN",
                  font(SERIF_B, 40), W - 2 * m - 40)
    py = para(d, px, py + 6,
              "Iran struck a US air base in Kuwait and targeted Bahrain as the "
              "Gulf confrontation widened. Two tankers were reported hit near "
              "Oman, and an ADNOC vessel was attacked in the Strait of Hormuz "
              "with one crew member missing. Oil fell more than 3% as traders "
              "weighed a wider war.", font(SANS, 21), W - 2 * m - 40)
    # alert strip inside lead
    d.rectangle([px, y + 268 - 34, W - m - 20, y + 268 - 12], fill=(253, 230, 225))
    d.text((px + 8, y + 268 - 32), "STRAIT OF HORMUZ: shipping on alert  •  Kuwait, Bahrain, Oman in the firing line",
           font=font(SANS_B, 16), fill=RED)

    # ---- Row 2: COP31 + Shenzhen summit ----
    y = 430
    rh = 218
    hw = (W - 2 * m - 16) // 2
    panel(d, (m, y, m + hw, y + rh), TEAL)
    px, py = m + 16, y + 10
    py = kicker(d, px, py, "Climate — COP31", TEAL)
    py = headline(d, px, py, "FOSSIL-FUEL FIGHT DEADLOCKS COP31",
                  font(SERIF_B, 27), hw - 32)
    para(d, px, py + 4,
         "Delegates from nearly 200 countries are deadlocked at COP31, "
         "with fossil fuels the sticking point in the final stretch.",
         font(SANS, 19), hw - 32)

    x2 = m + hw + 16
    panel(d, (x2, y, x2 + hw, y + rh), NAVY)
    px, py = x2 + 16, y + 10
    py = kicker(d, px, py, "Diplomacy — Shenzhen", NAVY)
    py = headline(d, px, py, "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
                  font(SERIF_B, 27), hw - 32)
    para(d, px, py + 4,
         "Trump hails a 'momentous' summit with Xi and Putin at APEC in "
         "Shenzhen, as the first trilateral meeting of the three leaders "
         "draws criticism over Iran and Ukraine.",
         font(SANS, 19), hw - 32)

    # ---- Row 3: Peru quake + Estonia border ----
    y = 664
    panel(d, (m, y, m + hw, y + rh), GOLD)
    px, py = m + 16, y + 10
    py = kicker(d, px, py, "Disaster — Peru", GOLD)
    py = headline(d, px, py, "6.9 QUAKE SHAKES PERU'S ANDES",
                  font(SERIF_B, 27), hw - 32)
    para(d, px, py + 4,
         "A magnitude 6.9 earthquake struck near Junin, shaking Lima and "
         "sending residents into the streets. No casualties or major damage "
         "were reported; no tsunami threat.",
         font(SANS, 19), hw - 32)

    panel(d, (x2, y, x2 + hw, y + rh), RED)
    px, py = x2 + 16, y + 10
    py = kicker(d, px, py, "Europe — Russia", RED)
    py = headline(d, px, py, "ESTONIA TO SHUT BORDER WITH RUSSIA",
                  font(SERIF_B, 27), hw - 32)
    para(d, px, py + 4,
         "Estonia moves to close its border with Russia, and Moscow decries "
         "a 'new Iron Curtain' as the standoff on NATO's eastern flank deepens.",
         font(SANS, 19), hw - 32)

    # ---- Row 4: FBI hack (full width, shorter) ----
    y = 898
    panel(d, (m, y, W - m, y + 62), NAVY)
    d.text((m + 16, y + 8), "CYBER  •  FBI PROBES APPARENT HACK OF ITS CRIME DATABASE",
           font=font(SANS_B, 20), fill=NAVY)
    d.text((m + 16, y + 34), "Agents investigate a breach of the National Crime Information Center system used by police nationwide.",
           font=font(SANS, 18), fill=INK)

    # ---- Ticker ----
    d.rectangle([0, 972, W, 1024], fill=NAVY)
    d.text((m, 982), "ALSO:  India 159/1 in Wellington Test  •  ANC fights to hold SA cities  •  Zelensky on Crimean Bridge strikes",
           font=font(SANS, 15), fill=(220, 224, 232))
    d.text((m, 1004), "Cyclone Akvan toll counted  •  Mamdani plans Rikers closure  •  Nepal PM meets Modi  •  Sources: BBC, Reuters, AP, USGS",
           font=font(SANS, 13), fill=(150, 158, 172))

    img.save(OUT, format="PNG")
    print("wrote %s %dx%d" % (OUT, W, H))


if __name__ == "__main__":
    main()
