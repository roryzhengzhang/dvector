import os
import re
import glob
from pathlib import Path
from pydub import AudioSegment

os.chdir('accent')
for file in glob.glob('*/*.mp3', recursive = True):
  accent = re.match(r'([A-Za-z]+)', Path(file).stem)
  accent = accent.groups(0)[0]
  sound = AudioSegment.from_mp3(file)
  out = os.path.abspath(f"~/dvector/accent_wav/{accent}")
  if not os.path.exists(out):
    os.makedirs(out)
  sound.export(os.path.abspath(f"~/dvector/accent_wav/{accent}/{Path(file).stem}.wav"), format="wav")


