# navigate_by_keywords
Extract most important words from each page of a website and use these as an alternate method for navigation

Using the ideas from https://peekaboo-vision.blogspot.com/2012/11/a-wordcloud-in-python.html as a starting point for keyword collection

pip install sklearn fitz pymupdf

Sample output:

For overall commonality, list the words which were in the top set for more than one doc, and the docs

word: number of docs: total appearances where key: list of docs where this is a key word
available: 2: 147:      can-good-work-solve-the-productivity-puzzle.pdf, rsa-ffcc-our-future-in-the-land.pdf
citizens: 2: 255:       democratising-decisions-tech-report.pdf, rsa-citizen-participation-and-the-economy.pdf
city: 2: 85:    manifesto-for-city-led-green-recovery.pdf, rsa-making-home.pdf
council: 2: 80: manifesto-for-city-led-green-recovery.pdf, rsa-citizen-participation-and-the-economy.pdf
data: 2: 68:    a-new-blueprint-for-good-work.pdf, democratising-decisions-tech-report.pdf
economy: 3: 105:        a-new-blueprint-for-good-work.pdf, rsa-citizen-participation-and-the-economy.pdf, rsa_four-futures-of-work.pdf
future: 3: 78:  retailtherapy.pdf, rsa-ffcc-our-future-in-the-land.pdf, rsa_four-futures-of-work.pdf
good: 3: 62:    a-new-blueprint-for-good-work.pdf, can-good-work-solve-the-productivity-puzzle.pdf, retailtherapy.pdf
local: 3: 100:  manifesto-for-city-led-green-recovery.pdf, rsa-making-home.pdf, the-rsa-schools-without-walls.pdf
new: 3: 128:    a-new-blueprint-for-good-work.pdf, retailtherapy.pdf, rsa_four-futures-of-work.pdf
people: 4: 240: can-good-work-solve-the-productivity-puzzle.pdf, rsa-citizen-participation-and-the-economy.pdf, rsa-ffcc-our-future-in-the-land.pdf, rsa-making-home.pdf
policy: 2: 93:  manifesto-for-city-led-green-recovery.pdf, rsa-citizen-participation-and-the-economy.pdf
public: 4: 185: democratising-decisions-tech-report.pdf, manifesto-for-city-led-green-recovery.pdf, rsa-citizen-participation-and-the-economy.pdf, rsa-ffcc-our-future-in-the-land.pdf
technology: 2: 183:     democratising-decisions-tech-report.pdf, rsa_four-futures-of-work.pdf
uk: 4: 98:      can-good-work-solve-the-productivity-puzzle.pdf, rsa-citizen-participation-and-the-economy.pdf, rsa-ffcc-our-future-in-the-land.pdf, rsa_four-futures-of-work.pdf
work: 5: 103:   a-new-blueprint-for-good-work.pdf, can-good-work-solve-the-productivity-puzzle.pdf, retailtherapy.pdf, rsa_four-futures-of-work.pdf, the-rsa-schools-without-walls.pdf
workers: 4: 223:        a-new-blueprint-for-good-work.pdf, can-good-work-solve-the-productivity-puzzle.pdf, retailtherapy.pdf, rsa_four-futures-of-work.pdf

Also print the list of docs with how many key words they have
More is an indication they are more central to this list

 7
rsa-citizen-participation-and-the-economy.pdf, rsa_four-futures-of-work.pdf
 6
can-good-work-solve-the-productivity-puzzle.pdf, a-new-blueprint-for-good-work.pdf
 5
rsa-ffcc-our-future-in-the-land.pdf, manifesto-for-city-led-green-recovery.pdf, retailtherapy.pdf
 4
democratising-decisions-tech-report.pdf
 3
rsa-making-home.pdf
 2
the-rsa-schools-without-walls.pdf