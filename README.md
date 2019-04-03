# pos2pickandplace

notes: kicad's coordinate system counts positively in the Y axis toward the
bottom of the screen, but when exporting a .POS file, the Y coordinates are
negative for some reason, as if someone multiplied the kicad Y coordinate by -1

rotation:  a part oriented vertially (matching the way it sits on the spools of
the machine) can set as -90° or +90° in kicad, but -90° will be 270° in the
.POS file.  A part set to +90° in kicad shows up as 90° in the POS file.

a diode with a rotation of 180° in kicad and also the POS file has pin 1
KATHODE on the right, and is oriented horizontally.

a diode with a rotation of 90° in kicad and also the POS file has pin 1 KATHODE
on the bottom, and is oriented vertically.
