#!/usr/bin/python
# -*- coding: utf8 -*-

import argparse
import collections
import os
import re
import string


REMY = """
        :oooooooooooo+
     +hhmNNNNNNNNNNNNNhhy`
  .--yNNNNNNNNNNNNNNNNNNm:--
  oNNNNNyoooooooooooooNNNNNm`
`ymNNNNN+            .mNNNNNh:
.mNNN+   .mNm`   oNN+   .mNNN+
.mNNN+   `+o+    :oo-   .mNNN+
.mNNNo```` .::::::: ````-mNNN+
  oNNNNNNm`oh++++om`oNNNNNNm`
  oNNNNNo. oNNNNNNm``:NNNNNm`
  ./NNm:.  oNNNNNNm` `:yNNs-
    `+hhhhhmNNNNNNNhhhhhy.`
           :oooooo+
"""


# These have to go first, or they will get overridden by later keys.
REMYSPEAK = collections.OrderedDict({
    "(ye )?new(e)?( )?biz": "new orders of business",
    "(ye )?old(e)?( )?biz": "previously discussed business",
    "cycle on": "spend time on",
    "open loop": "unfinished task",
})
# Order-insensitive keys
REMYSPEAK.update({
    "what's good": "how are you",
    "kettle of fish": "matter",
    "cycle": "period of time",
    "cycles": "time available to spend on work",
    "loop": "task",
    "loops": "current tasks",
    "motherfucker": "fellow",
    "biz": "five",
    "hunny": "a hundred",
    "hundo": "a hundred",
    "step out": "smoke",
    "homeboy": "dude",
    "homegirl": "girl",
    "wat": "what",
    "chops": "skills",
    "foo": "skill",
    "step outside": "smoke",
    "fuck this": "education is important",
    "(<)?buz(z)+er(/?>)?": "nope",
    "lolz": "*giggle*",
    "lolol": "haha",
    "lollerskates": "hilarious",
    "(a|one) minute": "a long time",
    "lo(ad|de)stone": "bad luck",
    "beverage(s)?": "alcohol\\1",
    "may or may not be": "is",
    'tomo': 'tomorrow',
    'def': 'definitely',
    "&": "steps into the background",
    "hosed": "destroyed",
    "EoB": "End of Business",
    "moar": "additional",
    "G/B/U": "Good/Bad/Ugly",
    "(1337|leet|l337|l33t)z(o|0)r": "advanced hacker",
    "dece": "decent",
    "qual": "quality",
    "holy business": "this situation is getting out of hand",
    "(ob|ab)sanity": "absurd insanity",
  })

def translate_remyspeak(text):
    cap_map = [str.lower, str.capitalize, str.upper]
    # figure out casing of input
    try:
        if not text:
            return text
        if text[0] in string.lowercase:
            # Ex: 'a'
            case = 0
        elif text[1] in string.lowercase or text[1] not in string.letters:
            # Ex: 'Aa' or 'A '
            case = 1
        else:
            case = 2
    except:
        case = 0

    text = text.lower()
    for item in REMYSPEAK:
        text = re.sub(r'\b{}\b'.format(item), REMYSPEAK[item], text)

    return cap_map[case](text)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('text', nargs="+", help='Remyspeak to be translated.')
    p.add_argument('-n', '--nohead', action='store_true',
                   help='Don\'t print the ASCII Remy head.')
    p.add_argument('-s', '--speak', action='store_true',
                   help='Say it')
    args = p.parse_args()

    if not args.nohead:
        print REMY
    else:
        print "\n"

    result = translate_remyspeak(" ".join(args.text))
    print result
    print "\n"

    if args.speak:
        os.system("espeak %r" % result)
