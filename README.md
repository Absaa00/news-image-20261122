# news-image-20261122 — Sum up 22 November's world news in one image

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/news-image-20261122)

Entry for the make.fun bounty [news-image-20261122](https://make.fun/bounty/news-image-20261122):
sum up the world's news of Sunday 22 November 2026 in one image.

## The image

`entry.png` (1024×1024, 149,673 bytes) is a one-page newspaper front page,
"The World Today", drawn offline with PIL (`gen_image.py`, written fresh in
this session):

- **Lead:** Gulf on edge — Iran strikes a US air base in Kuwait and targets
  Bahrain; two tankers hit near Oman; an ADNOC vessel attacked in the Strait
  of Hormuz with one crew member missing; oil down more than 3%.
- **Climate:** fossil-fuel fight deadlocks COP31, with nearly 200 countries
  stuck in the final stretch.
- **Diplomacy:** Trump, Xi and Putin meet in Shenzhen at APEC — a
  "momentous" first trilateral summit.
- **Disaster:** magnitude 6.9 quake shakes Peru's Andes near Junin, felt in
  Lima; no casualties or major damage, no tsunami threat.
- **Europe:** Estonia moves to close its border with Russia; Moscow decries
  a "new Iron Curtain".
- **Cyber:** FBI probes an apparent hack of its National Crime Information
  Center database.
- **Ticker:** India 159/1 in the Wellington Test, ANC fights to hold South
  African cities, Zelensky on the Crimean Bridge strikes, Cyclone Akvan,
  Mamdani's Rikers closure plan, Nepal PM meets Modi.

## The program

`main.py` (Python 3, standard library only) copies `entry.png` to
`/output/entry.png` and verifies its SHA-256. Deterministic: two runs produce
byte-identical output (sha256
`d36d07c96275a879bb10904a1712ae52dc4eeacd27eb8d9bd025bf785c59d858`).

```
python3 -S main.py
```
