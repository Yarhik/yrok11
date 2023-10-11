
class Video:
    chis= 0
    def __init__(self, name, sec, min, youtuber, year):
        self.name = name
        self.sec = sec
        self.min = min
        self.youtuber = youtuber
        self.year = year
        Video.chis+= 1

lol = Video("jailbreake", 54, 10, "Pozzi", 2017)
ez = Video("photoshop", 13, 4, "Pozzi", 2016)

print(Video.chis)