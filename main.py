from datetime import date
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, tasks
from itertools import cycle
import nextcord
import asyncio
import sqlite3
import random
import datetime

#adding space in discord
space1 = "‎ ‎ ‎  ‎  ‎  ‎ ‎ ‎ ‎ ‎ ‎ "
space = "‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎  ‎  ‎ ‎ ‎ ‎ ‎ ‎ "

mydb = sqlite3.connect("database.db")

mycursor = mydb.cursor()


guild = ["your guild Id goes here"]
token = 'your token'
State = cycle(["/help", "El Za3em 👑"])

bot = commands.Bot(command_prefix='/',status=nextcord.Status.idle, help_command=None)
so = 0

today  = date.today ()
dayNow  = today .strftime("%d")
monthNow = today .strftime("%m")
# yearNow = today .strftime("%Y")
currentdate=  f"{dayNow}/{monthNow}"



@tasks.loop(seconds=3)
async def change_status():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=next(State)))


@bot.event
async def on_ready():
    change_status.start()
    channel = bot.get_channel("channel id")
    print(f"s                      El Za3emV2.0 Connected :)")
    



@bot.slash_command(name='To-do', description="  to know what to do today  ", guild_ids=guild)
async def sendMessage(ctx: Interaction ):
    VidTable=""
    SheetTable=""
    author=""
    id = ctx.user.id
    if id == "user id " :
        author=""
        VidTable=""
        SheetTable=""
    elif  id == "user_id" :
        author="user id"
        VidTable="  "
        SheetTable="  "
    elif  id == "user_id" :
        author="user id"
        VidTable="  "
        SheetTable="  "
    elif  id == "user_id" :
        author="user id"
        VidTable="  "
        SheetTable="  "
    elif  id == "user_id" :
        author="user id"
        VidTable="  "
        SheetTable="  "
    elif  id == "user_id" :
        author="user id"
        VidTable="  "
        SheetTable="  "
    elif  id == "user_id" :
        author="user id"
        VidTable="  "
        SheetTable="  "
    elif  id == "user_id" :
        author="user id"
        VidTable=" 2 "
        SheetTable=" 2 "
    embed = nextcord.Embed(
    title=" TO_DO  ✅",
    description=f" dont be lazy {author} 😊",
    colour=0xf99441)
    
    mycursor.execute(f"SELECT * FROM {VidTable}  ORDER BY videos LIMIT 1")
    for x in mycursor:
        x=str(x)
        brac=str(x).find("(")
        comma=str(x).find(",")
        embed.add_field(name=" videos 🎥 ", value=f"{x[brac+1:comma]}", inline=True)

    mycursor.execute(f"SELECT * FROM {SheetTable} ORDER BY Sheets  LIMIT 1")
    for y in mycursor:
        y=str(y)
        brac=str(y).find("(")
        comma=str(y).find(",")
        embed.add_field(name=" sheets 📒 ", value=f"{y[brac+1:comma]} ", inline=True)
    await ctx.send(embed=embed)


@bot.slash_command(name='all_course_data', description="to show all data course (videos & sheets)", guild_ids=guild)
async def sendMessage(ctx: Interaction ):
    VideosList=[]
    SheetsList=[]
    embed = nextcord.Embed(
    title="DataBase  📅",
    colour=0xf99441)
    mycursor.execute(f"SELECT * FROM CourseDataVideos ORDER BY Videos ASC ")
    for x in mycursor:
        x=str(x)
        brac=str(x).find("(")
        comma=str(x).find(",")
        if x[brac+1:comma] != "None":
            VideosList.append(x[brac+1:comma])

    mycursor.execute(f"SELECT * FROM CourseDataSheets ORDER BY Sheets ASC")
    for x in mycursor:
        x=str(x)
        brac=str(x).find("(")
        comma=str(x).find(",")
        if x[brac+1:comma] != "None":
            SheetsList.append(x[brac+1:comma])
    stringx=str(VideosList)
    brac=stringx.find("[")
    brac2=stringx.find("]")
    stringxmod = str(stringx[brac+1:brac2])
    stringxmod=stringxmod.replace(',','\n') 
    stringxmod=stringxmod.replace("'"," ")
    embed.add_field(name="Videos", value=f"{stringxmod} \n ", inline=True)

    stringxa=str(SheetsList)
    brac=stringxa.find("[")
    brac2=stringxa.find("]")
    stringxmoda = str(stringxa[brac+1:brac2])
    stringxmoda=stringxmoda.replace(',','\n')
    stringxmoda=stringxmoda.replace("'"," ")

    embed.add_field(name="Sheets", value=f"{stringxmoda} ", inline=True)
    await ctx.send(embed=embed)

@bot.slash_command(name='finshed', description="   to add dinshed data into completed table in DB   ", guild_ids=guild)
async def sendMessage(ctx: Interaction,videonumber: int = SlashOption(description=" Enter finshed videonumber ", min_value=1, max_value=65,default=77,required=False),sheetnumber: int = SlashOption(description=" Enter Finshed sheetnumber", min_value=1, max_value=5,default=77,required=False)):
    embed = nextcord.Embed(
    colour=0xf99441)
    state=2
    VidTable=""
    SheetTable=""
    RemVidTable=""
    RemsheetTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        VidTable=""
        SheetTable=""
        RemVidTable=""
        RemsheetTable=""
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" 2"
        VidTable=" 2 "
        SheetTable=" 2 "
        RemVidTable=" 2 "
        RemsheetTable=" 2 "

    embed.add_field(name=f" hi {author} 👋", value=" you r doin great ", inline=False)
    if videonumber != 77 :
        mycursor.execute(f"SELECT * FROM {VidTable} ORDER BY videos ASC ")
        for x in mycursor :
            x=str(x)
            brac=str(x).find("(")
            comma=str(x).find(",")
            if x[brac+1:comma] == str(videonumber):
                embed.add_field(name="careful", value=f" u finshed this video before {videonumber}", inline=False)
                state=4
        if state!=4 :
            mycursor.execute(f"INSERT INTO {VidTable}  VALUES({videonumber})")
            mycursor.execute(f"DELETE FROM {RemVidTable} WHERE videos = {videonumber}")
            state=0
            mydb.commit()
            embed.add_field(name=" nice ", value=f"u finshed video number :arrow_left:  {videonumber}", inline=False)

    if sheetnumber != 77 :
        mycursor.execute(f"SELECT *  FROM {SheetTable} ORDER BY Sheets ASC ")
        for x in mycursor :
            x=str(x)
            brac=str(x).find("(")
            comma=str(x).find(",")
            if x[brac+1:comma] == str(sheetnumber):
                embed.add_field(name="careful", value=f"   u finshed this sheet before {videonumber}", inline=False)
                state=5
        if state  != 5 :
            mycursor.execute(f"INSERT INTO {SheetTable}  VALUES({sheetnumber})")
            mycursor.execute(f"DELETE FROM {RemsheetTable} WHERE Sheets = {sheetnumber}")
            state=1
            mydb.commit()
            embed.add_field(name="nice", value=f"u finshed sheet number :arrow_left: {sheetnumber}", inline=False)


    if state == 2:
        embed.add_field(name=" Error ", value=f"u must choose at least one option ", inline=False)
    await ctx.send(embed=embed)

@bot.slash_command(name='unfinsh', description=" to bring back video or sheet  ", guild_ids=guild)
async def sendMessage(ctx: Interaction,videonumber: int = SlashOption(description=" Enter unfinshed video number", min_value=1, max_value=65,default=77,required=False),sheetnumber: int = SlashOption(description=" enter unfinshed sheet number   ", min_value=1, max_value=5,default=77,required=False)):
    embed = nextcord.Embed(
    colour=0xf99441)
    state=2
    VidTable=""
    SheetTable=""
    RemVidTable=""
    RemsheetTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        VidTable=""
        SheetTable=""
        RemVidTable=""
        RemsheetTable=""
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" 2"
        VidTable=" 2 "
        SheetTable=" 2 "
        RemVidTable=" 2 "
        RemsheetTable=" 2 "
        
    embed.add_field(name=f"hi {author} 👋", value=" u r doin great ", inline=False)
    if videonumber != 77 :
        mycursor.execute(f"SELECT * FROM {VidTable} ORDER BY videos ")
        for x in mycursor :
            x=str(x)
            brac=str(x).find("(")
            comma=str(x).find(",")
            if x[brac+1:comma] == str(videonumber):
                state=4
        if state==4:
            mycursor.execute(f"DELETE FROM {VidTable} WHERE videos = {videonumber}")
            mycursor.execute(f"INSERT INTO {RemVidTable}   VALUES({videonumber})")
            mydb.commit()
            embed.add_field(name="hi", value=f"  u returned this video number {videonumber}", inline=False)
        else :
                embed.add_field(name="Error", value=f"  u r not finshed this video yet   {videonumber}", inline=False)
        state=0

    if sheetnumber != 77 :
        mycursor.execute(f"SELECT * FROM {SheetTable} ")
        for x in mycursor :
            x=str(x)
            brac=str(x).find("(")
            comma=str(x).find(",")
            if x[brac+1:comma] == str(sheetnumber):
                state=5
        if state == 5:
            mycursor.execute(f"DELETE FROM {SheetTable} WHERE Sheets = {sheetnumber}")
            mycursor.execute(f"INSERT INTO {RemsheetTable}  VALUES({sheetnumber})")
            mydb.commit()
            embed.add_field(name="hi", value=f"u returned this sheet number {sheetnumber}", inline=False)
        else :
            embed.add_field(name=" Error", value=f"   u r not finshed this sheet yet   {sheetnumber}", inline=False)
        state=1

    if state == 2:
        embed.add_field(name=" ERROR ", value=f" u must choose one option at least ", inline=False)

    await ctx.send(embed=embed)
    


@bot.slash_command(name='see_wht_u_finshed', description="to see videos and sheets u finshed ", guild_ids=guild)
async def sendMessage(ctx: Interaction):
    completed_list=[]
    ycompleted_list=[]
    embed = nextcord.Embed(
    colour=0xf99441)
    VidTable=""
    SheetTable=""
    RemVidTable=""
    RemsheetTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        VidTable=""
        SheetTable=""
        RemVidTable=""
        RemsheetTable=""
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" 2"
        VidTable=" 2 "
        SheetTable=" 2 "
        RemVidTable=" 2 "
        RemsheetTable=" 2 "
    
    mycursor.execute(f"SELECT * FROM {VidTable} ORDER BY videos ASC")
    for x in mycursor :
        if x != None :
            completed_list.append(x)
    mycursor.execute(f"SELECT * FROM {SheetTable} ORDER BY Sheets ASC")
    for y in mycursor :
        if y != None :
            ycompleted_list.append(y)
    
    stringxa=str(completed_list)
    brac=stringxa.find("[")
    brac2=stringxa.find("]")
    stringxmoda = str(stringxa[brac+1:brac2])
    stringxmoda=stringxmoda.replace(',',' ')
    stringxmoda=stringxmoda.replace("'"," ")
    stringxmoda=stringxmoda.replace(")"," ")
    stringxmoda=stringxmoda.replace("("," \n")
    embed.add_field(name=f" hi {author} 👋", value="your progress", inline=False)
    embed.add_field(name="Videos", value=f"{stringxmoda}", inline=True)
    stringxaa=str(ycompleted_list)
    brac=stringxaa.find("[")
    brac2=stringxaa.find("]")
    stringxmodaa = str(stringxaa[brac+1:brac2])
    stringxmodaa=stringxmodaa.replace(',',' ')
    stringxmodaa=stringxmodaa.replace("'"," ")
    stringxmodaa=stringxmodaa.replace(")"," ")
    stringxmodaa=stringxmodaa.replace("("," \n")
    embed.add_field(name="Sheets", value=f"{stringxmodaa}", inline=True)
    await ctx.send(embed=embed)
    

@bot.slash_command(name='seee_wht_remanning', description=" to see remmanning content in the course", guild_ids=guild)
async def sendMessage(ctx: Interaction):
    Remanning_list=[]
    yRemanning_list=[]
    embed = nextcord.Embed(
    colour=0xf99441)
    VidTable=""
    SheetTable=""
    RemVidTable=""
    RemsheetTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        VidTable=""
        SheetTable=""
        RemVidTable=""
        RemsheetTable=""
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" "
        VidTable="  "
        SheetTable="  "
        RemVidTable="  "
        RemsheetTable="  "
    elif  id == "user_id" :
        author=" 2"
        VidTable=" 2 "
        SheetTable=" 2 "
        RemVidTable=" 2 "
        RemsheetTable=" 2 "
    
    mycursor.execute(f"SELECT * FROM {RemVidTable} ORDER BY videos ASC ")
    for x in mycursor :
        if x != None :
            Remanning_list.append(x)

    mycursor.execute(f"SELECT * FROM {RemsheetTable} ORDER BY Sheets ASC ")
    for y in mycursor :
        if y != None :
            yRemanning_list.append(y)

    stringxa=str(Remanning_list)
    brac=stringxa.find("[")
    brac2=stringxa.find("]")
    stringxmoda = str(stringxa[brac+1:brac2])
    stringxmoda=stringxmoda.replace(',',' ')
    stringxmoda=stringxmoda.replace("'"," ")
    stringxmoda=stringxmoda.replace(")"," ")
    stringxmoda=stringxmoda.replace("("," \n")
    embed.add_field(name=f"hi {author} 👋", value=" the remanning content ", inline=False)
    embed.add_field(name="Videos", value=f"{stringxmoda}", inline=True)
    
    stringxaa=str(yRemanning_list)
    brac=stringxaa.find("[")
    brac2=stringxaa.find("]")
    stringxmodaa = str(stringxaa[brac+1:brac2])
    stringxmodaa=stringxmodaa.replace(',',' ')
    stringxmodaa=stringxmodaa.replace("'"," ")
    stringxmodaa=stringxmodaa.replace(")"," ")
    stringxmodaa=stringxmodaa.replace("("," \n")
    embed.add_field(name="Sheets", value=f"{stringxmodaa}", inline=True)

    await ctx.send(embed=embed)




@bot.slash_command(name='add_note', description=" to  add note  ", guild_ids=guild)
async def sendMessage(ctx: Interaction,note:str= SlashOption(description="  add note content  " ,required=True)):
    embed = nextcord.Embed(
    colour=0xf99441)
    NoteTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"

    
    mycursor.execute(f"INSERT INTO {NoteTable}(Notes) VALUES('{note}')")
    mydb.commit()
    embed.add_field(name=f" hi {author} 👋", value=" u added a note", inline=False)

    await ctx.send(embed=embed)

@bot.slash_command(name='delete_note', description=" to delete note ", guild_ids=guild)
async def sendMessage(ctx: Interaction,ids:int= SlashOption(description="delete note with its id number" ,required=True)):
    embed = nextcord.Embed(
    colour=0xf99441)
    NoteTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" 2"
        NoteTable="Notes"

    x=4

    print(ids)
    mycursor.execute(f"SELECT count(*) FROM {NoteTable} WHERE ID = {ids} ")
    for x in mycursor :
        x=str(x)
        brac=x.find("(")
        comma=x.find(",")
        x=int(x[brac+1:comma])
        print(x)
    
    if x != 0 :
        mycursor.execute(f"DELETE FROM {NoteTable} WHERE ID = {ids}")
        mydb.commit()
        embed.add_field(name=f" hi {author} 👋", value=" u deleted a note", inline=False)
    else :
        embed.add_field(name=f" hi {author} 👋", value=" this note does not exsist ", inline=False)

    await ctx.send(embed=embed)

@bot.slash_command(name='show_notes', description=" to show your notes with note id ", guild_ids=guild)
async def sendMessage(ctx: Interaction):
    idس=[]
    note=[]

    embed = nextcord.Embed(
    colour=0xf99441)
    NoteTable=""
    author=""
    id = ctx.user.id
    if id == "user_id" :
        author=""
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" "
        NoteTable="Notes"
    elif  id == "user_id" :
        author=" 2"
        NoteTable="Notes"

    x= 4
    mycursor.execute(f"SELECT count(*) FROM {NoteTable} ")
    for x in mycursor :
        x=str(x)
        brac=x.find("(")
        comma=x.find(",")
        x=int(x[brac+1:comma])
        if x == 0 :
            embed.add_field(name=f" hi {author} 👋", value="you dont have a note"  , inline=False)
    if x != 0 :
        mycursor.execute(f"SELECT * FROM {NoteTable} ORDER BY ID ASC")
        embed.add_field(name=f" hi {author} 👋", value="your notes :"  , inline=False)
        embed.add_field(name=f"ID{space1}DATE", value="\u200b", inline=False)
        for x ,y in mycursor :
            idس.append(y)
            note.append(x)
            embed.add_field(name="\u200b", value=f"{y}{space}{x}", inline=False)

    await ctx.send(embed=embed)

@bot.slash_command(name="remind", description="start the reminder", guild_ids=guild)
async def remind(ctx: Interaction):
    id = ctx.user.id
    channel = bot.get_channel(1127543418336325662)

    if id == "user_id" :
        while True :
            zeronote=[]
            notzeronote=[]
            notzeronotenumber=[]
            embed = nextcord.Embed(
            colour=0xf99441)
            ids = ["user_id","user_id","user_id","user_id","user_id","user_id","user_id","user_id"]
            NoteTables = ["Notes","Notes","Notes","Notes","Notes","Notes","Notes","Notes"]
            

            
            loop_time = 120
            now = datetime.datetime.now()
            then = now + datetime.timedelta(minutes=loop_time)
            global wait_time
            wait_time = (then-now).total_seconds()
            await asyncio.sleep(wait_time)

            x= 4
            embed.add_field(name=f" Notes 📒 ", value="\u200b"  , inline=False)
            for (au,id) in zip(NoteTables, ids) :
                mycursor.execute(f"""
                                SELECT count(Notes) as s
                                FROM {au} 
                                """)
                for x in mycursor :
                    x=str(x)
                    brac=x.find("(")
                    comma=x.find(",")
                    x=int(x[brac+1:comma])
                    if x == 0 :
                        zid = f"<@"+str(id)+">"
                        zeronote.append(zid)
                    else :
                        zid = f"<@"+str(id)+">"
                        notzeronote.append(zid)
                        notzeronotenumber.append(x)

            embed.add_field(name=f" u have notes ", value=f"\u200b"  , inline=False)
            embed.add_field(name=f"User{space1}{space1}{space1}{space1}Notes Numbers", value="\u200b", inline=False)
            for x in range(len(notzeronote)) :
                embed.add_field(name="\u200b", value=f"{notzeronote[x]}{space}{space}{space}{space}{notzeronotenumber[x]}", inline=False)



            embed.add_field(name=f"\u200b", value=f"\u200b"  , inline=False)
            embed.add_field(name=f"   u dont have notes add one    ", value=f"{zeronote}"  , inline=False)
            embed.add_field(name=f"\u200b", value=f"\u200b"  , inline=False)
            #add motivational quotes
            x= ["","","","    " ,"   ","  ","     ","       "]
            # print(random.choice(x)
            
            await channel.send(f"{random.choice(x)}\n @everyone")

    else : 
        channel = bot.get_channel(1127543418336325662)
        await channel.send("U Dont have a Permission")

bot.run(token)
