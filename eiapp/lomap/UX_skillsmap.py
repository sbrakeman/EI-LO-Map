# CSC 111
# Author: Tani Somolu
# PLaying with matplotlib and trying to generate some sort of graph

# matplotlib imported to be used
#import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

import random
import seaborn
import plotly.plotly as py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

seaborn.set()

LO1 = "Reading: Main Idea: I am able to identify and explain the main purpose of a text written for a general audience"
LO2 = "Reading: Key Vocab: I am able to identify key vocabulary and use context clues to determine the meaning of vocabulary"
LO3 = "Reading: Supporting Evidence: I am able to identify evidence that supports the main purpose of the text"
LO4 = "Listening: Main Idea: I am able to identify the main idea from a speech that I listen to"
LO5 = "Listening: Key Vocab: I am able to identify key vocabulary and use context clues to determine the meaning of vocabulary"
LO6 = "Listening: Supporting Evidence: I am able to identify supporting evidence that supports the main purpose of the speech"
LO7 = "Speaking: Clarity: I am able to speak clearly and fluently with correct pronunciation and tone"
LO8 = "Speaking: Coherency: I am able to articulate my thoughts and ideas coherently using appropriate vocabulary"
LO9 = "Writing: Main Idea: I can clearly construct a main idea"
LO10 = "Writing: Structure and Organization: I am able to write a connected text that conveys a main idea"
LO11 = "Writing: Sentence Structure: I am able to use varied sentence structures"
LO12 = "Writing: Grammar: I am able to use correct grammar, syntax, and punctuation in my writing"
LO13 = "Writing: Voice: I am able to use appropriate style and tone in my writing to engage the readers"
LO14 = "Growth: Vocab: I am able to identify words that I do not know, and define these words on my own"
LO15 = "Growth: Research: I am able to research events referenced in texts to contextualize articles"
LO16 = "Growth: Opinions: I am able to express my own opinions about a text"
LO17 = "Digital literacy: Digital Proficiency: I can use the appropriate computer applications and tools to document,organize and present my ideas"
LO18 = "Digital Literacy: Information and Access: I can use web browsers, search engines and the internet to find and retrieve high-quality, relevant information to support my learning."

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

#py.sign_in("tsomolu", "9pXQsAKOef1QdqHCC9BW")

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Fs_bF37oMIR7j71GTgVh_-V1v50s_lcMt0KwOk868qY/edit#gid=619321339").sheet1

pp = pprint.PrettyPrinter()
values_lists = sheet.col_values(3)
#print(values_lists)
#lo_list = pp.pprint(values_lists)

learning_outcomes = [LO1,LO2,LO3,LO4,LO5,LO6,LO7,LO8,LO9,LO10,LO11,LO12,LO13,LO14,LO15,LO16,LO17,LO18]

#LO = "reading: main idea"

LO1,LO2,LO3,LO4,LO5,LO6,LO7,LO8,LO9,LO10,LO11,LO12,LO13,LO14,LO15,LO16,LO17,LO18 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

for LO in values_lists:
    #print(lo)
    LO = LO.lower()
    
    if "reading: main idea" in LO:
        LO1 = LO1 + 1
    elif "reading: key vocab" in LO:
        LO2 = LO2 + 1
    elif "reading: supporting evidence" in LO:
        LO3 = LO3 + 1
    elif "listening: main idea" in LO:
        LO4 = LO4 + 1
    elif "listening: key vocab" in LO:
        LO5 = LO5 + 1
    elif "listening: supporting evidence" in LO:
        LO6 = LO6 + 1
    elif "speaking: clarity" in LO:
        LO7 = LO7 + 1
    elif "speaking: coheency" in LO:
        LO8 = LO8 + 1
    elif "writing: main idea" in LO:
        LO9 = LO9 + 1
    elif "writing: structure and organization" in LO:
        LO10 = LO10 + 1
    elif "writing: sentence structure" in LO:
        LO11 = LO11 + 1
    elif "writing: grammar" in LO:
        LO12 = LO12 + 1
    elif "writing: voice" in LO:
        LO13 = LO13 + 1
    elif "growth: vocab" in LO:
        LO14 = LO14 + 1
    elif "growth: research" in LO:
        LO15 = LO15 + 1
    elif "growth: opinions" in LO:
        LO16 = LO16 + 1
    elif "digital literacy: digital proficiency" in LO:
        LO17 = LO17 + 1
    elif "digital literacy: information and access" in LO:
        LO18 = LO18 + 1
        

#clusters = np.arange((len(Learning_Outcomes)/3))
bar_lefts = 0.3
width = 0.3

b = []
d = []
e = []


b_value = random.randint(25,50)
b.append(b_value)
d_value = random.randint(25,50)
d.append(d_value)
e_value = random.randint(25,50)
e.append(e_value)

fig = plt.figure(facecolor = "gainsboro", figsize = (6,4))

ax1 = fig.add_subplot(131)
ax1.set_facecolor("gainsboro")
plt.xlabel("Comprehension(input)")
plt.ylabel("Learning Outcome Frequencies")

ax2 = fig.add_subplot(132, sharey = ax1)
ax2.set_facecolor("gainsboro")
plt.xlabel("Communication(output)")

ax3 = fig.add_subplot(133, sharey = ax1)
ax3.set_facecolor("gainsboro")
plt.xlabel("Growth")

# ec short for edge color
# for cluster 1
ax1.bar(bar_lefts, LO1, width, color = "lime", ec="k", linewidth = 1.5)
ax1.bar(bar_lefts*2,LO2, width, color = "lime", ec ="k", linewidth = 1.5)
ax1.bar(bar_lefts*3, LO3, width, color = "lime", ec="k", linewidth = 1.5)

ax1.bar(bar_lefts*4, LO4, width, color = "darkgreen", ec="k", linewidth = 1.5)
ax1.bar(bar_lefts*5, LO5, width, color = "darkgreen", ec="k", linewidth = 1.5)
ax1.bar(bar_lefts*6, LO6 ,width, color = "darkgreen", ec="k", linewidth = 1.5)

# for cluster 2
ax2.bar(bar_lefts, LO7, width, color = "darkblue", ec="k", linewidth = 1.5)
ax2.bar(bar_lefts*2,LO8, width, color = "darkblue", ec ="k", linewidth = 1.5)
ax2.bar(bar_lefts*3, LO9, width, color = "darkblue", ec="k", linewidth = 1.5)

ax2.bar(bar_lefts*4, LO10, width, color = "aqua", ec="k", linewidth = 1.5)
ax2.bar(bar_lefts*5, LO11, width, color = "aqua", ec="k", linewidth = 1.5)
ax2.bar(bar_lefts*6, LO12 ,width, color = "aqua", ec="k", linewidth = 1.5)
ax2.bar(bar_lefts*7, LO13, width, color = "aqua", ec = "k", linewidth = 1.5)

# for cluster 3
ax3.bar(bar_lefts, LO14, width, color = "r", ec="k", linewidth = 1.5)
ax3.bar(bar_lefts*2,LO15, width, color = "r", ec ="k", linewidth = 1.5)
ax3.bar(bar_lefts*3, LO16, width, color = "r", ec="k", linewidth = 1.5)

ax3.bar(bar_lefts*4, LO17, width, color = "lightcoral", ec="k", linewidth = 1.5)
ax3.bar(bar_lefts*5, LO18, width, color = "lightcoral", ec="k", linewidth = 1.5)

#print(LO1,LO2,LO3,LO4,LO5,LO6,LO7,LO8,LO9,LO10,LO11,LO12,LO13,LO14,LO15,LO16,LO17,LO18)

for ax in [ax1,ax2,ax3]:
    ax.set_xticks([])
    ax.set_yticks(np.arange(0,10,1))
    ax.grid("off")
for ax in [ax2,ax3]:
    plt.setp(ax.get_yticklabels(), visible= False)

#line1 = plt.plot([],[],color="lime")

#fig.legend([line1],["Reading","Listening","Speaking","Writing","Growth","Digital Literacy"],"upper right")
#plt.legend(["Reading\nListening","Speaking\nWriting","Growth\nDigital Literacy"])
plt.show()
#plot_url = py.plot_mpl(fig)



            



