# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:00:59 2020

@author: Paras

"""

import cv2
from shapely import geometry
import time

t = time.time()
def line_intersection(line1, line2):
        
    line1 = geometry.LineString(line1)
    line2 = geometry.LineString(line2)
    x = str(line1.intersection(line2))
    if 'POINT' in x:
        return True
    else:
        return False
    
def graph_generation(empty_cells):
    counter = 0
    graph = {}
    threshold = 200   ## Search bubble radius
    for cell in empty_cells:
        cell_edges = [[cell[0], cell[1]],[cell[1], cell[2]],[cell[2], cell[3]],[cell[3], cell[0]]]
        cell_mp = ((cell[3][0]+cell[0][0])//2, (cell[1][1]+cell[0][1])//2)   ## mid point of the cell
        graph[cell_mp] = {}
        
        for acell in empty_cells:
            if cell == acell:
                continue
            acell_mp = ((acell[3][0]+acell[0][0])//2, (acell[1][1]+acell[0][1])//2)  ## mid point of the acell
            distance = int(((cell_mp[1] - acell_mp[1])**2 + (cell_mp[0] - acell_mp[0])**2)**0.5)
            
            if distance < threshold:
                acell_edges = [[acell[0], acell[1]],[acell[1], acell[2]],[acell[2], acell[3]],[acell[3], acell[0]]]
                for i in cell_edges:
                    for e in acell_edges:
                        counter+=1
                        if line_intersection(i,e):
                            
                            graph[cell_mp].update({acell_mp: distance})
                            break
                    else:
                        continue
                    break
    print(counter)   
    return graph


empty_cells = [[(337, 0), (337, 56), (393, 56), (393, 0)], [(393, 0), (393, 56), (450, 56), (450, 0)], [(421, 84), (421, 112), (450, 112), (450, 84)], [(421, 56), (421, 84), (450, 84), (450, 56)], [(414, 91), (414, 98), (421, 98), (421, 91)], [(414, 84), (414, 91), (421, 91), (421, 84)], [(407, 70), (407, 84), (421, 84), (421, 70)], [(407, 56), (407, 70), (421, 70), (421, 56)], [(400, 70), (400, 77), (407, 77), (407, 70)], [(393, 56), (393, 63), (400, 63), (400, 56)], [(400, 63), (400, 70), (407, 70), (407, 63)], [(400, 56), (400, 63), (407, 63), (407, 56)], [(337, 56), (337, 84), (365, 84), (365, 56)], [(365, 56), (365, 70), (379, 70), (379, 56)], [(379, 56), (379, 63), (386, 63), (386, 56)], [(365, 70), (365, 77), (372, 77), (372, 70)], [(365, 77), (365, 84), (372, 84), (372, 77)], [(372, 70), (372, 77), (379, 77), (379, 70)], [(365, 84), (365, 91), (372, 91), (372, 84)], [(337, 84), (337, 98), (351, 98), (351, 84)], [(337, 98), (337, 112), (351, 112), (351, 98)], [(351, 84), (351, 98), (365, 98), (365, 84)], [(351, 98), (351, 105), (358, 105), (358, 98)], [(351, 105), (351, 112), (358, 112), (358, 105)], [(337, 168), (337, 225), (393, 225), (393, 168)], [(393, 168), (393, 225), (450, 225), (450, 168)], [(393, 140), (393, 168), (421, 168), (421, 140)], [(421, 140), (421, 168), (450, 168), (450, 140)], [(421, 126), (421, 140), (435, 140), (435, 126)], [(435, 126), (435, 140), (450, 140), (450, 126)], [(435, 112), (435, 126), (450, 126), (450, 112)], [(428, 119), (428, 126), (435, 126), (435, 119)], [(428, 112), (428, 119), (435, 119), (435, 112)], [(393, 126), (393, 140), (407, 140), (407, 126)], [(407, 126), (407, 140), (421, 140), (421, 126)], [(337, 140), (337, 168), (365, 168), (365, 140)], [(365, 140), (365, 168), (393, 168), (393, 140)], [(365, 126), (365, 140), (379, 140), (379, 126)], [(379, 126), (379, 140), (393, 140), (393, 126)], [(337, 112), (337, 126), (351, 126), (351, 112)], [(337, 126), (337, 140), (351, 140), (351, 126)], [(351, 126), (351, 140), (365, 140), (365, 126)], [(309, 140), (309, 168), (337, 168), (337, 140)], [(309, 112), (309, 140), (337, 140), (337, 112)], [(302, 147), (302, 154), (309, 154), (309, 147)], [(302, 140), (302, 147), (309, 147), (309, 140)], [(302, 161), (302, 168), (309, 168), (309, 161)], [(302, 154), (302, 161), (309, 161), (309, 154)], [(302, 119), (302, 126), (309, 126), (309, 119)], [(302, 112), (302, 119), (309, 119), (309, 112)], [(302, 133), (302, 140), (309, 140), (309, 133)], [(302, 126), (302, 133), (309, 133), (309, 126)], [(309, 196), (309, 225), (337, 225), (337, 196)], [(309, 168), (309, 196), (337, 196), (337, 168)], [(302, 203), (302, 210), (309, 210), (309, 203)], [(302, 196), (302, 203), (309, 203), (309, 196)], [(302, 217), (302, 225), (309, 225), (309, 217)], [(302, 210), (302, 217), (309, 217), (309, 210)], [(302, 175), (302, 182), (309, 182), (309, 175)], [(302, 168), (302, 175), (309, 175), (309, 168)], [(302, 189), (302, 196), (309, 196), (309, 189)], [(302, 182), (302, 189), (309, 189), (309, 182)], [(225, 0), (225, 56), (281, 56), (281, 0)], [(281, 0), (281, 56), (337, 56), (337, 0)], [(309, 84), (309, 112), (337, 112), (337, 84)], [(309, 56), (309, 84), (337, 84), (337, 56)], [(302, 91), (302, 98), (309, 98), (309, 91)], [(302, 84), (302, 91), (309, 91), (309, 84)], [(302, 105), (302, 112), (309, 112), (309, 105)], [(302, 98), (302, 105), (309, 105), (309, 98)], [(295, 56), (295, 63), (302, 63), (302, 56)], [(302, 63), (302, 70), (309, 70), (309, 63)], [(302, 56), (302, 63), (309, 63), (309, 56)], [(302, 77), (302, 84), (309, 84), (309, 77)], [(302, 70), (302, 77), (309, 77), (309, 70)], [(281, 56), (281, 63), (288, 63), (288, 56)], [(288, 56), (288, 63), (295, 63), (295, 56)], [(267, 56), (267, 63), (274, 63), (274, 56)], [(274, 56), (274, 63), (281, 63), (281, 56)], [(253, 56), (253, 63), (260, 63), (260, 56)], [(260, 56), (260, 63), (267, 63), (267, 56)], [(239, 56), (239, 63), (246, 63), (246, 56)], [(246, 56), (246, 63), (253, 63), (253, 56)], [(225, 56), (225, 63), (232, 63), (232, 56)], [(232, 56), (232, 63), (239, 63), (239, 56)], [(337, 225), (337, 281), (393, 281), (393, 225)], [(393, 281), (393, 337), (450, 337), (450, 281)], [(393, 225), (393, 281), (450, 281), (450, 225)], [(365, 281), (365, 295), (379, 295), (379, 281)], [(379, 295), (379, 309), (393, 309), (393, 295)], [(379, 281), (379, 295), (393, 295), (393, 281)], [(365, 295), (365, 302), (372, 302), (372, 295)], [(372, 302), (372, 309), (379, 309), (379, 302)], [(372, 295), (372, 302), (379, 302), (379, 295)], [(379, 309), (379, 323), (393, 323), (393, 309)], [(386, 323), (386, 330), (393, 330), (393, 323)], [(351, 281), (351, 288), (358, 288), (358, 281)], [(358, 288), (358, 295), (365, 295), (365, 288)], [(358, 281), (358, 288), (365, 288), (365, 281)], [(337, 281), (337, 288), (344, 288), (344, 281)], [(337, 393), (337, 450), (393, 450), (393, 393)], [(393, 337), (393, 393), (450, 393), (450, 337)], [(421, 421), (421, 450), (450, 450), (450, 421)], [(421, 393), (421, 421), (450, 421), (450, 393)], [(393, 435), (393, 450), (407, 450), (407, 435)], [(407, 435), (407, 450), (421, 450), (421, 435)], [(407, 428), (407, 435), (414, 435), (414, 428)], [(414, 428), (414, 435), (421, 435), (421, 428)], [(393, 428), (393, 435), (400, 435), (400, 428)], [(400, 428), (400, 435), (407, 435), (407, 428)], [(393, 393), (393, 407), (407, 407), (407, 393)], [(407, 393), (407, 407), (421, 407), (421, 393)], [(386, 344), (386, 351), (393, 351), (393, 344)], [(379, 358), (379, 365), (386, 365), (386, 358)], [(386, 358), (386, 365), (393, 365), (393, 358)], [(386, 351), (386, 358), (393, 358), (393, 351)], [(365, 379), (365, 393), (379, 393), (379, 379)], [(379, 379), (379, 393), (393, 393), (393, 379)], [(379, 365), (379, 379), (393, 379), (393, 365)], [(365, 372), (365, 379), (372, 379), (372, 372)], [(372, 372), (372, 379), (379, 379), (379, 372)], [(372, 365), (372, 372), (379, 372), (379, 365)], [(351, 386), (351, 393), (358, 393), (358, 386)], [(358, 386), (358, 393), (365, 393), (365, 386)], [(358, 379), (358, 386), (365, 386), (365, 379)], [(337, 386), (337, 393), (344, 393), (344, 386)], [(225, 337), (225, 393), (281, 393), (281, 337)], [(225, 393), (225, 450), (281, 450), (281, 393)], [(281, 393), (281, 450), (337, 450), (337, 393)], [(281, 365), (281, 393), (309, 393), (309, 365)], [(309, 358), (309, 365), (316, 365), (316, 358)], [(309, 365), (309, 379), (323, 379), (323, 365)], [(309, 379), (309, 393), (323, 393), (323, 379)], [(323, 379), (323, 393), (337, 393), (337, 379)], [(323, 372), (323, 379), (330, 379), (330, 372)], [(281, 337), (281, 351), (295, 351), (295, 337)], [(281, 351), (281, 365), (295, 365), (295, 351)], [(295, 351), (295, 365), (309, 365), (309, 351)], [(295, 337), (295, 344), (302, 344), (302, 337)], [(295, 344), (295, 351), (302, 351), (302, 344)], [(302, 344), (302, 351), (309, 351), (309, 344)], [(225, 225), (225, 281), (281, 281), (281, 225)], [(225, 281), (225, 337), (281, 337), (281, 281)], [(281, 225), (281, 281), (337, 281), (337, 225)], [(281, 281), (281, 309), (309, 309), (309, 281)], [(309, 281), (309, 295), (323, 295), (323, 281)], [(309, 295), (309, 309), (323, 309), (323, 295)], [(323, 281), (323, 295), (337, 295), (337, 281)], [(323, 295), (323, 302), (330, 302), (330, 295)], [(309, 309), (309, 316), (316, 316), (316, 309)], [(309, 316), (309, 323), (316, 323), (316, 316)], [(316, 309), (316, 316), (323, 316), (323, 309)], [(281, 309), (281, 323), (295, 323), (295, 309)], [(281, 323), (281, 337), (295, 337), (295, 323)], [(295, 309), (295, 323), (309, 323), (309, 309)], [(295, 323), (295, 330), (302, 330), (302, 323)], [(295, 330), (295, 337), (302, 337), (302, 330)], [(302, 323), (302, 330), (309, 330), (309, 323)], [(112, 225), (112, 281), (168, 281), (168, 225)], [(168, 281), (168, 337), (225, 337), (225, 281)], [(168, 225), (168, 281), (225, 281), (225, 225)], [(140, 281), (140, 309), (168, 309), (168, 281)], [(154, 309), (154, 323), (168, 323), (168, 309)], [(161, 323), (161, 330), (168, 330), (168, 323)], [(140, 309), (140, 316), (147, 316), (147, 309)], [(147, 316), (147, 323), (154, 323), (154, 316)], [(147, 309), (147, 316), (154, 316), (154, 309)], [(112, 281), (112, 295), (126, 295), (126, 281)], [(126, 281), (126, 295), (140, 295), (140, 281)], [(126, 295), (126, 302), (133, 302), (133, 295)], [(133, 302), (133, 309), (140, 309), (140, 302)], [(133, 295), (133, 302), (140, 302), (140, 295)], [(119, 295), (119, 302), (126, 302), (126, 295)], [(112, 393), (112, 450), (168, 450), (168, 393)], [(168, 393), (168, 450), (225, 450), (225, 393)], [(196, 337), (196, 351), (210, 351), (210, 337)], [(210, 351), (210, 365), (225, 365), (225, 351)], [(210, 337), (210, 351), (225, 351), (225, 337)], [(196, 351), (196, 358), (203, 358), (203, 351)], [(203, 351), (203, 358), (210, 358), (210, 351)], [(196, 379), (196, 393), (210, 393), (210, 379)], [(210, 379), (210, 393), (225, 393), (225, 379)], [(210, 372), (210, 379), (217, 379), (217, 372)], [(217, 372), (217, 379), (225, 379), (225, 372)], [(217, 365), (217, 372), (225, 372), (225, 365)], [(196, 372), (196, 379), (203, 379), (203, 372)], [(203, 372), (203, 379), (210, 379), (210, 372)], [(168, 379), (168, 393), (182, 393), (182, 379)], [(182, 379), (182, 393), (196, 393), (196, 379)], [(182, 372), (182, 379), (189, 379), (189, 372)], [(189, 372), (189, 379), (196, 379), (196, 372)], [(168, 372), (168, 379), (175, 379), (175, 372)], [(175, 372), (175, 379), (182, 379), (182, 372)], [(182, 337), (182, 344), (189, 344), (189, 337)], [(189, 344), (189, 351), (196, 351), (196, 344)], [(189, 337), (189, 344), (196, 344), (196, 337)], [(140, 379), (140, 393), (154, 393), (154, 379)], [(154, 379), (154, 393), (168, 393), (168, 379)], [(154, 372), (154, 379), (161, 379), (161, 372)], [(161, 372), (161, 379), (168, 379), (168, 372)], [(140, 372), (140, 379), (147, 379), (147, 372)], [(147, 372), (147, 379), (154, 379), (154, 372)], [(112, 379), (112, 393), (126, 393), (126, 379)], [(126, 379), (126, 393), (140, 393), (140, 379)], [(126, 372), (126, 379), (133, 379), (133, 372)], [(133, 372), (133, 379), (140, 379), (140, 372)], [(112, 372), (112, 379), (119, 379), (119, 372)], [(119, 372), (119, 379), (126, 379), (126, 372)], [(0, 337), (0, 393), (56, 393), (56, 337)], [(0, 393), (0, 450), (56, 450), (56, 393)], [(56, 393), (56, 450), (112, 450), (112, 393)], [(84, 379), (84, 393), (98, 393), (98, 379)], [(98, 379), (98, 393), (112, 393), (112, 379)], [(98, 372), (98, 379), (105, 379), (105, 372)], [(105, 372), (105, 379), (112, 379), (112, 372)], [(84, 372), (84, 379), (91, 379), (91, 372)], [(91, 372), (91, 379), (98, 379), (98, 372)], [(56, 365), (56, 379), (70, 379), (70, 365)], [(56, 379), (56, 393), (70, 393), (70, 379)], [(70, 379), (70, 393), (84, 393), (84, 379)], [(70, 372), (70, 379), (77, 379), (77, 372)], [(77, 372), (77, 379), (84, 379), (84, 372)], [(56, 337), (56, 351), (70, 351), (70, 337)], [(56, 351), (56, 365), (70, 365), (70, 351)], [(0, 225), (0, 281), (56, 281), (56, 225)], [(0, 281), (0, 337), (56, 337), (56, 281)], [(56, 225), (56, 253), (84, 253), (84, 225)], [(84, 225), (84, 253), (112, 253), (112, 225)], [(84, 253), (84, 267), (98, 267), (98, 253)], [(98, 267), (98, 281), (112, 281), (112, 267)], [(98, 253), (98, 267), (112, 267), (112, 253)], [(84, 267), (84, 274), (91, 274), (91, 267)], [(91, 274), (91, 281), (98, 281), (98, 274)], [(91, 267), (91, 274), (98, 274), (98, 267)], [(56, 253), (56, 267), (70, 267), (70, 253)], [(56, 267), (56, 281), (70, 281), (70, 267)], [(70, 253), (70, 267), (84, 267), (84, 253)], [(105, 281), (105, 288), (112, 288), (112, 281)], [(56, 309), (56, 323), (70, 323), (70, 309)], [(56, 323), (56, 337), (70, 337), (70, 323)], [(56, 281), (56, 295), (70, 295), (70, 281)], [(56, 295), (56, 309), (70, 309), (70, 295)], [(0, 112), (0, 225), (112, 225), (112, 112)], [(112, 0), (112, 56), (168, 56), (168, 0)], [(168, 0), (168, 56), (225, 56), (225, 0)], [(210, 56), (210, 63), (217, 63), (217, 56)], [(217, 56), (217, 63), (225, 63), (225, 56)], [(196, 56), (196, 63), (203, 63), (203, 56)], [(203, 56), (203, 63), (210, 63), (210, 56)], [(182, 56), (182, 63), (189, 63), (189, 56)], [(189, 56), (189, 63), (196, 63), (196, 56)], [(168, 56), (168, 63), (175, 63), (175, 56)], [(175, 56), (175, 63), (182, 63), (182, 56)], [(112, 56), (112, 84), (140, 84), (140, 56)], [(112, 84), (112, 112), (140, 112), (140, 84)], [(154, 56), (154, 63), (161, 63), (161, 56)], [(161, 56), (161, 63), (168, 63), (168, 56)], [(140, 56), (140, 63), (147, 63), (147, 56)], [(147, 56), (147, 63), (154, 63), (154, 56)], [(112, 168), (112, 196), (140, 196), (140, 168)], [(112, 196), (112, 225), (140, 225), (140, 196)], [(112, 112), (112, 140), (140, 140), (140, 112)], [(112, 140), (112, 168), (140, 168), (140, 140)], [(0, 56), (0, 112), (56, 112), (56, 56)], [(56, 56), (56, 112), (112, 112), (112, 56)], [(56, 0), (56, 56), (112, 56), (112, 0)], [(0, 28), (0, 56), (28, 56), (28, 28)], [(28, 28), (28, 56), (56, 56), (56, 28)], [(28, 0), (28, 28), (56, 28), (56, 0)], [(14, 0), (14, 7), (21, 7), (21, 0)], [(21, 0), (21, 7), (28, 7), (28, 0)], [(0, 14), (0, 21), (7, 21), (7, 14)], [(0, 21), (0, 28), (7, 28), (7, 21)], [(0, 0), (0, 7), (7, 7), (7, 0)], [(0, 7), (0, 14), (7, 14), (7, 7)], [(7, 0), (7, 7), (14, 7), (14, 0)]]
graph = graph_generation(empty_cells)
# print(graph)
print(time.time()-t)
    