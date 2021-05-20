import pickle
import re
# Save fit vectorizer and fit tfidftransformer, use in prediction
from sklearn.feature_extraction.text import CountVectorizer

# a = ["This product is   amazing usama@gmail.com", "I     love this %product", "Very disappointed by this product"]


with open('home/nlp/MultinomialNB.pkl', 'rb') as f:
    modelLogistic = pickle.load(f)

feature_path = 'home/nlp/feature.pkl'
loaded_vec = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open(feature_path, "rb")))
#b = loaded_vec.transform([a])
#print(a)
##def inputList():
##    global a
##    
##    outputPredict(a)
#print(modelLogistic.predict(b))
def outputPredict(commentList):
    prediction = []
    posCount = 0
    commentCount = len(commentList)
    for i in commentList: 
        vecResult = loaded_vec.transform([cleanText(i)])
        pred = modelLogistic.predict(vecResult)
        if pred[0] == 1:
            posCount += 1
        prediction.append(pred[0])
    posPercent = (posCount / commentCount) * 100
    negPercent = 100 - posPercent
    predictions = {'positive':posPercent, 'negative':negPercent}
    return predictions
def cleanText(rawText):
    """This function will clean input raw text to be used for prediction
    Input Parameters: Raw Text
    Output: Clean Text
    """
    if type(rawText) != str:
        rawText = str(rawText)
    # Normalizing the data
    rawText = rawText.lower()#lower case conversion
    # Removing emails if there's any
    rawText=re.sub('([\w]+@[\w]+.+)', "", rawText)
    # Removing Special Characters
    rawText=re.sub('[^A-Z a-z 0-9-]+',"",rawText)
    # Removing Extra Spaces
    rawText=" ".join(rawText.split())
    #print("Cleaned Text:", rawText)
    return(rawText)
#inputList()
# outputPredict(a)
