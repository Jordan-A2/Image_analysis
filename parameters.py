TwoToTwo

cap         = cv.VideoCapture('./Working Videos/TwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/TwoToTwo.mp4') # Input feed
baseNames   = ['Mixed bellpeppers','The other bellpepper and stones'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 0 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weigth
changeLevel = 2 # Amount of successes or discards needed in a row to change state


OneToOne

cap         = cv.VideoCapture('./Working Videos/OneToOneBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/OneToOne.mp4') # Input feed
baseNames   = ['Non ripe strawberry','Pee'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 20 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 20 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards needed in a row to change state


LongRealVeg

cap         = cv.VideoCapture('./Working Videos/LongRealVegBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/LongRealVeg.mp4') # Input feed
baseNames   = ['Corn','Peas'] # Names of the objects
weight      = -10 # How much more should high intensity pixels count (Standard 2)
threshold   = 10 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 1 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 4 # Amount of successes or discards needed in a row to change state


ShortRealVeg

cap         = cv.VideoCapture('./Working Videos/ShortRealVegBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/ShortRealVeg.mp4') # Input feed
baseNames   = ['Peas','','','Corn','',''] # Names of the objects
weight      = 0 # How much more should high intensity pixels count (Standard 2)
threshold   = 0 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 25 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 5 # Amount of successes or discards needed in a row to change state


TwoToOneToOne

cap         = cv.VideoCapture('./Working Videos/TwoToOneToOneBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/TwoToOneToOne.mp4') # Input feed
baseNames   = ['Blueberry and stone','Dirty Lemon','Lime'] # Names of the objects
weight      = 0 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards needed in a row to change state


NOneToOne

cap         = cv.VideoCapture('./Working Videos/NMixBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/NOneToOne.mp4') # Input feed
baseNames   = ['Skittles','Skittles again but only the blue ones which have then been left out in the sun','Skittles again, again but only the sun dried ones, but soaked in purple paint','','','Dirty autumn','Psychadelic blueberries','Sand with dirty oranges in it','Dirty blueberries'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards 3eeded in a row to change state


NTwoToTwo
cap         = cv.VideoCapture('./Working Videos/NMixBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/NTwoToTwo.mp4') # Input feed
baseNames   = ['Skittles','Skittles again but only the blue ones which have then been left out in the sun','Skittles again, again but only the sun dried ones, but soaked in purple paint','','','Dirty autumn','Psychadelic blueberries','Sand with dirty oranges in it','Dirty blueberries'] # Names of the objects
weight      = 5 # How much more should high intensity pixels count (Standard 2)
threshold   = 25 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards 3eeded in a row to change state


NTwoToOneToOne

cap         = cv.VideoCapture('./Working Videos/NMixBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/NTwoToOneToOne.mp4') # Input feed
baseNames   = ['Skittles','Skittles again but only the blue ones which have then been left out in the sun','Skittles again, again but only the sun dried ones, but soaked in purple paint','','','Dirty autumn','Psychadelic blueberries','Sand with dirty oranges in it','Dirty blueberries'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards 3eeded in a row to change state


N1TwoToTwoToTwo

cap         = cv.VideoCapture('./Working Videos/N123TwoToTwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/N1TwoToTwoToTwo.mp4') # Input feed
baseNames   = ['Blueberries that are trying their best (keep up the good work, we are so proud of you!)','Legit blueberries','Wild berries in bushes','Not mixed grapes','Warm autumn','Not mixed grapes as well, but the other kind of grapes','Grape mix','Psycadelic berry mix','Psycadelic waterfall with blueberries in it'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards 3eeded in a row to change state


N2TwoToTwoToTwo

cap         = cv.VideoCapture('./Working Videos/N123TwoToTwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/N2TwoToTwoToTwo.mp4') # Input feed
baseNames   = ['Blueberries that are trying their best (keep up the good work, we are so proud of you!)','Legit blueberries','Wild berries in bushes','Not mixed grapes','Warm autumn','Not mixed grapes as well, but the other kind of grapes','Grape mix','Psycadelic berry mix','Psycadelic waterfall with blueberries in it'] # Names of the objects
weight      = -15 # How much more should high intensity pixels count (Standard 2)
threshold   = 200 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 50 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 10 # Amount of successes or discards 3eeded in a row to change state


N3TwoToTwoToTwo

cap         = cv.VideoCapture('./Working Videos/N123TwoToTwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/N3TwoToTwoToTwo.mp4') # Input feed
baseNames   = ['Blueberries that are trying their best (keep up the good work, we are so proud of you!)','Legit blueberries','Wild berries in bushes','Not mixed grapes','Warm autumn','Not mixed grapes as well, but the other kind of grapes','Grape mix','Psycadelic berry mix','Psycadelic waterfall with blueberries in it'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards 3eeded in a row to change state


PaperOneToOne

cap         = cv.VideoCapture('./Working Videos/PaperOneToOneBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/PaperOneToOne.mp4') # Input feed
baseNames   = ['Lime','Lemon'] # Names of the objects
weight      = -10 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 1 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 4 # Amount of successes or discards 3eeded in a row to change state


PaperTwoToTwo

cap         = cv.VideoCapture('./Working Videos/PaperTwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/PaperTwoToTwo.mp4') # Input feed
baseNames   = ['Christmas','Shit easter'] # Names of the objects
weight      = -5 # How much more should high intensity pixels count (Standard 2)
threshold   = 2 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 1 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 2 # Amount of successes or discards 3eeded in a row to change state


PaperTwoToTwoToTwo

cap         = cv.VideoCapture('./Working Videos/PaperTwoToTwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/PaperTwoToTwoToTwo.mp4') # Input feed
baseNames   = ['Game Of Thrones','Rødkål med gammel fløde','Orange tree'] # Names of the objects
weight      = 5 # How much more should high intensity pixels count (Standard 2)
threshold   = 25 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 1 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards 3eeded in a row to change state


PaperTwoToOneToOne

cap         = cv.VideoCapture('./Working Videos/PaperTwoToOneToOneBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/PaperTwoToOneToOne.mp4') # Input feed
baseNames   = ['Vomit on the floor','Water in a toiletbowl','Urine in a toiletbowl but also on the floor'] # Names of the objects
weight      = 5 # How much more should high intensity pixels count (Standard 2)
threshold   = 10 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 1 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 2 # Amount of successes or discards 3eeded in a row to change state


PaperThreeToThree

cap         = cv.VideoCapture('./Working Videos/PaperThreeToThreeBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/PaperThreeToThree.mp4') # Input feed
baseNames   = ['Good soup','Bad soup'] # Names of the objects
weight      = 5 # How much more should high intensity pixels count (Standard 2)
threshold   = 20 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 1 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 2 # Amount of successes or discards 3eeded in a row to change state