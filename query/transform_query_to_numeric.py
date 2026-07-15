# Deklarasi jumlah node untuk setiap label (entitas Film/Movie)
movie_node_counts = {
    "action": 293467,
    "adult": 222819,
    "adventure": 273401,
    "animation": 330135,
    "biography": 76749,
    "comedy": 1479294,
    "crime": 312629,
    "documentary": 618520,
    "drama": 1984332,
    "family": 489281,
    "fantasy": 155302,
    "film_noir": 784,
    "game_show": 225632,
    "history": 95891,
    "horror": 130261,
    "music": 356267,
    "musical": 54325,
    "mystery": 149470,
    "news": 408975,
    "reality_tv": 338752,
    "romance": 644609,
    "sci_fi": 89121,
    "sport": 137057,
    "talk_show": 773293,
    "thriller": 124666,
    "war": 26911,
    "western": 26970
}

# Deklarasi jumlah node untuk setiap label (entitas Person)
person_node_counts = {
    "actor": 1263984,
    "actress": 767812,
    "animation_department": 27980,
    "art_department": 62619,
    "art_director": 27370,
    "assistant": 443,
    "assistant_director": 84613,
    "camera_department": 186421,
    "casting_department": 13843,
    "casting_director": 10628,
    "cinematographer": 284302,
    "composer": 248066,
    "costume_department": 14904,
    "costume_designer": 11048,
    "director": 560717,
    "editor": 257000,
    "editorial_department": 63380,
    "electrical_department": 2,
    "executive": 9007,
    "legal": 437,
    "location_management": 13050,
    "make_up_department": 18686,
    "manager": 3122,
    "miscellaneous": 228889,
    "music_department": 76607,
    "producer": 613186,
    "production_department": 1,
    "production_designer": 51274,
    "production_manager": 51119,
    "publicist": 581,
    "script_department": 21987,
    "set_decorator": 9893,
    "sound_department": 80900,
    "soundtrack": 99799,
    "special_effects": 11232,
    "stunts": 21182,
    "talent_agent": 2291,
    "transportation_department": 4459,
    "visual_effects": 36300,
    "writer": 683795
}

# Deklarasi jumlah relasi KELUAR (Outgoing) dari entitas Person
outgoing_rel_counts = {
    "actor": {
        "ACTED_IN": 11460681, "ARCHIVE_FOOTAGE_MAKER_OF": 88930, "ARCHIVE_SOUND_MAKER_OF": 1605, 
        "CINEMATOGRAPHER_OF": 112385, "COMPOSED": 168155, "DIRECTED": 749294, "EDITED": 72098, 
        "PRODUCED": 274473, "PRODUCTION_DESIGNER_OF": 13833, "WROTE": 878695
    },
    "actress": {
        "ACTED_IN": 8169427, "ARCHIVE_FOOTAGE_MAKER_OF": 60446, "ARCHIVE_SOUND_MAKER_OF": 360, 
        "CINEMATOGRAPHER_OF": 7394, "COMPOSED": 11426, "DIRECTED": 100076, "EDITED": 17236, 
        "PRODUCED": 109240, "PRODUCTION_DESIGNER_OF": 6100, "WROTE": 269132
    },
    "animation_department": {
        "ACTED_IN": 42345, "ARCHIVE_FOOTAGE_MAKER_OF": 344, "ARCHIVE_SOUND_MAKER_OF": 39, 
        "CINEMATOGRAPHER_OF": 6233, "COMPOSED": 3068, "DIRECTED": 147668, "EDITED": 12685, 
        "PRODUCED": 18025, "PRODUCTION_DESIGNER_OF": 3705, "WROTE": 52885
    },
    "art_department": {
        "ACTED_IN": 122054, "ARCHIVE_FOOTAGE_MAKER_OF": 1191, "ARCHIVE_SOUND_MAKER_OF": 32, 
        "CINEMATOGRAPHER_OF": 11407, "COMPOSED": 5877, "DIRECTED": 142373, "EDITED": 18001, 
        "PRODUCED": 30184, "PRODUCTION_DESIGNER_OF": 156063, "WROTE": 63679
    },
    "art_director": {
        "ACTED_IN": 26879, "ARCHIVE_FOOTAGE_MAKER_OF": 275, "ARCHIVE_SOUND_MAKER_OF": 5, 
        "CINEMATOGRAPHER_OF": 3930, "COMPOSED": 766, "DIRECTED": 28534, "EDITED": 1940, 
        "PRODUCED": 13206, "PRODUCTION_DESIGNER_OF": 131381, "WROTE": 21320
    },
    "assistant": {
        "ACTED_IN": 1244, "ARCHIVE_FOOTAGE_MAKER_OF": 5, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 39, "COMPOSED": 15, "DIRECTED": 150, "EDITED": 36, 
        "PRODUCED": 181, "PRODUCTION_DESIGNER_OF": 7, "WROTE": 121
    },
    "assistant_director": {
        "ACTED_IN": 201443, "ARCHIVE_FOOTAGE_MAKER_OF": 1251, "ARCHIVE_SOUND_MAKER_OF": 9, 
        "CINEMATOGRAPHER_OF": 36133, "COMPOSED": 4361, "DIRECTED": 752330, "EDITED": 41134, 
        "PRODUCED": 127485, "PRODUCTION_DESIGNER_OF": 4115, "WROTE": 135658
    },
    "camera_department": {
        "ACTED_IN": 261744, "ARCHIVE_FOOTAGE_MAKER_OF": 4528, "ARCHIVE_SOUND_MAKER_OF": 22, 
        "CINEMATOGRAPHER_OF": 910837, "COMPOSED": 8254, "DIRECTED": 248283, "EDITED": 100132, 
        "PRODUCED": 97848, "PRODUCTION_DESIGNER_OF": 5897, "WROTE": 50819
    },
    "casting_department": {
        "ACTED_IN": 71426, "ARCHIVE_FOOTAGE_MAKER_OF": 318, "ARCHIVE_SOUND_MAKER_OF": 7, 
        "CINEMATOGRAPHER_OF": 840, "COMPOSED": 404, "DIRECTED": 11007, "EDITED": 2859, 
        "PRODUCED": 34346, "PRODUCTION_DESIGNER_OF": 440, "WROTE": 8779
    },
    "casting_director": {
        "ACTED_IN": 80137, "ARCHIVE_FOOTAGE_MAKER_OF": 372, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 439, "COMPOSED": 209, "DIRECTED": 20845, "EDITED": 1418, 
        "PRODUCED": 23864, "PRODUCTION_DESIGNER_OF": 250, "WROTE": 12149
    },
    "cinematographer": {
        "ACTED_IN": 137324, "ARCHIVE_FOOTAGE_MAKER_OF": 1444, "ARCHIVE_SOUND_MAKER_OF": 11, 
        "CINEMATOGRAPHER_OF": 1367616, "COMPOSED": 6642, "DIRECTED": 352706, "EDITED": 51109, 
        "PRODUCED": 79830, "PRODUCTION_DESIGNER_OF": 2074, "WROTE": 44313
    },
    "composer": {
        "ACTED_IN": 477897, "ARCHIVE_FOOTAGE_MAKER_OF": 10834, "ARCHIVE_SOUND_MAKER_OF": 69, 
        "CINEMATOGRAPHER_OF": 4279, "COMPOSED": 1413197, "DIRECTED": 27430, "EDITED": 8500, 
        "PRODUCED": 16353, "PRODUCTION_DESIGNER_OF": 409, "WROTE": 45299
    },
    "costume_department": {
        "ACTED_IN": 60019, "ARCHIVE_FOOTAGE_MAKER_OF": 650, "ARCHIVE_SOUND_MAKER_OF": 18, 
        "CINEMATOGRAPHER_OF": 628, "COMPOSED": 277, "DIRECTED": 3703, "EDITED": 1382, 
        "PRODUCED": 6099, "PRODUCTION_DESIGNER_OF": 6829, "WROTE": 8415
    },
    "costume_designer": {
        "ACTED_IN": 36504, "ARCHIVE_FOOTAGE_MAKER_OF": 246, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 351, "COMPOSED": 203, "DIRECTED": 4283, "EDITED": 431, 
        "PRODUCED": 3052, "PRODUCTION_DESIGNER_OF": 15531, "WROTE": 3793
    },
    "director": {
        "ACTED_IN": 2315792, "ARCHIVE_FOOTAGE_MAKER_OF": 27118, "ARCHIVE_SOUND_MAKER_OF": 205, 
        "CINEMATOGRAPHER_OF": 267819, "COMPOSED": 21866, "DIRECTED": 4398352, "EDITED": 175106, 
        "PRODUCED": 562157, "PRODUCTION_DESIGNER_OF": 11864, "WROTE": 883586
    },
    "editor": {
        "ACTED_IN": 229937, "ARCHIVE_FOOTAGE_MAKER_OF": 1428, "ARCHIVE_SOUND_MAKER_OF": 29, 
        "CINEMATOGRAPHER_OF": 114850, "COMPOSED": 15178, "DIRECTED": 449208, "EDITED": 1326183, 
        "PRODUCED": 106401, "PRODUCTION_DESIGNER_OF": 1874, "WROTE": 101144
    },
    "editorial_department": {
        "ACTED_IN": 62326, "ARCHIVE_FOOTAGE_MAKER_OF": 472, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 42337, "COMPOSED": 4202, "DIRECTED": 76548, "EDITED": 682261, 
        "PRODUCED": 59430, "PRODUCTION_DESIGNER_OF": 902, "WROTE": 37219
    },
    "electrical_department": {
        "ACTED_IN": 83, "ARCHIVE_FOOTAGE_MAKER_OF": 0, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 0, "COMPOSED": 0, "DIRECTED": 0, "EDITED": 1, 
        "PRODUCED": 0, "PRODUCTION_DESIGNER_OF": 0, "WROTE": 0
    },
    "executive": {
        "ACTED_IN": 46081, "ARCHIVE_FOOTAGE_MAKER_OF": 1293, "ARCHIVE_SOUND_MAKER_OF": 16, 
        "CINEMATOGRAPHER_OF": 757, "COMPOSED": 498, "DIRECTED": 3068, "EDITED": 563, 
        "PRODUCED": 54632, "PRODUCTION_DESIGNER_OF": 133, "WROTE": 14571
    },
    "legal": {
        "ACTED_IN": 2007, "ARCHIVE_FOOTAGE_MAKER_OF": 49, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 6, "COMPOSED": 10, "DIRECTED": 2593, "EDITED": 5, 
        "PRODUCED": 507, "PRODUCTION_DESIGNER_OF": 0, "WROTE": 631
    },
    "location_management": {
        "ACTED_IN": 26248, "ARCHIVE_FOOTAGE_MAKER_OF": 112, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 3081, "COMPOSED": 602, "DIRECTED": 22452, "EDITED": 1620, 
        "PRODUCED": 28478, "PRODUCTION_DESIGNER_OF": 1703, "WROTE": 9631
    },
    "make_up_department": {
        "ACTED_IN": 77505, "ARCHIVE_FOOTAGE_MAKER_OF": 1038, "ARCHIVE_SOUND_MAKER_OF": 3, 
        "CINEMATOGRAPHER_OF": 1213, "COMPOSED": 1474, "DIRECTED": 5202, "EDITED": 1270, 
        "PRODUCED": 5213, "PRODUCTION_DESIGNER_OF": 2719, "WROTE": 4238
    },
    "manager": {
        "ACTED_IN": 11227, "ARCHIVE_FOOTAGE_MAKER_OF": 83, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 238, "COMPOSED": 445, "DIRECTED": 788, "EDITED": 199, 
        "PRODUCED": 11321, "PRODUCTION_DESIGNER_OF": 62, "WROTE": 2710
    },
    "miscellaneous": {
        "ACTED_IN": 1338470, "ARCHIVE_FOOTAGE_MAKER_OF": 15642, "ARCHIVE_SOUND_MAKER_OF": 310, 
        "CINEMATOGRAPHER_OF": 90087, "COMPOSED": 21122, "DIRECTED": 491294, "EDITED": 117573, 
        "PRODUCED": 609647, "PRODUCTION_DESIGNER_OF": 17759, "WROTE": 1204892
    },
    "music_department": {
        "ACTED_IN": 608627, "ARCHIVE_FOOTAGE_MAKER_OF": 9186, "ARCHIVE_SOUND_MAKER_OF": 189, 
        "CINEMATOGRAPHER_OF": 2511, "COMPOSED": 955171, "DIRECTED": 18409, "EDITED": 15018, 
        "PRODUCED": 23633, "PRODUCTION_DESIGNER_OF": 175, "WROTE": 115410
    },
    "producer": {
        "ACTED_IN": 3852407, "ARCHIVE_FOOTAGE_MAKER_OF": 42086, "ARCHIVE_SOUND_MAKER_OF": 544, 
        "CINEMATOGRAPHER_OF": 179006, "COMPOSED": 57855, "DIRECTED": 1743713, "EDITED": 210501, 
        "PRODUCED": 2464941, "PRODUCTION_DESIGNER_OF": 25152, "WROTE": 2014325
    },
    "production_department": {
        "ACTED_IN": 0, "ARCHIVE_FOOTAGE_MAKER_OF": 0, "ARCHIVE_SOUND_MAKER_OF": 6, 
        "CINEMATOGRAPHER_OF": 0, "COMPOSED": 0, "DIRECTED": 0, "EDITED": 0, 
        "PRODUCED": 1, "PRODUCTION_DESIGNER_OF": 276145, "WROTE": 0
    },
    "production_designer": {
        "ACTED_IN": 26731, "ARCHIVE_FOOTAGE_MAKER_OF": 181, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 2728, "COMPOSED": 726, "DIRECTED": 21996, "EDITED": 1633, 
        "PRODUCED": 17017, "PRODUCTION_DESIGNER_OF": 0, "WROTE": 15902
    },
    "production_manager": {
        "ACTED_IN": 74967, "ARCHIVE_FOOTAGE_MAKER_OF": 1052, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 7553, "COMPOSED": 1996, "DIRECTED": 87105, "EDITED": 30298, 
        "PRODUCED": 338896, "PRODUCTION_DESIGNER_OF": 3106, "WROTE": 64513
    },
    "publicist": {
        "ACTED_IN": 2679, "ARCHIVE_FOOTAGE_MAKER_OF": 105, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 9, "COMPOSED": 36, "DIRECTED": 162, "EDITED": 25, 
        "PRODUCED": 773, "PRODUCTION_DESIGNER_OF": 11, "WROTE": 224
    },
    "script_department": {
        "ACTED_IN": 63521, "ARCHIVE_FOOTAGE_MAKER_OF": 452, "ARCHIVE_SOUND_MAKER_OF": 11, 
        "CINEMATOGRAPHER_OF": 1835, "COMPOSED": 1027, "DIRECTED": 48371, "EDITED": 11327, 
        "PRODUCED": 46905, "PRODUCTION_DESIGNER_OF": 546, "WROTE": 355616
    },
    "set_decorator": {
        "ACTED_IN": 13091, "ARCHIVE_FOOTAGE_MAKER_OF": 55, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 955, "COMPOSED": 311, "DIRECTED": 6767, "EDITED": 711, 
        "PRODUCED": 2587, "PRODUCTION_DESIGNER_OF": 36206, "WROTE": 1550
    },
    "sound_department": {
        "ACTED_IN": 184110, "ARCHIVE_FOOTAGE_MAKER_OF": 509, "ARCHIVE_SOUND_MAKER_OF": 66, 
        "CINEMATOGRAPHER_OF": 37334, "COMPOSED": 159926, "DIRECTED": 52031, "EDITED": 107218, 
        "PRODUCED": 35229, "PRODUCTION_DESIGNER_OF": 1952, "WROTE": 22699
    },
    "soundtrack": {
        "ACTED_IN": 3260775, "ARCHIVE_FOOTAGE_MAKER_OF": 52102, "ARCHIVE_SOUND_MAKER_OF": 726, 
        "CINEMATOGRAPHER_OF": 1116, "COMPOSED": 628532, "DIRECTED": 24857, "EDITED": 1756, 
        "PRODUCED": 17336, "PRODUCTION_DESIGNER_OF": 106, "WROTE": 142990
    },
    "special_effects": {
        "ACTED_IN": 30578, "ARCHIVE_FOOTAGE_MAKER_OF": 189, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 11683, "COMPOSED": 1086, "DIRECTED": 6461, "EDITED": 7784, 
        "PRODUCED": 3026, "PRODUCTION_DESIGNER_OF": 3752, "WROTE": 2383
    },
    "stunts": {
        "ACTED_IN": 172580, "ARCHIVE_FOOTAGE_MAKER_OF": 1333, "ARCHIVE_SOUND_MAKER_OF": 14, 
        "CINEMATOGRAPHER_OF": 1388, "COMPOSED": 339, "DIRECTED": 8071, "EDITED": 545, 
        "PRODUCED": 9604, "PRODUCTION_DESIGNER_OF": 135, "WROTE": 2961
    },
    "talent_agent": {
        "ACTED_IN": 17490, "ARCHIVE_FOOTAGE_MAKER_OF": 187, "ARCHIVE_SOUND_MAKER_OF": 5, 
        "CINEMATOGRAPHER_OF": 154, "COMPOSED": 200, "DIRECTED": 481, "EDITED": 4531, 
        "PRODUCED": 5823, "PRODUCTION_DESIGNER_OF": 18, "WROTE": 906
    },
    "transportation_department": {
        "ACTED_IN": 13190, "ARCHIVE_FOOTAGE_MAKER_OF": 154, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 1467, "COMPOSED": 367, "DIRECTED": 870, "EDITED": 809, 
        "PRODUCED": 3125, "PRODUCTION_DESIGNER_OF": 473, "WROTE": 1223
    },
    "visual_effects": {
        "ACTED_IN": 40185, "ARCHIVE_FOOTAGE_MAKER_OF": 270, "ARCHIVE_SOUND_MAKER_OF": 6, 
        "CINEMATOGRAPHER_OF": 29654, "COMPOSED": 3212, "DIRECTED": 43382, "EDITED": 67190, 
        "PRODUCED": 18737, "PRODUCTION_DESIGNER_OF": 5920, "WROTE": 12263
    },
    "writer": {
        "ACTED_IN": 3960419, "ARCHIVE_FOOTAGE_MAKER_OF": 38793, "ARCHIVE_SOUND_MAKER_OF": 634, 
        "CINEMATOGRAPHER_OF": 78420, "COMPOSED": 31832, "DIRECTED": 1853560, "EDITED": 99018, 
        "PRODUCED": 607136, "PRODUCTION_DESIGNER_OF": 8472, "WROTE": 5319043
    }
}

# Deklarasi jumlah relasi MASUK (Incoming) ke entitas Film/Movie
incoming_rel_counts = {
    "action": {
        "ACTED_IN": 1230882, "ARCHIVE_FOOTAGE_MAKER_OF": 4785, "ARCHIVE_SOUND_MAKER_OF": 488, 
        "CINEMATOGRAPHER_OF": 66783, "COMPOSED": 115827, "DIRECTED": 271042, "EDITED": 50525, 
        "PRODUCED": 152468, "PRODUCTION_DESIGNER_OF": 10270, "WROTE": 426348
    },
    "adult": {
        "ACTED_IN": 783767, "ARCHIVE_FOOTAGE_MAKER_OF": 43237, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 9538, "COMPOSED": 5641, "DIRECTED": 73531, "EDITED": 14117, 
        "PRODUCED": 11023, "PRODUCTION_DESIGNER_OF": 431, "WROTE": 8735
    },
    "adventure": {
        "ACTED_IN": 1056053, "ARCHIVE_FOOTAGE_MAKER_OF": 3497, "ARCHIVE_SOUND_MAKER_OF": 373, 
        "CINEMATOGRAPHER_OF": 60371, "COMPOSED": 104922, "DIRECTED": 249591, "EDITED": 55016, 
        "PRODUCED": 127305, "PRODUCTION_DESIGNER_OF": 10913, "WROTE": 398140
    },
    "animation": {
        "ACTED_IN": 1017184, "ARCHIVE_FOOTAGE_MAKER_OF": 1866, "ARCHIVE_SOUND_MAKER_OF": 790, 
        "CINEMATOGRAPHER_OF": 27525, "COMPOSED": 131642, "DIRECTED": 304392, "EDITED": 55299, 
        "PRODUCED": 132947, "PRODUCTION_DESIGNER_OF": 6086, "WROTE": 395706
    },
    "biography": {
        "ACTED_IN": 187118, "ARCHIVE_FOOTAGE_MAKER_OF": 8731, "ARCHIVE_SOUND_MAKER_OF": 26, 
        "CINEMATOGRAPHER_OF": 24552, "COMPOSED": 21975, "DIRECTED": 59948, "EDITED": 21419, 
        "PRODUCED": 32828, "PRODUCTION_DESIGNER_OF": 2663, "WROTE": 41963
    },
    "comedy": {
        "ACTED_IN": 5776115, "ARCHIVE_FOOTAGE_MAKER_OF": 23252, "ARCHIVE_SOUND_MAKER_OF": 691, 
        "CINEMATOGRAPHER_OF": 312480, "COMPOSED": 334011, "DIRECTED": 1126831, "EDITED": 274400, 
        "PRODUCED": 583231, "PRODUCTION_DESIGNER_OF": 88423, "WROTE": 1668482
    },
    "crime": {
        "ACTED_IN": 1264641, "ARCHIVE_FOOTAGE_MAKER_OF": 1773, "ARCHIVE_SOUND_MAKER_OF": 18, 
        "CINEMATOGRAPHER_OF": 91877, "COMPOSED": 109847, "DIRECTED": 294318, "EDITED": 69317, 
        "PRODUCED": 187252, "PRODUCTION_DESIGNER_OF": 20048, "WROTE": 491454
    },
    "documentary": {
        "ACTED_IN": 827125, "ARCHIVE_FOOTAGE_MAKER_OF": 45518, "ARCHIVE_SOUND_MAKER_OF": 243, 
        "CINEMATOGRAPHER_OF": 232968, "COMPOSED": 152376, "DIRECTED": 435655, "EDITED": 239358, 
        "PRODUCED": 243383, "PRODUCTION_DESIGNER_OF": 7200, "WROTE": 151441
    },
    "drama": {
        "ACTED_IN": 8160487, "ARCHIVE_FOOTAGE_MAKER_OF": 5524, "ARCHIVE_SOUND_MAKER_OF": 27, 
        "CINEMATOGRAPHER_OF": 581332, "COMPOSED": 531594, "DIRECTED": 2082743, "EDITED": 390703, 
        "PRODUCED": 996207, "PRODUCTION_DESIGNER_OF": 137329, "WROTE": 2854122
    },
    "family": {
        "ACTED_IN": 1745818, "ARCHIVE_FOOTAGE_MAKER_OF": 4386, "ARCHIVE_SOUND_MAKER_OF": 252, 
        "CINEMATOGRAPHER_OF": 94191, "COMPOSED": 134427, "DIRECTED": 397648, "EDITED": 108511, 
        "PRODUCED": 217841, "PRODUCTION_DESIGNER_OF": 26433, "WROTE": 512868
    },
    "fantasy": {
        "ACTED_IN": 559487, "ARCHIVE_FOOTAGE_MAKER_OF": 1082, "ARCHIVE_SOUND_MAKER_OF": 88, 
        "CINEMATOGRAPHER_OF": 40087, "COMPOSED": 54850, "DIRECTED": 144474, "EDITED": 27473, 
        "PRODUCED": 72054, "PRODUCTION_DESIGNER_OF": 10072, "WROTE": 189413
    },
    "film_noir": {
        "ACTED_IN": 3212, "ARCHIVE_FOOTAGE_MAKER_OF": 0, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 548, "COMPOSED": 524, "DIRECTED": 785, "EDITED": 289, 
        "PRODUCED": 537, "PRODUCTION_DESIGNER_OF": 9, "WROTE": 1839
    },
    "game_show": {
        "ACTED_IN": 763616, "ARCHIVE_FOOTAGE_MAKER_OF": 2568, "ARCHIVE_SOUND_MAKER_OF": 22, 
        "CINEMATOGRAPHER_OF": 6921, "COMPOSED": 36456, "DIRECTED": 92006, "EDITED": 53798, 
        "PRODUCED": 83862, "PRODUCTION_DESIGNER_OF": 15475, "WROTE": 81622
    },
    "history": {
        "ACTED_IN": 273944, "ARCHIVE_FOOTAGE_MAKER_OF": 6802, "ARCHIVE_SOUND_MAKER_OF": 192, 
        "CINEMATOGRAPHER_OF": 32258, "COMPOSED": 30959, "DIRECTED": 75873, "EDITED": 27832, 
        "PRODUCED": 39707, "PRODUCTION_DESIGNER_OF": 4932, "WROTE": 71522
    },
    "horror": {
        "ACTED_IN": 440395, "ARCHIVE_FOOTAGE_MAKER_OF": 1421, "ARCHIVE_SOUND_MAKER_OF": 51, 
        "CINEMATOGRAPHER_OF": 49089, "COMPOSED": 48903, "DIRECTED": 104942, "EDITED": 24745, 
        "PRODUCED": 65930, "PRODUCTION_DESIGNER_OF": 9056, "WROTE": 96393
    },
    "music": {
        "ACTED_IN": 1199835, "ARCHIVE_FOOTAGE_MAKER_OF": 17184, "ARCHIVE_SOUND_MAKER_OF": 96, 
        "CINEMATOGRAPHER_OF": 54276, "COMPOSED": 64896, "DIRECTED": 219984, "EDITED": 61038, 
        "PRODUCED": 97101, "PRODUCTION_DESIGNER_OF": 16573, "WROTE": 191400
    },
    "musical": {
        "ACTED_IN": 195107, "ARCHIVE_FOOTAGE_MAKER_OF": 1090, "ARCHIVE_SOUND_MAKER_OF": 29, 
        "CINEMATOGRAPHER_OF": 14317, "COMPOSED": 16231, "DIRECTED": 50900, "EDITED": 10490, 
        "PRODUCED": 25287, "PRODUCTION_DESIGNER_OF": 3205, "WROTE": 51533
    },
    "mystery": {
        "ACTED_IN": 589673, "ARCHIVE_FOOTAGE_MAKER_OF": 936, "ARCHIVE_SOUND_MAKER_OF": 22, 
        "CINEMATOGRAPHER_OF": 42557, "COMPOSED": 55619, "DIRECTED": 137654, "EDITED": 25934, 
        "PRODUCED": 85544, "PRODUCTION_DESIGNER_OF": 7792, "WROTE": 210391
    },
    "news": {
        "ACTED_IN": 859718, "ARCHIVE_FOOTAGE_MAKER_OF": 31387, "ARCHIVE_SOUND_MAKER_OF": 368, 
        "CINEMATOGRAPHER_OF": 13630, "COMPOSED": 63605, "DIRECTED": 75972, "EDITED": 60097, 
        "PRODUCED": 97180, "PRODUCTION_DESIGNER_OF": 3682, "WROTE": 105562
    },
    "reality_tv": {
        "ACTED_IN": 731951, "ARCHIVE_FOOTAGE_MAKER_OF": 2854, "ARCHIVE_SOUND_MAKER_OF": 11, 
        "CINEMATOGRAPHER_OF": 68900, "COMPOSED": 83171, "DIRECTED": 146031, "EDITED": 183762, 
        "PRODUCED": 158576, "PRODUCTION_DESIGNER_OF": 10540, "WROTE": 98896
    },
    "romance": {
        "ACTED_IN": 2907409, "ARCHIVE_FOOTAGE_MAKER_OF": 1524, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 118989, "COMPOSED": 127344, "DIRECTED": 759546, "EDITED": 92229, 
        "PRODUCED": 284671, "PRODUCTION_DESIGNER_OF": 37873, "WROTE": 1160519
    },
    "sci_fi": {
        "ACTED_IN": 325339, "ARCHIVE_FOOTAGE_MAKER_OF": 1483, "ARCHIVE_SOUND_MAKER_OF": 221, 
        "CINEMATOGRAPHER_OF": 27678, "COMPOSED": 34105, "DIRECTED": 70932, "EDITED": 17905, 
        "PRODUCED": 44965, "PRODUCTION_DESIGNER_OF": 6726, "WROTE": 81271
    },
    "sport": {
        "ACTED_IN": 371509, "ARCHIVE_FOOTAGE_MAKER_OF": 10718, "ARCHIVE_SOUND_MAKER_OF": 291, 
        "CINEMATOGRAPHER_OF": 17335, "COMPOSED": 16167, "DIRECTED": 43658, "EDITED": 28227, 
        "PRODUCED": 40037, "PRODUCTION_DESIGNER_OF": 2332, "WROTE": 46891
    },
    "talk_show": {
        "ACTED_IN": 1979368, "ARCHIVE_FOOTAGE_MAKER_OF": 28929, "ARCHIVE_SOUND_MAKER_OF": 396, 
        "CINEMATOGRAPHER_OF": 21735, "COMPOSED": 49909, "DIRECTED": 161568, "EDITED": 98220, 
        "PRODUCED": 148124, "PRODUCTION_DESIGNER_OF": 11796, "WROTE": 261408
    },
    "thriller": {
        "ACTED_IN": 472757, "ARCHIVE_FOOTAGE_MAKER_OF": 296, "ARCHIVE_SOUND_MAKER_OF": 5, 
        "CINEMATOGRAPHER_OF": 50177, "COMPOSED": 51880, "DIRECTED": 121988, "EDITED": 29195, 
        "PRODUCED": 79100, "PRODUCTION_DESIGNER_OF": 9267, "WROTE": 136357
    },
    "war": {
        "ACTED_IN": 95675, "ARCHIVE_FOOTAGE_MAKER_OF": 952, "ARCHIVE_SOUND_MAKER_OF": 33, 
        "CINEMATOGRAPHER_OF": 12134, "COMPOSED": 11245, "DIRECTED": 24055, "EDITED": 8408, 
        "PRODUCED": 12472, "PRODUCTION_DESIGNER_OF": 2513, "WROTE": 29409
    },
    "western": {
        "ACTED_IN": 112634, "ARCHIVE_FOOTAGE_MAKER_OF": 680, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 14239, "COMPOSED": 9330, "DIRECTED": 23891, "EDITED": 9135, 
        "PRODUCED": 15302, "PRODUCTION_DESIGNER_OF": 635, "WROTE": 36782
    }
}

# Deklarasi jumlah value untuk properti 'category'
category_prop_counts = {
    "tvEpisode": 4587657,
    "short": 639766,
    "movie": 492210,
    "video": 265757,
    "tvSeries": 162227,
    "tvMovie": 116975,
    "tvMiniSeries": 28085,
    "tvSpecial": 26082,
    "videoGame": 15693,
    "tvShort": 7633,
    "audiobook": 1,
    "radioSeries": 1,
    "episode": 1
}

# Deklarasi jumlah value untuk properti 'year'
year_prop_counts = {
    "0": 624693,
    "2017": 326849,
    "2016": 315054,
    "2018": 309713,
    "2015": 301687,
    "2019": 293391,
    "2014": 286661,
    "2013": 274407,
    "2012": 256827,
    "2020": 240885,
    "2011": 230219,
    "2010": 201811,
    "2009": 178162,
    "2008": 166310,
    "2007": 154677,
    "2006": 139569,
    "2005": 124040,
    "2004": 110667,
    "2003": 96314,
    "2002": 82362,
    "2001": 78922,
    "2000": 70977,
    "1999": 68290,
    "1998": 64196,
    "1997": 57892,
    "1996": 54464,
    "2021": 53493,
    "1995": 52210,
    "1994": 46553,
    "1993": 41693,
    "1992": 39291,
    "1991": 38592,
    "1990": 36334,
    "1989": 34805,
    "1988": 32144,
    "1987": 31942,
    "1985": 29538,
    "1986": 29350,
    "1984": 27142,
    "1983": 25930,
    "1982": 25526,
    "1980": 24492,
    "1981": 24159,
    "1973": 23934,
    "1974": 23132,
    "1975": 23033,
    "1976": 22926,
    "1972": 22670,
    "1977": 22499,
    "1979": 22438,
    "1971": 22384,
    "1978": 22332,
    "1969": 21786,
    "1970": 21686,
    "1967": 20162,
    "1966": 19977,
    "1968": 19427,
    "1965": 18807,
    "1964": 16568,
    "1963": 15451,
    "1961": 14725,
    "1960": 14415,
    "1959": 13601,
    "1962": 13589,
    "1958": 13055,
    "1957": 12315,
    "1955": 11240,
    "1956": 11098,
    "1954": 10378,
    "1953": 8097,
    "1952": 7484,
    "1951": 7321,
    "1914": 6669,
    "1913": 6658,
    "1915": 6538,
    "1950": 5763,
    "1912": 5482,
    "1916": 5105,
    "1911": 4275,
    "1949": 4198,
    "1917": 4015,
    "1918": 3220,
    "1910": 3112,
    "1948": 2970,
    "1920": 2873,
    "1937": 2809,
    "1929": 2800,
    "1938": 2750,
    "1919": 2742,
    "1927": 2671,
    "1928": 2648,
    "1926": 2621,
    "1936": 2599,
    "1921": 2504,
    "1931": 2459,
    "1947": 2452,
    "1939": 2428,
    "1930": 2402,
    "1932": 2314,
    "1925": 2309,
    "1935": 2304,
    "1934": 2301,
    "1922": 2246,
    "1933": 2238,
    "1946": 2093,
    "1940": 2056,
    "1941": 2043,
    "1924": 2009,
    "1942": 1976,
    "1909": 1969,
    "1923": 1938,
    "2022": 1869,
    "1903": 1840,
    "1943": 1770,
    "1945": 1636,
    "1944": 1601,
    "1908": 1549,
    "1900": 1159,
    "1901": 1120,
    "1907": 1088,
    "1899": 1011,
    "1904": 992,
    "1906": 940,
    "1898": 916,
    "1902": 829,
    "1905": 799,
    "1897": 697,
    "1896": 568,
    "2023": 161,
    "1895": 70,
    "1894": 46,
    "2024": 41,
    "1887": 15,
    "1892": 8,
    "2025": 8,
    "2027": 5,
    "1891": 4,
    "1888": 4,
    "2026": 4,
    "1893": 3,
    "2028": 3,
    "1890": 2,
    "1878": 2,
    "1889": 1,
    "1874": 1,
    "2115": 1,
    "1883": 1,
    "1881": 1,
    "1885": 1
}

# Deklarasi jumlah value untuk properti 'birth'
birth_prop_counts = {
    "0": 3209521, "1980": 6439, "1978": 6358, "1979": 6302, "1981": 6195,
    "1982": 6192, "1977": 5926, "1976": 5852, "1984": 5756, "1975": 5722,
    "1974": 5717, "1983": 5646, "1970": 5587, "1972": 5544, "1971": 5481,
    "1985": 5397, "1973": 5376, "1986": 5234, "1969": 5132, "1968": 4830,
    "1987": 4682, "1965": 4572, "1964": 4565, "1967": 4525, "1966": 4463,
    "1988": 4415, "1963": 4325, "1962": 4281, "1961": 4123, "1947": 4050,
    "1989": 3956, "1960": 3885, "1946": 3769, "1958": 3765, "1959": 3745,
    "1948": 3725, "1990": 3686, "1957": 3677, "1944": 3604, "1943": 3569,
    "1949": 3537, "1950": 3529, "1955": 3508, "1952": 3470, "1953": 3388,
    "1956": 3387, "1942": 3382, "1951": 3373, "1945": 3373, "1954": 3354,
    "1941": 3263, "1940": 3262, "1930": 3211, "1991": 3196, "1938": 3168,
    "1939": 3148, "1929": 3126, "1928": 3111, "1937": 3043, "1931": 3030,
    "1927": 3021, "1992": 3006, "1926": 2940, "1936": 2922, "1932": 2916,
    "1934": 2896, "1925": 2890, "1924": 2829, "1935": 2828, "1933": 2754,
    "1923": 2688, "1993": 2619, "1922": 2598, "1921": 2594, "1920": 2576,
    "1994": 2280, "1995": 2055, "1914": 1978, "1919": 1962, "1918": 1941,
    "1912": 1856, "1913": 1809, "1915": 1801, "1916": 1798, "1910": 1782,
    "1908": 1780, "1911": 1754, "1917": 1752, "1909": 1742, "1996": 1739,
    "1907": 1701, "1904": 1625, "1906": 1602, "1997": 1574, "1905": 1540,
    "1903": 1514, "1901": 1458, "1902": 1426, "1900": 1321, "1899": 1293,
    "1898": 1282, "1998": 1259, "1896": 1166, "1897": 1128, "1892": 1113,
    "1893": 1105, "1895": 1104, "1894": 1073, "1889": 1022, "1888": 1021,
    "1891": 1012, "1890": 1010, "1999": 900, "1887": 886, "1886": 861,
    "1885": 840, "1884": 801, "1883": 707, "1882": 705, "2000": 674,
    "1880": 648, "1881": 629, "1879": 611, "1878": 572, "2001": 554,
    "1876": 501, "1877": 489, "1875": 479, "1874": 458, "1873": 401,
    "2002": 393, "1872": 390, "1870": 371, "1871": 343, "1869": 326,
    "2003": 320, "1867": 286, "1866": 269, "1868": 268, "1865": 252,
    "2004": 246, "1863": 235, "1864": 212, "1862": 212, "2005": 196,
    "1860": 194, "1861": 166, "1858": 150, "1859": 149, "2006": 138,
    "2007": 132, "1857": 131, "2008": 98, "1854": 97, "1856": 93,
    "1855": 92, "1853": 91, "2009": 77, "1852": 76, "1851": 74,
    "1850": 68, "1848": 61, "2010": 61, "1849": 51, "1846": 47,
    "1847": 45, "1842": 42, "2011": 39, "1844": 35, "2012": 32,
    "1845": 28, "1839": 26, "1841": 26, "1838": 22, "1843": 22,
    "1836": 22, "1840": 21, "1821": 20, "1837": 20, "1830": 20,
    "1835": 18, "1834": 18, "1828": 17, "1810": 16, "1813": 15,
    "1811": 15, "1819": 15, "1829": 15, "1831": 15, "2014": 15,
    "2013": 15, "1804": 14, "1832": 14, "1822": 14, "1809": 13,
    "1824": 13, "1825": 13, "1812": 12, "1833": 12, "1820": 11,
    "1797": 11, "1823": 11, "1803": 10, "1827": 10, "1817": 10,
    "1814": 10, "1826": 9, "1808": 9, "1801": 9, "1791": 9,
    "1818": 8, "1806": 8, "1802": 8, "1815": 8, "1816": 7,
    "1792": 7, "1799": 7, "1805": 7, "1807": 6, "2016": 6,
    "1798": 6, "1775": 5, "1685": 5, "1770": 5, "1749": 5,
    "1782": 5, "1788": 5, "1793": 5, "1790": 5, "1795": 5,
    "1786": 5, "1766": 4, "1784": 4, "1737": 4, "1796": 4,
    "1759": 4, "1789": 4, "1772": 4, "1777": 4, "1785": 4,
    "1767": 4, "1725": 4, "1774": 4, "1751": 4, "1755": 4,
    "2015": 4, "1776": 3, "1707": 3, "1778": 3, "1711": 3,
    "1567": 3, "1732": 3, "1740": 3, "1761": 3, "1720": 3,
    "1741": 3, "1783": 3, "1768": 3, "1779": 3, "1580": 3,
    "1585": 3, "1735": 3, "1550": 3, "1731": 3, "1758": 3,
    "1746": 3, "1564": 2, "1547": 2, "1773": 2, "1698": 2,
    "1572": 2, "1756": 2, "1712": 2, "1747": 2, "1678": 2,
    "1579": 2, "1710": 2, "1510": 2, "1714": 2, "1757": 2,
    "1764": 2, "1671": 2, "1688": 2, "1584": 2, "1640": 2,
    "1653": 2, "1668": 2, "1713": 2, "1717": 2, "1622": 2,
    "1697": 2, "1440": 2, "1780": 2, "1674": 2, "1639": 2,
    "1628": 2, "1781": 2, "1734": 2, "1641": 2, "1743": 2,
    "1652": 2, "2017": 2, "1754": 2, "1670": 2, "1619": 2,
    "1494": 2, "1583": 2, "1724": 2, "1769": 2, "1492": 2,
    "1568": 2, "1474": 1, "1542": 1, "1343": 1, "1180": 1,
    "1563": 1, "1508": 1, "1493": 1, "1543": 1, "1586": 1,
    "1283": 1, "1600": 1, "1621": 1, "1503": 1, "1313": 1,
    "1715": 1, "1265": 1, "1468": 1, "1660": 1, "1606": 1,
    "1763": 1, "1530": 1, "1748": 1, "1560": 1, "1730": 1,
    "1561": 1, "1150": 1, "1716": 1, "1504": 1, "1787": 1,
    "1634": 1, "1684": 1, "1529": 1, "59": 1, "1629": 1,
    "1562": 1, "1485": 1, "1330": 1, "1700": 1, "1745": 1,
    "1469": 1, "1760": 1, "1729": 1, "1618": 1, "37": 1,
    "1414": 1, "1693": 1, "1656": 1, "973": 1, "1686": 1,
    "1608": 1, "1739": 1, "1771": 1, "1465": 1, "4": 1,
    "1659": 1, "1635": 1, "1207": 1, "1664": 1, "1431": 1,
    "1398": 1, "1694": 1, "1726": 1, "1667": 1, "1727": 1,
    "1689": 1, "1130": 1, "1544": 1, "1578": 1, "1681": 1,
    "1549": 1, "1589": 1, "1532": 1, "1677": 1, "1506": 1,
    "1412": 1, "1587": 1, "1706": 1, "2019": 1, "1728": 1,
    "1733": 1, "2020": 1, "163": 1, "95": 1, "46": 1,
    "69": 1, "1765": 1, "1098": 1, "1593": 1, "1569": 1,
    "770": 1, "1505": 1, "1291": 1, "1452": 1, "1644": 1,
    "1413": 1, "1658": 1, "1794": 1, "1525": 1, "1566": 1,
    "1750": 1, "1646": 1, "1654": 1, "1636": 1, "1633": 1,
    "1657": 1, "1420": 1, "1581": 1, "1335": 1, "1558": 1,
    "1524": 1, "1577": 1, "1533": 1, "1067": 1, "1571": 1,
    "1475": 1, "1422": 1, "1604": 1, "1616": 1, "1645": 1,
    "1626": 1, "6": 1, "1511": 1, "1095": 1, "1599": 1,
    "21": 1, "1632": 1, "1631": 1
}

# Deklarasi jumlah value untuk properti 'death'
death_prop_counts = {
    "0": 3453973, "2020": 3510, "2016": 3218, "2019": 3124, "2017": 3123,
    "2018": 3118, "2015": 3116, "2014": 2981, "2012": 2953, "2013": 2921,
    "2011": 2875, "2010": 2775, "2009": 2711, "2008": 2619, "2006": 2491,
    "2007": 2442, "2005": 2348, "2004": 2337, "2003": 2288, "2002": 2094,
    "2001": 2090, "1999": 2011, "2000": 1938, "1995": 1878, "1998": 1857,
    "1996": 1842, "1997": 1827, "1993": 1813, "1992": 1754, "1994": 1731,
    "1991": 1706, "1990": 1654, "1989": 1652, "1988": 1552, "1984": 1505,
    "1986": 1474, "1987": 1469, "1985": 1455, "1983": 1432, "1980": 1387,
    "1982": 1356, "1979": 1335, "1981": 1333, "1978": 1216, "1977": 1195,
    "1973": 1187, "1975": 1166, "1976": 1152, "1974": 1136, "1971": 1110,
    "1970": 1086, "1972": 1075, "1967": 1041, "1968": 1035, "1969": 1017,
    "1966": 951, "1965": 862, "1964": 861, "1962": 835, "1963": 807,
    "1961": 767, "1960": 752, "1958": 731, "1959": 704, "1957": 693,
    "2021": 655, "1956": 612, "1954": 603, "1944": 592, "1953": 591,
    "1955": 590, "1945": 573, "1951": 554, "1952": 552, "1942": 523,
    "1943": 500, "1950": 495, "1947": 486, "1949": 480, "1948": 457,
    "1946": 449, "1941": 439, "1940": 432, "1937": 394, "1939": 388,
    "1938": 383, "1936": 360, "1935": 326, "1933": 314, "1934": 305,
    "1931": 284, "1929": 276, "1932": 271, "1930": 253, "1928": 246,
    "1927": 224, "1924": 197, "1925": 196, "1923": 189, "1926": 185,
    "1920": 161, "1918": 160, "1922": 152, "1921": 149, "1919": 124,
    "1916": 123, "1917": 107, "1915": 101, "1914": 74, "1913": 54,
    "1912": 42, "1911": 39, "1910": 34, "1908": 31, "1909": 31,
    "1907": 24, "1904": 24, "1899": 24, "1905": 24, "1903": 22,
    "1889": 21, "1906": 20, "1890": 19, "1900": 19, "1895": 18,
    "1901": 18, "1902": 16, "1888": 15, "1894": 15, "1883": 15,
    "1896": 15, "1898": 15, "1871": 14, "1893": 14, "1891": 13,
    "1870": 13, "1873": 13, "1897": 13, "1882": 13, "1884": 12,
    "1865": 11, "1885": 10, "1892": 10, "1880": 10, "1886": 10,
    "1887": 10, "1863": 10, "1881": 9, "1849": 9, "1875": 9,
    "1859": 9, "1878": 9, "1855": 8, "1848": 8, "1861": 8,
    "1877": 8, "1876": 8, "1857": 8, "1872": 8, "1842": 8,
    "1862": 8, "1864": 8, "1852": 7, "1869": 7, "1856": 7,
    "1854": 7, "1843": 7, "1879": 6, "1805": 6, "1868": 6,
    "1874": 6, "1851": 6, "1866": 6, "1831": 6, "1828": 5,
    "1827": 5, "1794": 5, "1860": 5, "1837": 5, "1795": 5,
    "1836": 5, "1616": 4, "1778": 4, "1847": 4, "1625": 4,
    "1850": 4, "1830": 4, "1803": 4, "1853": 4, "1826": 4,
    "1715": 4, "1750": 3, "1400": 3, "1626": 3, "1838": 3,
    "1814": 3, "1801": 3, "1566": 3, "1635": 3, "1846": 3,
    "1867": 3, "1835": 3, "1832": 3, "1806": 3, "1677": 3,
    "1844": 3, "1811": 3, "1634": 3, "1823": 3, "1618": 3,
    "1821": 3, "1817": 2, "1553": 2, "1631": 2, "1791": 2,
    "1754": 2, "1822": 2, "1623": 2, "1824": 2, "1834": 2,
    "1695": 2, "1763": 2, "1723": 2, "1764": 2, "1799": 2,
    "1779": 2, "1787": 2, "1627": 2, "1829": 2, "1813": 2,
    "1809": 2, "1729": 2, "1580": 2, "17": 2, "1643": 2,
    "1792": 2, "1739": 2, "1812": 2, "1839": 2, "1840": 2,
    "1816": 2, "1688": 2, "1703": 2, "1797": 2, "1785": 2,
    "1726": 2, "1707": 2, "1804": 2, "1786": 2, "140": 2,
    "1845": 2, "1574": 2, "1576": 2, "1696": 2, "1591": 1,
    "1756": 1, "1250": 1, "1567": 1, "1759": 1, "1543": 1,
    "1796": 1, "1741": 1, "1789": 1, "1639": 1, "1780": 1,
    "1350": 1, "1681": 1, "1648": 1, "1375": 1, "1321": 1,
    "1529": 1, "1731": 1, "1713": 1, "1684": 1, "1733": 1,
    "1798": 1, "1820": 1, "1594": 1, "1784": 1, "1807": 1,
    "1732": 1, "1613": 1, "1793": 1, "1774": 1, "1220": 1,
    "1771": 1, "1584": 1, "1676": 1, "1693": 1, "1747": 1,
    "1558": 1, "1773": 1, "1527": 1, "1841": 1, "1781": 1,
    "1669": 1, "1637": 1, "95": 1, "1818": 1, "1471": 1,
    "1479": 1, "1728": 1, "1031": 1, "1782": 1, "1593": 1,
    "1601": 1, "1674": 1, "1698": 1, "1673": 1, "1541": 1,
    "1815": 1, "65": 1, "1706": 1, "1645": 1, "1699": 1,
    "1273": 1, "1630": 1, "1724": 1, "1463": 1, "1448": 1,
    "1745": 1, "66": 1, "1761": 1, "1191": 1, "1595": 1,
    "1767": 1, "1604": 1, "1611": 1, "1638": 1, "1720": 1,
    "1768": 1, "1581": 1, "1431": 1, "1679": 1, "1718": 1,
    "1790": 1, "1655": 1, "235": 1, "165": 1, "122": 1,
    "1179": 1, "1736": 1, "1757": 1, "1521": 1, "840": 1,
    "1585": 1, "1361": 1, "1569": 1, "1701": 1, "1519": 1,
    "1694": 1, "1468": 1, "1609": 1, "1571": 1, "1614": 1,
    "1556": 1, "1725": 1, "1408": 1, "1632": 1, "1549": 1,
    "1819": 1, "1470": 1, "1755": 1, "1672": 1, "27": 1,
    "1540": 1, "485": 1, "1602": 1, "1800": 1, "1640": 1,
    "1592": 1, "1744": 1, "1610": 1, "1564": 1, "1473": 1,
    "1788": 1, "1722": 1, "1668": 1, "1664": 1, "1697": 1,
    "1155": 1, "1641": 1, "5": 1, "1651": 1, "1700": 1
}

import re
import csv

def format_number(num):
    """Fungsi untuk menambahkan koma pemisah ribuan agar rapi"""
    try:
        return f"{int(num):,}"
    except (ValueError, TypeError):
        return num

def transform_query(query):
    # --- 1. MENGUBAH PROPERTI DI KLAUSA WHERE ---
    def property_replacer(match):
        var_name = match.group('var')
        prop_name = match.group('prop')
        raw_val = match.group('val')
        
        # Bersihkan tanda kutip (") atau (') jika nilainya berupa string
        clean_val = raw_val.strip('"\'')
        
        # Filter: Cari di dictionary yang sesuai
        if prop_name == "year":
            count = year_prop_counts.get(clean_val, "xxxxxx")
        elif prop_name == "birth":
            count = birth_prop_counts.get(clean_val, "xxxxxx")
        elif prop_name == "death":
            count = death_prop_counts.get(clean_val, "xxxxxx")
        elif prop_name == "category":
            count = category_prop_counts.get(clean_val, "xxxxxx")
        else:
            # Jika properti 'name', kembalikan persis seperti string aslinya
            return match.group(0)
            
        return f"{var_name}.{format_number(count)}"

    # REGEX BARU: Menangkap angka atau string ("..."), tanpa peduli tanda kurung/AND
    prop_pattern = re.compile(r'(?P<var>\w+)\.(?P<prop>\w+)\s*=\s*(?P<val>"[^"]*"|\'[^\']*\'|[0-9]+)')
    query = prop_pattern.sub(property_replacer, query)

    # --- 2. MENGUBAH POLA GRAF (NODE & RELASI) ---
    def path_replacer(match):
        s_var = match.group('s_var')
        s_lbl = match.group('s_lbl')
        r_lbl = match.group('r_lbl')
        t_var = match.group('t_var')
        t_lbl = match.group('t_lbl')

        # Ambil jumlah node
        s_count = person_node_counts.get(s_lbl, movie_node_counts.get(s_lbl, "xxxxxx"))
        t_count = movie_node_counts.get(t_lbl, person_node_counts.get(t_lbl, "xxxxxx"))

        # Ambil jumlah relasi masuk dan keluar
        out_count = outgoing_rel_counts.get(s_lbl, {}).get(r_lbl, "xxxxxx")
        in_count = incoming_rel_counts.get(t_lbl, {}).get(r_lbl, "xxxxxx")

        return f"({s_var}:{format_number(s_count)}) -[{format_number(out_count)}]-[{format_number(in_count)}]-> ({t_var}:{format_number(t_count)})"

    path_pattern = re.compile(
        r'\((?P<s_var>\w+):(?P<s_lbl>\w+)\)\s*-\[\s*(?:\w*\s*:)?\s*(?P<r_lbl>\w+)\s*\]->\s*\((?P<t_var>\w+):(?P<t_lbl>\w+)\)'
    )
    query = path_pattern.sub(path_replacer, query)

    return query

def cari_filter_pertama(query):
    """
    Menentukan var:label mana yang difilter pertama kali,
    berdasarkan angka terkecil di antara:
    - jumlah node (label) sumber
    - jumlah node (label) target
    - jumlah relasi keluar (outgoing) dari node sumber
    - jumlah relasi masuk (incoming) ke node target
    """
    path_pattern = re.compile(
        r'\((?P<s_var>\w+):(?P<s_lbl>\w+)\)\s*-\[\s*(?:\w*\s*:)?\s*(?P<r_lbl>\w+)\s*\]->\s*\((?P<t_var>\w+):(?P<t_lbl>\w+)\)'
    )

    kandidat = []  # list of (nilai, var, label)

    for m in path_pattern.finditer(query):
        s_var, s_lbl = m.group('s_var'), m.group('s_lbl')
        r_lbl = m.group('r_lbl')
        t_var, t_lbl = m.group('t_var'), m.group('t_lbl')

        s_count = person_node_counts.get(s_lbl, movie_node_counts.get(s_lbl))
        t_count = movie_node_counts.get(t_lbl, person_node_counts.get(t_lbl))
        out_count = outgoing_rel_counts.get(s_lbl, {}).get(r_lbl)
        in_count = incoming_rel_counts.get(t_lbl, {}).get(r_lbl)

        if s_count is not None:
            kandidat.append((s_count, s_var, s_lbl))
        if t_count is not None:
            kandidat.append((t_count, t_var, t_lbl))
        if out_count is not None:
            kandidat.append((out_count, s_var, s_lbl))
        if in_count is not None:
            kandidat.append((in_count, t_var, t_lbl))

    if not kandidat:
        return "-"

    nilai_min, var_min, lbl_min = min(kandidat, key=lambda x: x[0])
    return f"{var_min}:{lbl_min}"

def transform_file_kueri_baseline_to_numeric(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            daftar_kueri_asli = [line.strip() for line in f.readlines() if line.strip()]

        print(f"Berhasil membaca {len(daftar_kueri_asli)} kueri dari {input_file}...")

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')

            # Header kolom (ditambah 1 kolom baru)
            writer.writerow(['kueri asal', 'kueri numerik', 'filter pertama'])

            for kueri_asli in daftar_kueri_asli:
                kueri_numerik = transform_query(kueri_asli)
                filter_pertama = cari_filter_pertama(kueri_asli)
                writer.writerow([kueri_asli, kueri_numerik, filter_pertama])

        print(f"Selesai! Hasil telah disimpan ke dalam {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# # ==============================================================
# # EKSEKUSI PROGRAM
# # ==============================================================
# nama_file_input = 'Query_Where.txt'
# nama_file_output = 'Query_Where_Numerik.csv'

# proses_file_kueri(nama_file_input, nama_file_output)