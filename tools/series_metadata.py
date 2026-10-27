"""Canonical volume subtitles shared by covers, book front matter and web/KDP metadata."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def subtitles():
    return json.loads((ROOT/'common/volume-subtitles.json').read_text())
def subtitle(number):
    return subtitles().get(str(number),'')
def tex_source():
    definitions=[r'% Generated from volume-subtitles.json by tools/series_metadata.py.',
      r'\newcommand{\volumesubtitledef}[2]{\expandafter\def\csname ocsubtitle@#1\endcsname{#2}}',
      r'\newcommand{\volumesubtitle}[1]{\ifcsname ocsubtitle@#1\endcsname\csname ocsubtitle@#1\endcsname\fi}']
    for number,value in subtitles().items():
        assert not any(c in value for c in '\\{}%&_$#'),value
        definitions.append(r'\volumesubtitledef{'+number+'}{'+value+'}')
    return '\n'.join(definitions)+'\n'
def main():
    data=subtitles()
    assert len(data)==19 and len(set(data.values()))==19
    (ROOT/'common/volume-subtitles.tex').write_text(tex_source())
def check_sync():
    target=ROOT/'common/volume-subtitles.tex'
    if not target.exists() or target.read_text()!=tex_source():
        raise SystemExit('Subtitle TeX is stale; run python3 tools/series_metadata.py')

if __name__=='__main__':
    import sys
    check_sync() if '--check' in sys.argv else main()
