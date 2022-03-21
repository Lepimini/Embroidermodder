#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    The about_xpm icon.
"""

_3dviews_xpm = [
    "128 128 17 1",
    " 	c None",
    ".	c #000000",
    "+	c #000000",
    "@	c #1f2317",
    "#	c #3b3c34",
    "$	c #3f443e",
    "%	c #3f443e",
    "&	c #666f67",
    "*	c #767a78",
    "=	c #8f948e",
    "-	c #8f948e",
    ";	c #c1bbbe",
    ">	c #c1bbbe",
    ",	c #c3c0c4",
    "'	c #dee4e0",
    ")	c #e7ebe6",
    "!	c #e7ebe6",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                            .....                                                               ",
    "                                                           .......                                                              ",
    "                                                          .........                                                             ",
    "                                                         ...#%@.....                                                            ",
    "                                                        ...%*&#......                                                           ",
    "                                                       ..@&&$.........                                                          ",
    "                                                      ..%&+............                                                         ",
    "                                                     ..*%..@............                                                        ",
    "                                                    ..*...@-.....&+......                                                       ",
    "                                                   ..*...@>-.....&=+......                                                      ",
    "                                                  ..*...@>,-.....&;=+......                                                     ",
    "                                                 ..*...@>,>=.....&;;=+......                                                    ",
    "                                                ..*...@>,>>=.....*-;;-+......                                                   ",
    "                                               ..*...@>,>;>-.....*;;;>-+......                                                  ",
    "                                              ..*...@>,>>>;-..+..*;;>>,;+......                                                 ",
    "                                             ..*...@,,>;>>>-.....*>;>,,,;+......                                                ",
    "                                            ..*...@>,;>;>>,;..+..*;>>,'''>+......                                               ",
    "                                           ..*...@>,>;>>>,,;..+..*;>,,''''>+......                                              ",
    "                                          ..*...@>,>>>>>,')>.....*;>>,')))';+......                                             ",
    "                                         ..*...@>,>;>>>,,')>..+..*;>,,))!))'>+......                                            ",
    "                                        ..*...@>,>>>>>,'))),.....*;;,,')!!!)'>+......                                           ",
    "                                       ..*...@>,>;;>>,,')!!>..+..*;>>,')!!!))'>+......                                          ",
    "                                      ..*...@>,>>>>>,'))!!!,.....*;;,'))!!!!!)';+......                                         ",
    "                                     ..*...@>,;>;>,,,')!!!!,..+..*>>>,')!!!!!!)'>+......                                        ",
    "                                    ..*...@>,>>>>>,''))!!!!,.....*;;>''!!!!!!!!)'>+......                                       ",
    "                                   ..*...@>,;>;>>,,))!!!!!!,..+..*;>>,')!!!!!!!!)'>+......                                      ",
    "                                  ..*...@>,>>>>>,'')!!!!!!!,.....*;>>''!!!!!!!!!))';+......                                     ",
    "                                 ..*...@>,>>;>,,,)))!!!!!!!,..+..*;>>,')!!!!!!!!!!)'>+......                                    ",
    "                                ..*...@>,>;>>>,'''!!!!!!!!!,.....*>;,''!!!!!!!!!!!!)'>+......                                   ",
    "                               ..*...@>,>>;>>,,))!!!!!!!!!!,..+..*;>>,')!!!!!!!!!!!))'>+......                                  ",
    "                              ..*...@>,>;>>>,'')!!!!!!!!!!!,.....*>;,,'!!!!!!!!!!!!!!)'>+......                                 ",
    "                             ..*...@>,>>>>>,,)))!!!!!!!!!!!,..@..*;>>'')!!!!!!!!!!!!!!''>+......                                ",
    "                            ..*...@>,>>;>>,'''!!!!!!!!!!!!!,.+@..*;;,,')!!!!!!!!!!!!!!!)'>+......                               ",
    "                           ..*...@>,>;>>>,'')!!!!!!!!!!!!!!,.@$..*;>>'')!!!!!!!!!!!!!!!!)'>+......                              ",
    "                          ..*...@>,>>>;,,,')!!!!!!!!!!!!!!!,.$$..*>;,,'!!!!!!!!!!!!!!!!!!)'>+......                             ",
    "                         ..&+..@>,>>>>>,'')!!!!!!!!!!!!!!!!=.&$..&;>>'')!!!!!!!!!!!!!!!!!!)'>+......                            ",
    "                        ..#$..@>,;>;>>,,'))!!!!!!!!!!!!!!!;..&#...=>>,'!!!!!!!!!!!!!!!!!!!!)'>+..@...                           ",
    "                       ...*..@,,>>>>>,'))!!!!!!!!!!!!!!!!;..$%.....->,')!!!!!!!!!!!!!!!!!!!))'>+..$...                          ",
    "                      ...$&..-,>>>;,,,''!!!!!!!!!!!!!!!!;+.%@.......-,')!!!!!!!!!!!!!!!!!!!!!)'>+.&....                         ",
    "                      ...%%..+->;>;,'))!!!!!!!!!!!!!!!!;..*..........-,')!!!!!!!!!!!!!!!!!!!!!)'>+@&....                        ",
    "                       ..##...+-;>,,''!!!!!!!!!!!!!!!!>..=...@;+......;'))!!!!!!!!!!!!!!!!!!!!!)'%.*....                        ",
    "                       ...+....+->,'))!!!!!!!!!!!!!!!;..*...@>,-+.....+;'))!!!!!!!!!!!!!!!!!!!!!*.+*....                        ",
    "                       .........+;,')!!!!!!!!!!!!!!!>..*...@>,>>-+......;')!!!!!!!!!!!!!!!!!!!!*..$*....                        ",
    "                       ..........+;'')!!!!!!!!!!!!!;..=...@>,>>;;-+......;')!!!!!!!!!!!!!!!!!!*..#&%....                        ",
    "                       ....$......+>')!!!!!!!!!!!!>..*...@>,>>;>>,-+......-''!!!!!!!!!!!!!!!!*..$&#.....                        ",
    "                       ....%=......+,')!!!!!!!!!!>..*...@>,;>>>>,,,>+.....+;'))!!!!!!!!!!!!!*..&%.......                        ",
    "                       ....%>=......+;')!!!!!!!!>..*...@>,>>>;>,,'''>+......-')!!!!!!!!!!!!*.@*+..#.....                        ",
    "                       .+..%>;=......+>')!!!!!!;..*...@>,>;>>,,''')''>+......;')!!!!!!!!!!*.@*...$-.....                        ",
    "                       .@..%;;;=......+>''!!!!>+.*...@>,>>>;>,,'))!))'>+.....+-'))!!!!!!!*.@*...$,-.....                        ",
    "                       .#..%>;;>-......+,')!!;..*...@>,>;>>>,'')!!!!!)'>+......;'))!!!!!*.@*...$,,-.....                        ",
    "                       .$..%>>>>>-......+>');..*...@>,;>>>>,'')!!!!!!))'>+......;')!!!!*.@*...$,>>=.....                        ",
    "                       .$..%;;>,,,-+..+..+>-.+*...@,,>;>;,,,'))!!!!!!!!)'>+......;')!!*.@*...%,,>>=.....                        ",
    "                       .$..%>>>,,',-...&..+..$...@>>>>>>>,'')!!!!!!!!!!!)'>+......-''*.#*...$,,;>;-.....                        ",
    "                       .$..%;>,,''))-+.+*$......@,,>;>;,,,))!!!!!!!!!!!!!)'>+..@..+;&.#&...$,>>;>>-.....                        ",
    "                       .$..%>;>,'))''-..%*%+...@;,>>>>>,''))!!!!!!!!!!!!!))'>+..&@....#...$,>,>>>>-..+..                        ",
    "                       .$..%>>>,'))!)';..&%...+>>;>;>>,,))!!!!!!!!!!!!!!!!!)'>+..*%+.....$,,>;;>,,;..+..                        ",
    "                       .$..%>;,,')!)!)-.......+->>;>>,''))!!!!!!!!!!!!!!!!!!)'>+.$*%....$,,>;>>>,';.....                        ",
    "                       .$..%>>>,')!!!;.........+-;>>,,))!!!!!!!!!!!!!!!!!!!!!)'>.+%$...#>>;>>>,,,)>..+..                        ",
    "                       .$..%>;,,')!!;.+$........+-;,,'))!!!!!!!!!!!!!!!!!!!!!!)&........=;>;;>,'))>.....                        ",
    "                       .$..%>>>,')!>..*...+......+;,,')!!!!!!!!!!!!!!!!!!!!!!!*.........+=>>,,,')!,..+..                        ",
    "                       .$..%>;,,');..*...@>=......+;,))!!!!!!!!!!!!!!!!!!!!!!*.##.........=;,,')!!,.....                        ",
    "                       .$..%>>>,';..*...@>>>=......+>'))!!!!!!!!!!!!!!!!!!!!*.#&...#+......-,'')!!>..+..                        ",
    "                       .$..%>;,,-..*...@>,>>>=......+>')!!!!!!!!!!!!!!!!!!!*.@*...$>-+......-,'))!,.....                        ",
    "                       .%..%>>>-..*...@>,>;;>>=......+,')!!!!!!!!!!!!!!!!!*.@*...$,>;-+......;'))!,.++..                        ",
    "                       .%..%;>=.+*...@>,>>>>>,,-......+>')!!!!!!!!!!!!!!!*.@*...$,,>;;-+......;')!>.#...                        ",
    "                       .$%.%>=.$*...@>,;>>;>,,,'-+.....+>'))!!!!!!!!!!!!*.@*...%,,>>;>>-+......;')>.&...                        ",
    "                       .@*.%=.$%...@>,>>;;,,,''''-......+>')!!!!!!!!!!!=.@=...$,,>;>>>,,;+.....+-'>@*...                        ",
    "                       ..*##......@,,>>>>>,''))))';......+,')!!!!!!!!!*.@*...$,>;>>>>,,',>+......;;%*...                        ",
    "                       ..&&......@;,;>;>>,''))!!))'-......+>''!!!!!!!*.@*...%,>,>>;,,,')''>+..@%@#-*#...                        ",
    "                       ..%%.....@;>>>>>>,,')!!!!!!))-+.....+>')!!!!!=.@*...$,,>;>>>,')))!)'>+...&***....                        ",
    "                       ..##....@;>>>;>>,'))!!!!!!!))'-......@>')!!!*.@*...$,,>>>;,,'')!!)!)'>+...$*&....                        ",
    "                       .......+-;;;>>>,''))!!!!!!!!!)'-+.....+>')!*.@*...%,>>;;>>,,))!!!!!!)'>+....$....                        ",
    "                      .......@-;;;;>>,'''!!!!!!!!!!!!)'-......+>'*.$*...$,,>>>>,,'')!!!!!!!!)'>+........                        ",
    "                      .......=-;;;>>,,))!!!!!!!!!!!!!!)'-+..#..+&.#%...%,,>;>;,,'))!!!!!!!!!!)'>+.......                        ",
    "                       ......+--;;>,''))!!!!!!!!!!!!!!))'-...%%..@....$,,;>>;,,'')!!!!!!!!!!!!)'>+......                        ",
    "                        ......+-;>,,')!!!!!!!!!!!!!!!!!!)'-...%&@....$,,>>>>>,,))!!!!!!!!!!!!!!)'&......                        ",
    "                         ......+->,'))!!!!!!!!!!!!!!!!!!!));...+....$,,;>;;,,''))!!!!!!!!!!!!!!!&.+.....                        ",
    "                          ......+;,')!!!!!!!!!!!!!!!!!!!!))'-......#>;>;>>,,''!!!!!!!!!!!!!!!!!*.$.....                         ",
    "                           ......+>,')!!!!!!!!!!!!!!!!!!!!)))%....@>;>;>;,,,')!!!!!!!!!!!!!!!!*.$%....                          ",
    "                            ......+>))!!!!!!!!!!!!!!!!!!!!!!'&....$;;;;>>,')!)!!!!!!!!!!!!!!!*.@*....                           ",
    "                             ......+>''!!!!!!!!!!!!!!!!!!!!!!&....%;;;>>,'')!!!!!!!!!!!!!!!!*.@*....                            ",
    "                              ......+,')!!!!!!!!!!!!!!!!!!!!!&.+..$;;;>,,))!!!!!!!!!!!!!!!!*.@*....                             ",
    "                               ......+>')!!!!!!!!!!!!!!!!!!!!*.#..%;;;,,)'!!!!!!!!!!!!!!!!*.@*....                              ",
    "                                ......+>')!!!!!!!!!!!!!!!!!!!*.$..%;>>,,))!!!!!!!!!!!!!!!*.@=....                               ",
    "                                 ......+>')!!!!!!!!!!!!!!!!!!*.$..%>;>,')!!!!!!!!!!!!!!!*.@*....                                ",
    "                                  ......+>')!!!!!!!!!!!!!!!!!*.$..%>>>,,)!!!!!!!!!!!!!!*.@*....                                 ",
    "                                   ......+>')!!!!!!!!!!!!!!!!*.$..%;;,,')!!!!!!!!!!!!!*.@*....                                  ",
    "                                    ......+>')!!!!!!!!!!!!!!!*.$..%>>>,')!!!!!!!!!!!!*.@=....                                   ",
    "                                     ......+>')!!!!!!!!!!!!!!*.$..%>;,,')!!!!!!!!!!!*.@*....                                    ",
    "                                      ......+>')!!!!!!!!!!!!!*.$..%>>>,')!!!!!!!!!!*.@*....                                     ",
    "                                       ......+>')!!!!!!!!!!!!*.$..%>;,,')!!!!!!!!!*.@*....                                      ",
    "                                        ......+>')!!!!!!!!!!!*.$..%>>>,''!!!!!!!!*.@=....                                       ",
    "                                         ......+>''!!!!!!!!!!*.$..%>;,,')!!!!!!!*.@*....                                        ",
    "                                          ......+,')!!!!!!!!!*.$..%>>>,')!!!!!!*.@=....                                         ",
    "                                           ......+>''!!!!!!!!*.$..%>;,,')!!!!!*.@*....                                          ",
    "                                            ......+,')!!!!!!!*.$..%>>>,')!!!!*.@*....                                           ",
    "                                             ......+>')!!!!!!*.$..%>;,,')!!!*.#*....                                            ",
    "                                              ......+>')!!!!!*.$..%>>>,')!!*.@*....                                             ",
    "                                               ......+>')!!!!*.$..%>;,,')!*.@*....                                              ",
    "                                                ......+>'))!!*.$..%>>>,')*.@*....                                               ",
    "                                                 ......+>')))*.%..%>;,,)&.@*....                                                ",
    "                                                  ......+,')!*.&..%>>>,&.#*....                                                 ",
    "                                                   ......+>')&#*..%>;,&.@*....                                                  ",
    "                                                    ......+>'*&*..%>>&.#*....                                                   ",
    "                                                     ...+..+,=*%..%>%.%*....                                                    ",
    "                                                      ...#%#%=&%..%%.$#....                                                     ",
    "                                                       ....****#+.@.......                                                      ",
    "                                                        ....#&&$@........                                                       ",
    "                                                         .....#@........                                                        ",
    "                                                          .............                                                         ",
    "                                                           ...........                                                          ",
    "                                                            .........                                                           ",
    "                                                             .......                                                            ",
    "                                                              .....                                                             ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
    "                                                                                                                                ",
]
