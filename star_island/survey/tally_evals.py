""" Tally the 2026 All Star evaluations for the Star Meeting slides

Counts how many respondents mentioned each favorite activity and each
volunteer area of interest.  No names or emails are written out.

Usage:
    python star_island/survey/tally_evals.py
"""
import json
import os
import re

import pandas as pd

repo = os.path.join(os.path.dirname(__file__), '..', '..')
csv_file = os.path.join(repo, 'survey', '2026_All_Star_Evals.csv')
out_file = os.path.join(repo, 'slides', 'eval_tally.json')

# Activity label -> regex matched against "enjoyed the most" answers
ACTIVITIES = {
    'Lecture / Speaker': r'lectur|speaker|dr\. jen',
    '15x20': r'15\s*x\s*20',
    'Chapel': r'chapel',
    'Name That Tune': r'name that tune',
    'Social Hour': r'social hour',
    'Porchcraft': r'porch\s*craft',
    'Talks on the Rocks': r'talks on the rocks',
    'Trivia': r'trivia',
    'Stevie Wonder Night': r'stevie wonder',
    'Walking the island': r'walking',
}


def main():
    df = pd.read_csv(csv_file)
    cols = df.columns
    enjoyed = df[cols[3]].dropna().str.lower()
    volunteer = df[cols[7]].dropna()

    activities = {label: int(enjoyed.str.contains(rx, regex=True).sum())
                  for label, rx in ACTIVITIES.items()}

    # Volunteer areas: checkbox items look like "Area - Job"
    areas = {}
    for answer in volunteer:
        found = {m.strip() for m in re.findall(r'(?:^|, )([A-Z][\w/ ]+?) - ', answer)}
        for area in found:
            areas[area] = areas.get(area, 0) + 1

    tally = dict(
        n_responses=int(len(df)),
        n_enjoyed=int(len(enjoyed)),
        n_volunteer=int(len(volunteer)),
        activities=dict(sorted(activities.items(), key=lambda kv: -kv[1])),
        volunteer_areas=dict(sorted(areas.items(), key=lambda kv: -kv[1])),
    )
    with open(out_file, 'w') as f:
        json.dump(tally, f, indent=2)
    print(json.dumps(tally, indent=2))


if __name__ == '__main__':
    main()
