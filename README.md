# Fortnite Locker Statistics #
Created by Rubi Dionisio

## Description ##
This application is based on the video game Fortnite. In Fortnite, players have a wide
selection of cosmetics consisting of outfits, backpacks, emotes, pickaxes, and more that players can mix
and match to customize their character. This application is similar to this, except that it will also
allow for users to keep track of their own game stats using a specific locker combination. The overall
goal of my software system is for users to be able to reference their game stats for specific cosmetic
combinations and also be able to get more information on cosmetic items, such as rarity, set they belong
to, etc. Users can input, or log, cosmetic combinations that they have used in-game in the
past and also log in those game statistics and also update pre-existing logs as well. Whenever
they wish to, users can see overall game statistics for their combo they wish to see.
Information like the number of solo, double, trio, and squad wins should appear. Additionally, the user
should be able to see specific information pertaining to a certain cosmetic, such as seeing the rarity and
the set a certain outfit belongs to.

## How to Run ##
First you want to set up a new postgreSQL database using the following steps:

    * Create a new Database in pg_admin
    * Make sure that the host = localhost
    * Name the database 'fortnite' without the quotations
    * set the username as 'postgres' without the quotations
    * set the password as 'password' without the quotations

Then clone the repository https://github.com/dionisio-rubi/fortnite-locker-stats.git or if you download the files that works too.

Before running thr program, you need to have the fortnite information from the API so you can run the program, in the main.py file on line 618,make sure to uncomment the following:

```python
# getFortnite()
```

Lastly, to run the program, cd into the project folder, or make sure you are in the project folder. Then, run the command in the terminal:

```python
python3 main.py
```
To exit the application, just press the X button on the top right. After exiting the program, make sure to comment the line you uncommented beforehand, otherwise your locker will be cleared. That's it! Have fun! :)


## Sources Used ##
- [Fortnite API](https://fortnite-api.com/v2/cosmetics/br)