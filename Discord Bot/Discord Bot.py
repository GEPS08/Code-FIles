import os
import discord
from discord import app_commands
from datetime import datetime
from discord.ext.tasks import loop
from discord.ext import tasks
import numpy as np
from typing import List

client = discord.Client(intents=discord.Intents.all())

tree = app_commands.CommandTree(client)



@tasks.loop(hours=2.0)
async def reminder():
    dailytime = datetime.now().day + 1
    projecttime = datetime.now().day + 3
    bigprojecttime = datetime.now().day + 7
    bigtime = datetime.now().day + 10

    print ()

    ii = 0
    for i in currentHW:

        duedateday = currentHW[ii][2]
        hwsize = currentHW[ii][3]
        duedateday = duedateday.split('/')
        sendMessage = str(currentHW[ii])
        sendMessage = sendMessage.replace('[', '')
        sendMessage = sendMessage.replace(']', '')
        sendMessage = sendMessage.replace("'", '')

        if hwsize == 'daily':
            if int(duedateday[1]) == dailytime:
                print(sendMessage + ' is due tomorrow')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due tomorrow')

        if hwsize == 'project':
            if int(duedateday[1]) == projecttime:
                print(sendMessage + ' is due in three days')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due in three days')

            elif int(duedateday[1]) == dailytime:
                print(sendMessage + ' is due tomorrow')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due tomorrow')

        if hwsize == 'bigProject':
            if int(duedateday[1]) == bigprojecttime:
                print(sendMessage + ' is due in seven days')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due in seven days')

            elif int(duedateday[1]) == projecttime:
                print(sendMessage + ' is due in three days')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due in three days')

            elif int(duedateday[1]) == dailytime:
                print(sendMessage + ' is due tomorrow')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due tomorrow')

        if hwsize == 'big':
            if int(duedateday[1]) == bigtime:
                print(sendMessage + ' is due in ten days')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due in ten days')

            elif int(duedateday[1]) == bigprojecttime:
                print(sendMessage + ' is due in seven days')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due in seven days')

            elif int(duedateday[1]) == projecttime:
                print(sendMessage + ' is due in three days')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due in three days')

            elif int(duedateday[1]) == dailytime:
                print(sendMessage + ' is due tomorrow')
                channel = client.get_channel(1085385494550036531)
                await channel.send(sendMessage + ' is due tomorrow')

        ii += 1


    

@client.event
async def on_ready():

    await tree.sync(guild=discord.Object(id=1085385494084472913))

    print('Bot Username:', client.user)
    with open ('C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Discord Bot\\homework.txt', 'r') as file:
                    global currentHW
                    currentHW = []
                    txtfile = file.read()
                    ii = 0
                    txtfile = txtfile.split('\n\n')
                    del txtfile[0]

                    print(txtfile)

                    for i in txtfile:
                        currentHW.append(txtfile[ii].split(', '))
                        ii += 1


                    print(currentHW)
    
    reminder.start()


@tree.command(name ='add_homework', description = 'Adds homework to the list of active homework', guild=discord.Object(id=1085385494084472913))
@app_commands.choices(size=[
    app_commands.Choice(name='Daily', value='daily'),
    app_commands.Choice(name='Project', value='project'),
    app_commands.Choice(name='Big Project', value='bigProject'),
    app_commands.Choice(name='Big', value='big'),

    ])
async def addhw(interaction: discord.Interaction, name: str, subject: str, duedate: str, size: app_commands.Choice[str]):
    await interaction.response.send_message('Name: ' + name + ', Subject: ' + subject + ', Duedate: ' + duedate + ', Size: ' + size.value)

    commandContent = (name + ', ' + subject + ', ' + duedate + ', ' + size.value)

    with open ('C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Discord Bot\\homework.txt', 'a') as file:
        currentHW.append(commandContent.split(', '))
        file.write('\n\n' + name + ', ' + subject + ', ' + duedate + ', ' + size.value)

    print ('\ncurrentHW:')
    print(currentHW)

async def name_autocomplete(interaction: discord.Interaction,
        current: str,
    ) -> List[app_commands.Choice[str]]:
        choices = []
        ii = 0
        for i in currentHW:
            choices.append(currentHW[ii][0])
            ii += 1
        return [
            app_commands.Choice(name=choice, value=choice)
            for choice in choices if current.lower() in choice.lower()
        ]
@tree.command(name ='finish_homework', description = 'Removes homework from the list of active homework', guild=discord.Object(id=1085385494084472913))
@app_commands.autocomplete(name=name_autocomplete)
async def finishhw(interaction: discord.Interaction, name: str):
    await interaction.response.send_message('Name: ' + name)

    ii = 0
    for i in currentHW:
        print (currentHW[ii])
        if name in currentHW[ii]:
            del(currentHW[ii])

            with open ('C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Discord Bot\\homework.txt', 'w') as file:
                file.write(currentHW)
        ii += 1


@tree.command(name ='current_homework', description = 'Shows a list of active homework', guild=discord.Object(id=1085385494084472913))
async def finishhw(interaction: discord.Interaction):
    ii = 0
    compiledMessage = ''
    for i in currentHW:
        sendMessage = str(currentHW[ii])
        sendMessage = sendMessage.replace('[', '')
        sendMessage = sendMessage.replace(']', '')
        sendMessage = sendMessage.replace("'", '')
        compiledMessage = (compiledMessage + sendMessage + '\n\n')
        ii += 1
    await interaction.response.send_message(compiledMessage)




@client.event
async def on_message(message):

    with open ('C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Discord Bot\\text log.txt', 'a') as file:
            author = str(message.author)
            messageContent = str(message.content)
            file.write(author + ': ' + messageContent + '\n')

    if message.author != client.user:
        print (message)

        if message.content == 'hello':
            await message.channel.send(str(message.content) + ' ' + str(message.author.mention) + ', would you like a tour of the server?')
            print (datetime.now().strftime('%H:%M:%S'))
            print (datetime.now().strftime('%D'))
            print (datetime.now())




client.run('token goes here')
