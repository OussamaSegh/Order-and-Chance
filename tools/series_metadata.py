"""Canonical series catalog: parts, titles and subtitles.

common/series-catalog.json is the source. This module writes the flat subtitle
file, its TeX lookup, and the series page used on title pages and back covers.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CATALOG=ROOT/'common/series-catalog.json'

def catalog():
    return json.loads(CATALOG.read_text())
def subtitles():
    return {number:volume['subtitle'] for number,volume in catalog()['volumes'].items()}
def subtitle(number):
    return subtitles().get(str(number),'')
def parts():
    return catalog()['parts']
def volume(number):
    return catalog()['volumes'][str(number)]
def part_of(number):
    for part in parts():
        if str(number) in part['volumes']:
            return part
    raise KeyError(number)
def cover_subtitle_lines(number):
    text=subtitle(number)
    if str(number)=='1' and text=='Proof, Problem Solving and Mathematical Thinking':
        first,second=text.split(' and ',1)
        return [first,'and '+second]
    if str(number)=='15' and text=='The Meeting of Structure and Randomness':
        return ['The Meeting of Structure','and Randomness']
    return [text]

def tex_source():
    definitions=[r'% Generated from series-catalog.json by tools/series_metadata.py.',
      r'\newcommand{\volumesubtitledef}[2]{\expandafter\def\csname ocsubtitle@#1\endcsname{#2}}',
      r'\newcommand{\volumesubtitle}[1]{\ifcsname ocsubtitle@#1\endcsname\csname ocsubtitle@#1\endcsname\fi}']
    for number,value in subtitles().items():
        assert not any(c in value for c in '\\{}%&_$#'),value
        definitions.append(r'\volumesubtitledef{'+number+'}{'+value+'}')
    series=catalog().get('subtitle','')
    assert series and not any(c in series for c in '\\{}%&_$#')
    definitions.append(r'\providecommand{\seriessubtitle}{}')
    definitions.append(r'\renewcommand{\seriessubtitle}{'+series+'}')
    definitions.append(r'\newcommand{\volumecoversubtitle}[1]{\csname occoversubtitle@#1\endcsname}')
    for number in subtitles():
        definitions.append(r'\expandafter\def\csname occoversubtitle@'+number+r'\endcsname{'+r'\\'.join(cover_subtitle_lines(number))+'}')
    return '\n'.join(definitions)+'\n'

def series_tex():
    lines=['% Generated from series-catalog.json by tools/series_metadata.py.',
           '% The series list for every series page and back cover.']
    volumes=catalog()['volumes']
    for part in parts():
        lines.append(r'\seriespart{Part '+part['roman']+'. '+part['name']+'}')
        for number in part['volumes']:
            item=volumes[number]
            lines.append(r'\seriesvolume{'+number+'}{'+item['title']+'}{'+item['subtitle']+'}')
    return '\n'.join(lines)+'\n'

def flat_subtitles():
    return json.dumps(subtitles(), indent=2)+'\n'

def main():
    data=subtitles()
    assert len(data)==15 and len(set(data.values()))==15
    assert [number for part in parts() for number in part['volumes']]==[str(n) for n in range(1,16)]
    (ROOT/'common/volume-subtitles.json').write_text(flat_subtitles())
    (ROOT/'common/volume-subtitles.tex').write_text(tex_source())
    (ROOT/'common/series.tex').write_text(series_tex())
def check_sync():
    if (ROOT/'common/volume-subtitles.tex').read_text()!=tex_source():
        raise SystemExit('Subtitle TeX is stale; run python3 tools/series_metadata.py')
    if (ROOT/'common/volume-subtitles.json').read_text()!=flat_subtitles():
        raise SystemExit('Subtitle JSON is stale; run python3 tools/series_metadata.py')
    if (ROOT/'common/series.tex').read_text()!=series_tex():
        raise SystemExit('Series page is stale; run python3 tools/series_metadata.py')

if __name__=='__main__':
    import sys
    check_sync() if '--check' in sys.argv else main()
