# My CD Library

In the summer of 2024, I began collecting compact discs so I could listen to my favourite classical music in such a way that does not require me to use music streaming services like Spotify, Apple Music, etc. I recently began documenting each CD that I own for several reasons. Firstly, I enjoy documenting things, and this is a fun project to do in my free time. Secondly, I can remember what CDs I have when I am not near my collection (I can't bring all 120+ discs with me everywhere!). Thirdly, people I know who want to gift me CDs always worry that they will get me a duplicate; now, they have no excuse for not knowing my collection inside-and-out as well as I do!

# The Template

Each "disc" (which may actually include multiple CDs) is documented in JSON format that follows the template provided in `template.json`. Some objects, like boxed sets of CDs, or CD cases that contain two or more discs are in my collection and I wanted each physical object to map to one file. This template allows multiple discs to be documented per file. The fields for each file are described as follows:

 - `"SPARS code"`: a [three-position code](https://en.wikipedia.org/wiki/SPARS_code) denoting the type of recording equipment used to produce the audio on the CD. The first position represents the recording equipment (i.e. micorphones); the second position represents the mixing equipment, and the third position represents the delivery equipment (the CD itself). Since CDs are digital by nature, the last letter of the code is always `D` (for `D`igital) in these files. Some CDs have `A`s (for `A`nalog) in the first two positions, but `DDD` (all digital) is the most common, with ≈75% of discs using this format.
 - `"all artists"`: a list of the names of every artist featured on the discs contained in this jewel case.
 - `"copyright date"`: copyright date listed on the back of the case.
 - `"id"`: sequential ID, unique to each file.
 - `"label"`: the record label that produced this recording.
 - `"num discs"`: the number of discs documented in this file.
 - `"title"`: the title printed on the side of the case. This is also documented in the name of the file.
 - `"discs"`: the specific information for each disc.
   - `"number"`: order of this disc as it appears in the jewel case.
   - `"total timing"`: total duration of the recording on this disc. Due to the technological limitations of CDs, this is almost always 80 minutes or less.
   - `"pieces"`": specific information for each piece of music on the disc.
     - `"artists"`: a list containing the names of the artists that feature on this piece of music.
     - `"catalogue"`: the system used to document this piece within the composer's output. Most often this is "opus", for opus numbers. Some composers have different works catalogues, like "BWV" (Bach Werke Verzeichnis) for J.S. Bach, or "K" (the Köchel catalogue) for W.A. Mozart. Some composers have multiple catalogues, like Belá Bartók, who has opus numbers, the "Sz" catalogue (by András Szőllősy), and the chronological "BB" catalogue by László Somfai. For example, Dmitri Shostakovich's 5th Symphony is marked as Opus 47—this field would be marked as `"opus"`.
     - `"catalogue num"`: the position of this piece within the catalogue. For example, Dmitri Shostakovich's 5th Symphony is marked as Opus 47—this field would be marked as `47`.
     - `"composer"`: the name of the composer.
     - `"date"`: the date this piece was composed.
     - `"num movements"`: the number of movements this piece has. 
     - `"title"`: the title of thits piece.
     - `"tracks"`: a list containing one of the following: if this piece spans only one track on the CD, then this list contains only the number of the track it occupies. If this piece occupies multiple tracks, then the first element of the list is the number of the first track the piece occupies and the second element of the list is the number of the last track the piece occupies. 
     - `"movements"`: the specific information for each movement of the piece.
       - `"number"`: the number of the movement within the the piece of music.
       - `"subtitle"`: occupied if this movement has a title beyond the title of the piece as a whole.
       - `"timing"`: the duration of this entire movement.
       - `"tracks"`: a list containing one of the following: if this movement spans only one track on the CD, then this list contains only the number of the track it occupies. If this movement occupies multiple tracks, then the first element of the list is the number of the first track the movement occupies and the second element of the list is the number of the last track the movement occupies. 
       - `"subtracks"`: on rare occasions when movements are divided among multiple tracks, this list will contain a list of the specific information for each track that the movement occupies. More often than not, this list will be empty.
         - `"subtitle"`: occupied if the subtrack has a title beyond what the movement is titled.
         - `"timing"`: the duration of the single track this object refers to.
         - `"track"`: the number of the single track this object refers to.

### Default values:

Numerical: `-1`  
String: `""`  
List: `[]`  

# Naming Conventions

### File names

Each disc uses the (family) name of the _artist_ for which I am most likely to remember the disc by, followed by a colon and the name printed on the side of the CD casing. In most cases, the artist whose name the file bears is fairly straightforward; if the album contains music by only one composer, then I use that composer's name. If there are multiple composers featured, but one piece on the album is clearly the most prominent work, then I use the name of the most prominent piece's composer. 

File names are far less strictly organized; sometimes, the name printed on the side of a CD case includes the main composer's name at the very front, in which case I do not need to add anything to the file name. If the main artist on a disc has their name featured in a title, but it includes both personal and family names, then I may modify the title so that the artist's family name appears first in the title. 

Some albums do not have a single identifiable main artist (e.g. "Finlandia: A Festival of Finnish Music"). In this case, I use the name printed on the CD for the file name. In other similar cases, I might re-arrange the words in the title so that the word with which I primarily associate the album appears first (e.g. "The Fantastic Philadelphians" $\rightarrow$ "Philadelphians, The Fantastic"). I try to ensure that the artist or group or keyword that the album most clearly associates itself with appears as the first word of the file name.

File names are inconsistently organized, but the characteristic which unifies them is that sorting file names lexographically always follows the sorted order in which I keep my physical CD cases. 

### Artist names

Artist names are organized as follows: `[family name][delimiter][personal name]`  
If the artist's name follows the convention of putting the personal name before the family name, then the delimiter is a `,`. If the artist's name follows the convention of putting the family name before the personal name, then the delimiter is a `.`. 

# To Do

 - Add links to images of album covers (I understand the irony that all my CDs are available online)
 - I currently have 2, or maybe 4, individual CDs and one boxed set containing 12 CDs that I have yet o catalogue. 