# Movie Trailer Website
This program generates a webpage and run it in the browser, through the data of the movies submitted inside the file 'entertainment_center.py'. This webpage takes the trailer URL from the data for each movie and run them when clicked on any movie image.


# Installation:

Once you have downloaded the files:
Type in the following commands in your terminal when you are inside root/home folder (through your terminal)  to run the program:

```
cd movietrailer
python entertainment_center.py
```

# Working
The Program "entertainment_center.py" takes the data for movies . Each movie data is assigned to an Instance which uses the class "Movie" and is imported with the file 'media.py' . media.py acts as a constructor for the variables inside the Instance.
Finally all the instances are added into a list 'movies'.
The program then uses the function "open_movies_page()" which is defined inside the file "fresh_tomatoes.py". This function takes the list 'movies' as its argument and generates a webpage of our data, it also opens the browser with our generated webpage on it. 
