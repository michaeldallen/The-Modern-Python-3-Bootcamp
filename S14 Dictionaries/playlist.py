
playlist = {
    "title" : "patagolia bus",
    "author" : "colt steele",

    "songs" : [
        {
            "title" : "turn it off",
            "artist" : ["culture abuse"],
            "album" : "peach",
            "date" : "2017-10-31",
            "duration" : "3:37",
        },
        {
            "title" : "eating hooks",
            "artist" : ["moderat", "siriusumo", "solomun" ],
            "album" : "eating hooks remix",
            "date" : "2017-11-06",
            "duration" : "7:02",
        },
        {
            "title" : "nights off",
            "artist" : "siriusumo",
            "album" : "mosaik",
            "date" : "2017-11-06",
            "duration" : "4:08",
        }
    ]
}


def running_time(p):
    
    d=0
    for s in p["songs"]:
        [mn, sc] = s["duration"].split(":")
        d += (int(mn) * 60) + int(sc)
    (m,s) = divmod(d, 60)
    return(str(m) + ":" + str(s))

print(f"running time: for {playlist['title']} is {running_time(playlist)}")
