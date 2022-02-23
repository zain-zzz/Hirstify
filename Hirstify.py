#disclaimer: all songs shown here are entirely made up and don't actually exist.
songlength = 0
isTaken = True
isFound = True
questionChange = False
import time
import random
print("Welcome to Hirstify\n")
isNew = input("Would you like to create a new account or login(new/login)\n")
#New user name
if isNew == "new" or isNew == "New":
    with open("users.txt", "r") as users:
        fileNames = users.readlines()
        loops = len(fileNames) - 1
        while isTaken:
            isTaken = False
            userName = input("Please input your desired user name\n")
            userName = userName.lower()
            loops = len(fileNames) - 1
            while loops != 0:
                temp = fileNames[loops]
                temp = temp.strip('\n')
                if userName == temp:
                    print("Sorry that user name isn't available\n")
                    isTaken = True
                loops -= 1
    with open("users.txt", "a") as users:
        users.write(userName + "\n")
        users.close()
#New user fav. genre
    with open("genre.txt", "a") as genre:
        SelectedGenre = input("What's your favourite genre?\n The genres we have available as of now are: pop, surreal, rock, summer\n")
        while SelectedGenre != 'pop' and SelectedGenre != 'Pop' and SelectedGenre != 'surreal' and SelectedGenre != 'Surreal' and SelectedGenre != 'rock' and SelectedGenre != 'Rock':
            SelectedGenre = input('Sorry, either that genre isn\'t available or you\'ve typed it wrong\n')
        if SelectedGenre == 'pop' or SelectedGenre == 'Pop':
            genre.write("pop\n")
        if SelectedGenre == 'surreal' or SelectedGenre == 'Surreal':
            genre.write("surreal\n")
        if SelectedGenre == 'rock' or SelectedGenre == 'Rock':
            genre.write("rock\n")
        genre.close()
#fav artist
    with open("artist.txt", "a") as artist:
        SelectedArtist = input("What's your favourite artist?\nRight now our available artists are: 'kenny', 'aquaman', 'stoneyhedge', 'barockobama' and 'gaster'")
        SelectedArtist = SelectedArtist.lower()
        while SelectedArtist != 'kenny' and SelectedArtist != 'aquaman' and SelectedArtist != 'stoneyhedge' and SelectedArtist != 'barockobama' and SelectedArtist!= 'gaster':
            SelectedArtist = input('Sorry, either that artist isn\'t available or you\'ve typed it wrong\n')
        artist.write(SelectedArtist)
        artist.close()

else:
#slightly edited version of the module before is used for convinience
    with open("users.txt", "r") as users:
        fileNames = users.readlines()
        while isFound:
            isFound = False
            if questionChange:
                print("Username not found, please input it again.")
                time.sleep(0.25)
                questionChange = False
            if not questionChange:
                userName = input("What's your username?\n")
            loops = len(fileNames) - 1
            while loops != 0:
                temp = fileNames[loops]
                temp = temp.strip('\n')
                if userName == temp:
                    print("Username found.")
                    loops = 1
                    isFound = False
                else:
                    isFound = True
                    questionChange = True
                loops -= 1

#finding genre and artist for user
with open('users.txt', 'r') as info:
    fileNames = info.readlines()
    while True:
        loops = len(fileNames) - 1
        while loops != 0:
            temp = fileNames[loops]
            temp = temp.strip('\n')
            if userName == temp:
                break
            loops -= 1
        break
    info.close()
with open('genre.txt','r') as info:
    genreNames = info.readlines()
    info.close()
with open('artist.txt','r') as info:
    artistNames = info.readlines()
    info.close()
userName = (fileNames[loops])
genreName = genreNames[loops]
artistName = artistNames[loops]
#artist change
change = input('Would you like to change your selected artist?(yes/no)\n')
if change.lower() == 'yes' or change.lower == 'y':
    with open("artist.txt", "r") as artist:
        data = artist.readlines()
    SelectedArtist = input("Who do you want to change your artist to?\nRight now our available artists are: 'kenny', 'aquaman', 'stoneyhedge', 'barockobama' and 'gaster'")
    SelectedArtist = SelectedArtist.lower()
    while SelectedArtist != 'kenny' and SelectedArtist != 'aquaman' and SelectedArtist != 'stoneyhedge' and SelectedArtist != 'barockobama' and SelectedArtist != 'gaster':
        SelectedArtist = input('Sorry, either that artist isn\'t available or you\'ve typed it wrong\n')
    data[loops] = (SelectedArtist + '\n')
    with open('artist.txt', 'w') as artist:
        artist.writelines(data)
        artist.close()
#genre change
change = input('Would you like to change your selected genre?(yes/no)\n')
if change.lower() == 'yes' or change.lower == 'y':
    with open("genre.txt", "r") as genre:
        data = genre.readlines()
    SelectedGenre = input("What do you want to change your genre to?\n The genres we have available as of now are: pop, surreal, rock\n")
    while SelectedGenre != 'pop' and SelectedGenre != 'Pop' and SelectedGenre != 'surreal' and SelectedGenre != 'Surreal' and SelectedGenre != 'rock' and SelectedGenre != 'Rock':
        SelectedGenre = input('Sorry, either that genre isn\'t available or you\'ve typed it wrong\n')
    if SelectedGenre == 'pop' or SelectedGenre == 'Pop':
        data[loops] = ("pop\n")
    if SelectedGenre == 'surreal' or SelectedGenre == 'Surreal':
        data[loops] = ("surreal\n")
    if SelectedGenre == 'rock' or SelectedGenre == 'Rock':
        data[loops] = ("rock\n")
    with open("genre.txt", "r") as genre:
        genre.writelines(data)
        genre.close()
#songs
rock = [['granite', 128, 'rock', 'kenny'],['redstone', 142, 'rock','barockobama'],['lapis lazuli', 73, 'rock','stoneyhedge'],['obsidian', 203, 'rock','barockobama'],['sandstone', 52, 'rock','barockobama'],['chalk', 152, 'rock', 'gaster'],['basalt', 153, 'rock', 'barockobama']]
surreal = [['moisten', 142, 'surreal', 'aquaman'],['pepsi', 124, 'surreal', 'kenny'],['maxim', 90, 'surreal', 'aquaman'],[ 'octahedron', 53, 'surreal', 'aquaman'],[ 'vegetal', 93, 'surreal', 'aquaman'],[ 'red crisis', 54, 'surreal', 'stoneyhedge'],[ 'orange', 69, 'surreal', 'stoneyhedge']]
pop = [['regret', 183, 'pop', 'kenny'],[ 'melancholy', 222, 'pop', 'gaster'],[ 'human music',106 , 'pop', 'stoneyhedge'],['popular song', 211, 'pop', 'kenny'],['grape gang', 214, 'pop', 'gaster']]

option = input("Would you like to see all the songs in the library? (y/n)")
if option.lower() == 'y':
    print('The library has: ')
    for x in range(0, 6):
        print(rock[x][0])
        songtime = rock[x][1]
        songtimeR = songtime % 60
        songtimeF = songtime // 60
        if songtimeR < 10:
            songtimeR *= 10
        print(str(songtimeF) + ':' + str(songtimeR))
        print('By:', rock[x][3])
        time.sleep(0.3)
    for x in range(0, 6):
        print(surreal[x][0])
        songtime = surreal[x][1]
        songtimeR = songtime % 60
        songtimeF = songtime // 60
        if songtimeR < 10:
            songtimeR *= 10
        print(str(songtimeF) + ':' + str(songtimeR))
        print('By:', surreal[x][3])
        time.sleep(0.3)
    for x in range(0, 4):
        print(pop[x][0])
        songtime = pop[x][1]
        songtimeR = songtime % 60
        songtimeF = songtime // 60
        if songtimeR < 10:
            songtimeR *= 10
        print(str(songtimeF) + ':' + str(songtimeR))
        print('By:', pop[x][3])
        time.sleep(0.3)

option = input("Would you like to generate a playlist (y/n)\n")
if option.lower() == 'y':
    length = int(input('Whats the longest length you want your playlist to be?(minutes)\n'))
    length = length*60-60
    SelectedGenre = input("What genre would you like the songs to be in?\n")
    while SelectedGenre != 'pop' and SelectedGenre != 'Pop' and SelectedGenre != 'surreal' and SelectedGenre != 'Surreal' and SelectedGenre != 'rock' and SelectedGenre != 'Rock':
        SelectedGenre = input('Sorry, either that genre isn\'t available or you\'ve typed it wrong\n')
    cycles = 6
    playlist = []
    if SelectedGenre.lower() == 'rock':
        limit = 6
        while songlength < length and cycles != 0:
            song = random.randint(0, limit)
            longness = rock[song][1]
            songlength += longness
            cycles = cycles-1
            playlist.append(rock[song][0])
            playlist.append(rock[song][1])
            rock.pop(song)
            limit -= 1
    if SelectedGenre.lower() == 'surreal':
        limit = 6
        while songlength < length and cycles != 0:
            song = random.randint(0, limit)
            longness = surreal[song][1]
            songlength += longness
            cycles = cycles-1
            playlist.append(surreal[song][0])
            playlist.append(surreal[song][1])
            surreal.pop(song)
            limit -= 1
    if SelectedGenre.lower() == 'pop':
        limit = 4
        while songlength < length and cycles != 0:
            song = random.randint(0, limit)
            longness = pop[song][1]
            songlength += longness
            cycles = cycles-1
            playlist.append(pop[song][0])
            playlist.append(pop[song][1])
            pop.pop(song)
            limit -= 1

    longitude = len(playlist)
    print('Your playlist has: ')
    for x in range(0,longitude,2):
        print(playlist[x])
        songtime = playlist[x+1]
        songtimeR = songtime % 60
        songtimeF = songtime // 60
        if songtimeR < 10:
            songtimeR *= 10
        print(str(songtimeF) +':'+ str(songtimeR))

