from phonemizer.phonemize import phonemize

def convert(str):
    phonemes = phonemize(str,
                         language='ta',
                         backend='espeak',
                         strip=True,
                         preserve_punctuation=True,
                         with_stress='true')
    return phonemes

if __name__ == "__main__":
    audio_path = "/home/sureshkumar/Documents/TTSDataSet/KGB/wavs/"
    f = open("/home/sureshkumar/Documents/TTSDataSet/KGB/metadata.csv", "r", encoding='utf-8')
    out = open("/home/sureshkumar/Documents/TTSDataSet/KGB/metadata_out.csv", "a", encoding='utf-8')

    for x in f:
      x = x.strip('\n')
      values = x.split("|")

      out_value = audio_path+values[0]+"|"+values[1]+str("\n")
      print(out_value)
      out.write(out_value)