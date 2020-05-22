class Sentiment:
    def __init__(self, msg):
        self.msg = msg
        self.score = 0

    def analyze(self):
        dict = {
            "good" : 1, "better" : 2, "best" : 3,
            "bad" : -1, "worst" : -3, "dirty" : -2
        }
        for word in self.msg :
            if word in dict:
                    self.score += dict[word]
                    print(word)
        return self.score

class Analysis(Sentiment):
    def review(self):
        if(self.score > 0):
            return("Comment is Positive")
        elif(self.score < 0):
            return("Comment is Negative")
        else:
            return("Comment is Neutral")

msg = input("Enter your Message : ").split()
s = Analysis(msg)
score = s.analyze()
print(s.review())
