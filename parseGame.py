import requests
import os
import copy
import json
import re
import board


if __name__ == '__main__':
    # x = "https://theweekinchess.com/twic"
    # r = requests.get(x)
    # lines = r.text.split("\n")
    # for line in lines:
    #     if(line.__contains__('''<td><a href="http://www.theweekinchess.com/zips/twic''') and line.__contains__('''g.zip">PGN</a></td>''')):
    #         line = line.split('''"''')
    #         line = line.pop(1)
    #         url = copy.deepcopy(line)
    #         filename = line.split("/")
    #         filename = filename.pop(4)
    #         cmd = "wget -O ~/Documents/chess_engine/games/" + filename + " " + url
    #         os.system(cmd)
    f = open("/home/amly/Documents/chess_engine/games/twic920.pgn", "r")
    moves = ""
    game = []

    for i in f.readlines():
        if "[" in i:
            if 'Result' in i or 'WhitElo' in i or 'BlackElo' in i or 'Opening' in i or 'Variation' in i:
                x = i[1:len(i) - 1].split(" ")
                game.append({x[0][:5], x[1]})
        elif "." in i or "-" in i:
            moves += i
        elif len(game) > 0:
            moves = moves.replace('\n', ' ')        # remove line breaks
            moves = re.sub("[0-9]+\. ", "",  moves) # remove xx.
            moves = moves.replace(' ', ', ')        # insert comma
            moves = moves[:len(moves) - 2]          # remove trailing comma
            moves = moves.split(',')                # turn into array
            bstate = board.Board()                  # init board
            arrg = 0
            for s in bstate.states:
                #print(arrg,":",s.loc.acn, s.piece)
                arrg += 1
            if len(moves) > 1:
                wtom = False
                for i, m in enumerate(moves):
                    wtom = not wtom
                    m = m.strip(" ")
                    size = len(m)
                    if m.__contains__("x"):
                        m = m.replace("x", "")
                        m = m + "x"
                        size -= 1
                    if m.__contains__("+"):
                        size -= 1
                    #print(m, "*************")

                    if re.fullmatch("[a-h]{1,2}[1-8][+]*[x]*", m):  # all pawn moves
                        if size == 2:
                            bstate.move(m[0] + str(int(m[1]) - 1), m)
                        else:
                            if wtom:
                                pawns = bstate.w
                                diff = 1
                            else:
                                pawns = bstate.b
                                diff = -1

                            if size == 3:
                                srcLoc = m[0]
                                desLoc = m[1:3]
                            else:
                                srcLoc = m[0:2]
                                desLoc = m[2:4]
                            for p in pawns:
                                if not re.match(p.loc.acn, srcLoc): # test regex match
                                    pawns.remove(p)
                            if len(pawns) == 1:
                                x = 0
                                #print(pawns.pop(0).loc.acn, "only pawn move")
                            else:
                                x = 0
                                print(pawns, "    ::mofin pawns B")
                    elif re.match("R|B|N|Q|K", m[0]):
                        if size == 3:
                            #bstate.pmove(m[1:3], wtom, m[0])
                            x = 0
                        elif size == 4:
                            #bstate.pmove(m[2:3], wtom, m[0], m[1])
                            x = 0
                        else:
                            #bstate.pmove(m[3:4], wtom, m[0], m[1:2])
                            x = 0

                    elif m.__contains__("x"):
                        x = 0
                    else:
                        x = 0
            moves = ""
            game = []


else:
    exit(-1)
