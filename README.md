# NOTICE

There are things mentioned in this README that do not happen in the
code just yet. I have most of the pieces semi-working, but the program
is still in an unusable state. I wanted to make this README before
completing it just to keep track of my own guidelines and requirements
for the project.

# Lensmoor Wilderness Map Generator

The goal of this project is to create a system that players of Lensmoor
can use to help maintain an up-to-date map of the entire wilderness.
Since we no longer have access to the java applet, I decided to figure
out if a player could make a suitable replacement.

With the help of an atlas, an airship, some tintin++ scripts, and a
whole lot of trial and error, I discovered that yes - we can.

## Concepts/Glossary

If you want to make changes to the code or just understand how it
works, here are some necessary pieces of information.

### Room (or Point)

A room/point is a single place in the wilderness that a player can
stand in.

### View

A View is the ASCII 'map' that the player sees by default when
moving through the wilderness. While we're used to thinking of
the map as the 'room description', a View and a Room are two
very different things in this code.

### Roads

One of the biggest challenges of this project was to figure out
how to make it so that roads and rivers could be distinguished
from each other without the use of color. I wanted to be able to
store all of the map data as a flat, colorless text file that
was reasonably human-readable.

The data is intended to be re-converted back into something you can
view in color on a webpage. In webpage form, roads will look just
as they do in-game - bright white ASCII lines.

However, I wanted players to be able to read the raw text data in a
pinch, if the HTML version is unavailable or undesired.

For these reasons, roads get converted into the numbers 1-5 in the raw
text. I don't believe these numbers are used anywhere in the wilderness
system, so they are a way for roads to still appear as unique, simple,
single-character symbols - even if they do feel slightly janky.

The good news is that even if you do prefer to read the map in its flat
form, you don't really need to care what number the road is. You'll
just be able to know that if you see the numbers 1-5, that's a road,
not a river.

Rivers still use the normal 'line' characters as before. Here is what
each Road symbol gets converted to:

```
+   ->   1
-   ->   2
|   ->   3
\   ->   4
/   ->   5
```
### Observable World Dimensions
Lensmoor's wilderness has 1299 rows from top to bottom. This is a hardcoded
limit, and players cannot move beyond the top and bottom borders. (It's
interesting to note that the atlas *can* move beyond these borders, but
it shows completely blank space when you do so.) 

The world is also *roughly* 2000 rooms wide from left to right. It's
really difficult to accurately gauge how wide the world is. It can be
circumnavigated, but it starts behaving very weirdly beyond the 2000
mark.

When experimenting with the atlas, I noticed that I can move it
920 rooms west of New Lensmoor without anything weird happening.
But on the next movement west... the X in the middle of the view
*disappears*.

This is quite bizarre and I take it as a sign that this must be
where the western border of the world is. This is reflected in how
I wrote this program. New Lensmoor is 920 rooms east of this border.

From the west border, I can move 1995 rooms east in the atlas, but
once I try to move beyond 1995, the red X disappears again. This is
what makes me believe that the world is roughly 2000 rooms wide. It
may be similar to the up-down border - it might be 1999 rooms wide.
I haven't done precise enough testing to figure this out yet, though.

Once I found the western border, I moved the atlas all the way down
to the bottom border of the world. This was 975 rooms south of NL.

In total, the lower left corner of the observable world is 920 rooms
west and 975 rooms south of New Lensmoor.

This lower left corner is where this program considers the world origin
to be. All other coordinates are handled relative to this corner.

It feels a little bit counter-intuitive to be using the lower left
corner instead of the *upper* left corner, but I did it this way
because I wanted the Y coordinate to feel like the 'north/up'
direction. I also didn't want to have to use potentially confusing
'negative coordinates'.

Think of the lower left corner of the world as being the origin of
a graph, with everything existing up and to the right of it:
```
           ^
           |
           |        (The whole world
           |         map is up in this
           |         quadrant of our
           |         imaginary graph)
           |
   -X, +Y  | +X, +Y
-----------+--------------------------->
   -X, -Y  | +X, -Y
           |
           |
```

Using this way of thinking, all coordinates are expressed in positive
numbers. If we had some kind of landmark area that was confirmed by
imms to be exactly in the center of the world, I would probably use that
as my origin instead, with a willingness to use negative coordinates.
But since we don't have an area like that, I figured that what I've done
here would be the simplest way to establish the world boundaries.

The good news is that you don't have to move the atlas all the way to
the bottom left to sync it up with your scripts. All you need to do is
know the coordinates of other areas. An atlas can be told to center on
an area, so if you know the coordinates of a given area, you can set
your script's 'start point' accordingly.

Since 920, 975 is such a nice set of coordinates, I do most of my
map logging by starting with New Lensmoor. I plan to make a list of
other areas that have coordinates that end in 0 and 5, so that it'll
be easier to get to specific parts of the world when you want to map
out uncharted territory.

# The Process

## Gathering the Data

Before the data can be processed, it has to be gathered. This is done
by using your MUD client's logging feature while using an 'atlas' object
in-game. The librarian in the New Lensmoor University has one.

### Log Format

Your client must be logging the output in *raw* form, with ANSI color.
Yes, I'm talking about those really ugly escape sequences that make a
file completely human-unreadable. This program needs those!

Now, in theory, you COULD generate a wilderness map using logs that
have no color at all, but roads and rivers would become identical in
the finished map. If you don't mind this and you're making some kind
of funky alternate map, nothing is stopping you from using a colorless
log to do so.

### Necessary Scripts

You also need to have scripts that will automatically track and display
coordinates as you manipulate the atlas. I will provide examples of
tintin++ scripts for this in this repository (once I've polished them).

Until then, what you need to know is that when you're moving the atlas
view, your client MUST output a line that displays your coordinates.
This line must be visible in the logfile.

The true coordinate information is not available to players in-game,
but for the purposes of this program, New Lensmoor is at 920, 975.
You can use this to 'calibrate' your scripts to be able to follow
the atlas.

The atlas moves 5 rooms in whatever direction you move it in, so
your coordinates need to be updated accordingly on each movement.

For this program to work, a line reading `COORDINATES: X, Y` MUST
precede every View in the log, like this:

```
COORDINATES: 920, 975
       .           -------KEY-------
    .......        | * A City/Area |
   .........       | . Plains      |
  ++|.....###      | # Forest      |
 .|.|....#####     | + Road/River  |
 ...||--------     | X You         |
 *..|...*#####     -----------------
*--++|-X..#####
 ...|....#####
 ...||--------
 *-+|.........
  .|.........
   |........
    .......
       .


COORDINATES: 925, 975
       .           -------KEY-------
    ......#        | * A City/Area |
   ....#####       | . Plains      |
  ...#####*##      | # Forest      |
 ...######+---     | + Road/River  |
 ---------|###     | X You         |
 ..*##########     -----------------
|-*..##X######|
 ...#########|
 ------------|
 ............#
  .........*.
   .........
    ....###
       .
```

For right now, the process of scripting this is an exercise for the
reader. But if for whatever reason I never put up my polished tintin++
scripts, hopefully this will be enough information for a future coder
to be able to make use of this program.

## Processing the data

Once you've mapped some rooms, you can run the program with the
logfile as a command line argument. Right now, the code is such that
if you want a map of the entire world, you'd have to use the atlas
to look at ALL of it in a single session. It's more of a proof of
concept right now - eventually, I'll make it so that it can work with
multiple logfiles collected in a directory, so the data can be gathered
over time.

The program reads in all the lines in the file, then begins splitting
them up into Views. Each View object is comprised of its coordinates
and the 15 lines that make up the ASCII automap. The coordinates of
the View represent its center, where you see the player 'X'.

### Tidying

Once the Views are created, then the program strips out unneeded data
and converts roads to numbers, as mentioned above. This is the list
of things that get stripped out of each string:

* ANSI colors
* the key/legend
* extra spaces
* newlines

This leaves us with nice, trimmed lines that don't have any weird
escape codes in them. Removing the key probably isn't strictly
necessary, but I decided to leave that functionality in in case someone
makes a fork that requires it.

### Plotting

Once all of the Views are tidied up, that's when we start taking
each individual character from them and plotting them onto the
world map. The world map is a 2D array whose size is based on
the observable size of the Lensmoor world as detailed above.

There are 1299 elements in the array. Within each of these
elements is another set of 1995 elements. Each one of these
elements is a single character.

When the array is first generated, it is filled completely with
spaces. Using the data in the Views, these spaces are replaced
with whatever characters have been gathered and processed. And
finally, once all of these replacements have been done... the
result gets printed out.

The result is a 1299-line, 1995-column text file that is a 1:1
representation of the Lensmoor wilderness. Areas that were not
logged are left as empty space. The empty space is there to
preserve the structure of things that *did* get recorded.
