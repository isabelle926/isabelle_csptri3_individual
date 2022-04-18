def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("Welcome! If you'd like to learn more about Indonesia, you've come to the right place. Below are a few areas you can explore: ") # user input prompt


def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu

def sumatra():
  print("Sumatra is the world’s sixth largest island and the largest one located entirely within Indonesian territory. The island covers an area of 473,481 square km. It has been divided into 10 administrative provinces. Its population has been estimated to be around 50,180,000 people. Medan is the largest city on the island. Sumatra is part of the Sunda Islands`and is separated from the Malay Peninsula by the narrow Strait of Malacca. The island is separated from Java by the Sunda Strait. The landscape of Sumatra comprises of mountains, active volcanoes, massive plains, mangroves, and large rivers. The equator passes through the central part of Sumatra. Although Sumatra has a great diversity of wildlife, most of its flora and fauna are threatened today. Large swathes of the rainforest here have been cleared for human needs. Coffee plantations have consumed much of the forest land on the island.")

def sulawesi():
  print("With an area of 180,680.7 square km, Sulawesi is the world’s 11th largest island. Sulawesi has a population of 18,455,058 individuals. Politically, it is part of Indonesia and is divided into six administrative units. Sulawesi is located to the east of Borneo from which it is separated by the Strait of Makassar. Geographically, the island can be divided into four peninsulas that are separated by three gulfs. Tall mountains exist in the central part of Sulawesi that makes commuting between the peninsulas a difficult task. The island is famous for natural wealth. Eight Indonesian nations parks including four marine parks are located here. Agriculture and fishing are the main economic activities in Sulawesi.")
  
def guinea():
  print("The island of New Guinea is divided between two nations, Papua New Guinea and Indonesia. While the former lies entirely on the island, the latter has only two provinces as part of the island. Western New Guinea is the only part of Indonesia that is located in Oceania. Some nearby islands are also a part of this territory. Most of the region is inhabited by various tribes and is covered by dense rainforests. Jayapura is the largest urban settlement in the region. Western New Guinea covers an area of 420,540 square km and has a population of around 4,363,869. Agriculture, fishing, mining, and oil production are the major industries in the region.")

def sunda():
  print("The Lesser Sunda Islands are a group of islands located to the north of Australia where they are part of the Sunda Volcanic Arc in the Java Sea. Many of the islands in this group are top tourist destinations like Bali and Lombok. Most of these islands are politically a part of Indonesia. Three administrative provinces of Indonesia are located here. Many of the islands here are separated from their neighbors by deep oceanic trenches that have encouraged the evolution of endemic species independently on these islands. The Komodo dragon is one such species found here. Tourism, agriculture, and logging are the top economic activities in this Indonesian region. Sadly, the natural ecosystems in the Lesser Sunda Islands are today highly threatened due to the indiscriminate clearing of forests for development and agriculture.")

def maluku():
  print("The Maluku Islands is an Indonesian archipelago of around 1027 islands located in the Banda Sea. Sulawesi and New Guinea are located to the west and east of the archipelago, respectively. It is divided into two administrative provinces and hosts a population of around 2,844,131 residents. Ambon is the largest island in the archipelago in terms of population. Although the total area of the Maluku Islands is 850,000 square km, over 90% of it is sea. The islands were famous since the ancient times since spices like mace, cloves, and nutmeg originated here and attracted the Europeans to the region. Today, the economy of the Maluku Islands is dependent mainly on cultivation, fishing, and logging.")

def kalimantan():
  print("The Indonesian part of Borneo is called Kalimantan. It has been divided into five administrative provinces and has a total area of 544,150.07 square km which represents about 73% of the area of the island. Kalimantan shares the island with a Malaysian state and the country of Brunei. Kalimantan has 15,894,524 residents. Kalimantan is sparsely populated with large areas in the interior being covered by vast tracts of rainforest with a great diversity of flora and fauna. Banjarmasin is the biggest city in this Kalimantan while Balikpapan is a hub of international oil and mining industries.")

def java():
  print("Java, the world’s most populous island, is a part of Indonesia. The island hosts about 145 million people that represent about 56.7% of the Indonesian population. Java is also home to Jakarta, the capital city of the country. Formed by volcanism, Java is Indonesia’s fifth largest island by area. It has an area of 138,800 square km. Java served as the venue of most of Indonesia’s major historical events. It is the political, economic, and cultural hub of the nation. It served as the center of major Hindu, Buddhist, and Islamic empires. Java is home to four of the eight World Heritage Sites of Indonesia. It comprises of 4 administrative provinces and two special regions. It is the most developed Indonesian island.")


geography = {
  1: {"display":"Sumatra",
     "exec":sumatra,
     "type":"func"},
  2: {"display":"Sulawesi",
     "exec":sulawesi,
     "type":"func"},
  3: {"display":"Western New Guinea",
     "exec":guinea,
     "type":"func"},
  4: {"display":"Lesser Sunda Islands",
     "exec":sunda,
     "type":"func"},
  5: {"display":"Maluku Islands",
     "exec":maluku,
     "type":"func"},
  6: {"display":"Kalimantan",
     "exec":kalimantan,
     "type":"func"},
  7: {"display":"Java",
     "exec":java,
     "type":"func"},
  8: {"display":"Quit Program",
        "exec":quit,
        "type":"func"}
}
def famousFood():
  InfoDb = [{
    "Species": "African black-footed penguin",
    "Conservation Status": "Endangered",
    "Scientific Name": "Spheniscus demersus",
    "Location": ["South Africa", "Namibia"]
}, {
    "Species": "Northern rockhopper penguin",
    "Conservation Status": "Endangered",
    "Scientific Name": "Eudyptes moseleyi",
    "Location": ["Tristan da Cunha", "Gough Island"],
    "Family": "Spheniscidae",
    "Fun Facts": ["One of the smallest crested penguin", "Around 5 lbs", "Are scrappy and pugnacious"]
}, {
    "Species": "King penguin",
    "Conservation Status": "Least Concern",
    "Scientific Name": "Aptenodytes patagonicus",
    "Location": ["Falkland Islands"],
    "Family": "Spheniscidae",
    "Fun Facts": ["Fuzzy brown chicks", "Look similar to emperor penguins", "Around 3 ft tall"]
}, {
    "Species": "Adélie penguin",
    "Conservation Status": "Near Threatened",
    "Scientific Name": "Pygoscelis adeliae",
    "Location": ["Antartica"],
    "Family": "Spheniscidae",
    "Fun Facts": ["Attack with their flippers", "Characteristic 'tuxedo' look", "Smallest penguin in Antarctica"]
}]
food = {
  1: {"display":"Famous dishes",
     "exec":famousFood,
     "type":"func"},
  2: {"display":"History",
     "exec":foodHistory,
     "type":"func"},
  3: {"display":"Recipes",
     "exec":recipes,
     "type":"dict"},
  4: {"display":"Quit Program",
      "exec":quit,
      "type":"func"}
}

mainMenu = {
    1: {"display":"Geography",
        "exec":geography,
        "type":"dict"},
    2: {"display":"Food",
        "exec":food,
        "type":"dict"},
    3: {"display":"Language",
        "exec":language,
        "type":"dict"},
    4: {"display":"Culture",
        "exec":culture,
        "type":"dict"},
    5: {"display":"Clothing",
        "exec":clothing,
        "type":"dict"},
    6: {"display":"Quit Program",
        "exec":quit,
        "type":"func"}
}