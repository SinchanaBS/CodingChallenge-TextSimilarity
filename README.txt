Instructions to Run (Windows OS)
Clone the project
One way is to run the Project (app.py) directly without the docker:
Please use Python 3 or above version.
$ pip install flask (also please try pip3 if you have pip upgraded to pip3)
$ python app.py 
(please make sure to be in web folder to run above cmd, you can use cd to navigate to web folder)
Now please click on your link shown on the terminal when you run your program (localhost:5000)

Running the program with Docker:
Please have the docker installed, Virtual Machine with the network port http and connected to the internet.
Navigate to web folder (cd command)
To build docker image run the below command
$ docker build -t flask-sample:latest .
To run the docker container
$ docker run -d -p 5000:5000 flask-sample
$ docker ps -a
Now that the container is up and running! We can run using the docker compose 
$ docker stop #containerId
Come out of the web folder and run the below commands
$ cd..
$ docker-compose build
$ docker-compose up
Now please click on your link shown on the terminal when you run your program (localhost:5000)


• Do you count punctuation or only words?
       I counted only the words and have removed all the punctuations. Also, any whitespaces in the sentences are also removed for better results.

• Which words should matter in the similarity comparison?
       Well, there are few words which has more weightage and few other words which are to be ignored as they are the helping verbs, articles, conjunction words etc. Basically, our focus needs to be on the keywords or the important words of the sentences. Also, we can perform tokenization, stemming on the words and check for better similarity.

• Do you care about the ordering of words?
       Yes, ordering of the words does matter in the analysis of similarity. There are lot of methods in NLP which can be used for Semantic and lexical similarities of the sentences and different scenario demands different algorithm usage in my opinion. 

• What metric do you use to assign a numerical value to the similarity?
       I have used the reference of Cosine Formula which is used to find the similarity as this convinced me to be the better one when compared to other ones. But have not used the Cosine Similarity readily available function, have built the formula using the math library.

• What type of data structures should be used? 
       I have used Lists, Dictionaries, Sets in my code. 

I found that the sample 1 and 2 to be more similar when compared sample 1 and 3. Overall it was fun not to use the external python libraries and create your own code.
Bonus: Have tried creating a Web service API with the POST method. Flask library was helpful. Utilized the docker Container to add the Web Service and run it.
