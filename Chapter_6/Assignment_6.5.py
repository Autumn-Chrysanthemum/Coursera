text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")

#cut = text[pos+1:]

#host = float(cut.lstrip())

host = float(text[pos+1:])

print host