# CodingChallenge-TextSimilarity


•	Do you count punctuation or only words?
     I counted only the words and have removed all the punctuations. Also, any whitespaces in the sentences are also removed for better results.
•	Which words should matter in the similarity comparison?
     Well, there are few words which has more weightage and few other words which are to be ignored as they are the helping verbs, articles, conjunction words etc. Basically, our focus needs to be on the keywords or the important words of the sentences. Also, we can perform tokenization, stemming on the words and check for better similarity.
•	Do you care about the ordering of words?
     Yes, ordering of the words does matter in the analysis of similarity. There are lot of methods in NLP which can be used for Semantic and lexical similarities of the sentences and different scenario demands different algorithm usage in my opinion. 
•	What metric do you use to assign a numerical value to the similarity?
     I have used the reference of Cosine Formula which is used to find the similarity as this convinced me to be the better one when compared to other ones. But have not used the Cosine Similarity readily available function, have built the formula using the math library.
•	What type of data structures should be used? 
     I have used Lists, Dictionaries, Sets in my code. 

I found that the sample 1 and 2 are more similar when compared sample 1 and 3. Overall it was really fun not to use the external python libraries and create your own code.
Bonus: Have tried creating a Web service API with the POST method. Flask library was helpful. Utilized the docker Container and image to and run the project. Finally uploaded to the GitHub.


