#ENDCRYPT 4-B51-R2
#Ema Pex
#Created 03/03/16
#Updated 17/05/18

#Imports libraries needed for the program to work
import random, time, binascii, configparser, os
config=configparser.ConfigParser()

if not os.path.isdir("Data"):
    os.makedirs("Data")

clrLog=("\n"*125) #clears the screen

#Sets up the character list (UTF-8)
alphaLetters=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")      #Alphabet plus the space
alphaNumbers=("0123456789")                                                 #Numbers 0 - 9
alphaPunct  =("!\"(\\./:;'),?¡¸´¯¨")                                        #Collection of punctuation
alphaSymbols=("#£$%&*+-<=>@[]^_`{|}~¬¦€«»®©§¥¤¢ª¹²³º¼½¾·°±µ¶×Þß÷þÿ")        #Collection of symbols
alphaAccents=("ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝàáâãäåæçèéêëìíîïðñòóôöøùúûüý")  #Collection of accented letters

#Puts them all into one string
alpha = '{}{}{}{}{}'.format(alphaLetters, alphaNumbers, alphaPunct, alphaSymbols, alphaAccents)

#FUNCTIONS
#Generates the key
def keygen():
    global genkey
    genkey=""                       #Blank variable to store the generated key
    alphaMutate=alpha               #New variable for string mutation
    while alphaMutate!="":                      #Checks that the mutated string isn't empty
        r=random.choice(alphaMutate)            #Chooses a character from the mutation string
        genkey+=r                               #Adds it to the generated key
        alphaMutate=alphaMutate.replace(r,"")   #Mutates the string, removing the character

#Toggles Dev Mode
def devModeToggle():
    global shortDelay
    global decAutoDelay4
    global decAutoDelay1
    global decAutoDelay2
    if devMode=="on":
        shortDelay=0
        decAutoDelay1=0
        decAutoDelay2=0
        decAutoDelay4=0
    elif devMode=="off":
        shortDelay=3
        decAutoDelay1=0.75
        decAutoDelay2=1.33
        decAutoDelay4=0.55

#ENDCRYPT_History Toggle
def historyToggle():
    global tExport
    if endcryptHistory=="on":
        tExport="ENDCRYPT.ini has been overwritten and ENDCRYPT_History.ini has been saved."
    else:
        tExport="ENDCRYPT.ini has been overwritten."

#Writes the encryption to file
def writeEncryption():
    config=configparser.ConfigParser()
    print(tExport)
    if endcryptHistory=="on":
        print("Make sure to clear out your ENDCRYPT_History from time to time!")

    #Saves to 'ENDCRYPT_History.ini', a list of all encryptions ran
    if endcryptHistory=="on":
        with open('Data//ENDCRYPT_History.ini', 'a') as configfile:
            config["KEYS"] = {"Text": ench,
                              "EncryptKey": keyh,
                              "AlphaKey": alpkeyh,
                              "MasterKey": newkeyh}
            config.write(configfile)

    #Saves to 'ENDCRYPT.ini', only containing the most recent (for sharing).
    with open('Data//ENDCRYPT.ini', 'w') as configfile:     
        config["KEYS"] = {"Text": ench,
                          "EncryptKey": keyh,
                          "AlphaKey": alpkeyh,
                          "MasterKey": newkeyh}
        config.write(configfile)

#Generate default config file
def generateConfig():
    global readTime
    global filePathEntry
    global endcryptHistory
    global alwaysExport
    global encryptionPath
    global autoFileEncryption
    global devMode
    devMode="off"
    alwaysExport="on"
    autoFileEncryption="prompt"
    filePathEntry="on"
    encryptionPath="file.txt"
    readTime=3.5
    endcryptHistory="off"
    writeConfig()

#Saves the config file
def writeConfig():
    config = configparser.ConfigParser()
    with open('Data//ENDCRYPT_Config.ini', 'w') as configfile:
        config["SETTINGS"] = {"devMode": devMode,
                              "alwaysExport": alwaysExport,
                              "autoFileEncryption": autoFileEncryption,
                              "filePathEntry": filePathEntry,
                              "persistentFilePath": encryptionPath,
                              "readtime": readTime,
                              "endcryptHistory": endcryptHistory}
        config.write(configfile)

#Config validation
while True:
    if not os.path.exists("Data//ENDCRYPT_Config.ini"):
        generateConfig()
        break
    
    try:
        config.read("Data//ENDCRYPT_Config.ini")
    except configparser.MissingSectionHeaderError:
        print("ERROR: ENDCRYPT_Config.ini is missing its header.\nRestoring to default settings...")
        generateConfig()
        time.sleep(3)
        
    try:
        config.get("SETTINGS","alwaysexport")
        config.get("SETTINGS","endcrypthistory")
        config.get("SETTINGS","devmode")
        config.get("SETTINGS","filepathentry")
        config.get("SETTINGS","persistentfilepath")
        config.get("SETTINGS","autofileencryption")
        config.get("SETTINGS","readtime")
    except configparser.NoSectionError:
        break
    
    except configparser.NoOptionError:
        print('ERROR: ENDCRYPT_Config.ini is missing data.\nRestoring to default settings...')
        generateConfig()
        time.sleep(3)
        break
    
    alwaysExport=config.get("SETTINGS", "alwaysexport")
    endcryptHistory=config.get("SETTINGS", "endcrypthistory")
    devMode=config.get("SETTINGS", "devmode")
    filePathEntry=config.get("SETTINGS", "filepathentry")
    encryptionPath=config.get("SETTINGS", "persistentfilepath")
    autoFileEncryption=config.get("SETTINGS", "autofileencryption")
    readTime=float(config.get("SETTINGS", "readtime"))
    break

#MAIN
devModeToggle()
historyToggle()
while True:
    print(clrLog)
    
    #introductory message
    mode=str(input("\nWelcome to ENDCRYPT!\n    1)Encryption\n    2)Decryption\n    3)Options\nPress ENTER to exit.\n\n>")).lower()

    #ENCRYPTION
    if mode=="1":
        while True:
            print(clrLog)
            if autoFileEncryption=="on":
                encmode="2"
            elif autoFileEncryption=="prompt":
                encmode=str(input("Which encryption mode do you want to use?\n    1)Manual\n    2)Auto-File Encryption\n\n>"))
            elif autoFileEncryption=="off":
                encmode="1"
                
            keygen()    #Generates an encryption key
            key=genkey
            keyb=key.encode("utf-8")  #Converts the key to hex
            keyb=binascii.hexlify(keyb)
            keyh=keyb.decode("utf-8")
            enc=("")
            
            keygen()    #Generates an 'alpha' key
            alpkey=genkey
            alpkeyb=alpkey.encode("utf-8")    #Converts the key to hex
            alpkeyb=binascii.hexlify(alpkeyb)
            alpkeyh=alpkeyb.decode("utf-8")

            #Creates a 'translation' using the 'alpha' and encryption key, basically a cypher
            encryption=str.maketrans(alpkey,key)
            print(clrLog)

            #Manual text entry
            if encmode=="1":
                mes=str(input("Enter your message:\n>"))

            #AFE validation
            elif encmode=="2":
                fileNotFound=False
                if filePathEntry=="on":
                    while True:
                        print(clrLog)
                        if fileNotFound==True:
                            print("ERROR: File not found.")
                        encryptionPath=str(input("Enter the file path:\n>"))
                        try:
                            f=open(encryptionPath, 'r')
                        except FileNotFoundError:
                            fileNotFound=True
                        fileNotFound=False
                        break
                f=open(encryptionPath, 'r')
                mes=f.read()
                f.close()
            else:
                break
            
            enc=mes.translate(encryption)       #Runs the cypher over the inputted text
            encb=enc.encode("utf-8")            #Converts the encrypted text
            enchex=binascii.hexlify(encb)
            ench=enchex.decode("utf-8")
            
            keygen()                            #Generates the 'Master Key'
            newkey=genkey
            newkeyt=str.maketrans(alpha,newkey) #Creates a master translation
            newkeyh=newkey.encode("utf-8")
            newkeyh=binascii.hexlify(newkeyh)
            newkeyh=newkeyh.decode("utf-8")
            
            keyh=keyh.translate(newkeyt)        #Translates the keys using the master key
            keyb=keyh.encode("utf-8")           #Encrypts into hex... once again!
            keyb=binascii.hexlify(keyb)
            keyh=keyb.decode("utf-8")
            
            alpkeyh=alpkeyh.translate(newkeyt)
            alpkeyb=alpkeyh.encode("utf-8")     #Converts the key to hex
            alpkeyb=binascii.hexlify(alpkeyb)
            alpkeyh=alpkeyb.decode("utf-8")
            
            ench=ench.translate(newkeyt)
            encb=ench.encode("utf-8")
            encb=binascii.hexlify(encb)
            ench=encb.decode("utf-8")

            #SAVING
            if alwaysExport=="off":
                saveEncryption=input("Save encryption to file?\n  1)No\n  2)Yes\n\n>")
                
                if saveEncryption=="2": #Saves the encrypted text, encryption key, and 'alpha' key
                    writeEncryption()
                    
                if saveEncryption not in["2"]:  #Doesn't save the encryption and displays it instead.
                    print("Text: \n\n{!s}\nEncryption Key: \n\n{!s}\nAlpha Key: \n\n{!s}".format(ench,keyh,alpkeyh))
                    time.sleep(10)  #Delay the reset so the user can copy the information
                    
            elif alwaysExport=="on":
                writeEncryption()
                
            time.sleep(shortDelay)
            break

    #DECRYPTION
    if mode=="2":
        print(clrLog)
        decryptMode="2"

        #AUTO
        if decryptMode=="2":
            if not os.path.exists("Data//ENDCRYPT.ini"):
                print(clrLog)
                print("ERROR: ENDCRYPT.ini doesn't exist.")
                time.sleep(3)
                
            else:
                try:
                    config.read('Data//ENDCRYPT.ini')
                except configparser.MissingSectionHeaderError:
                    print("ERROR: ENDCRYPT.ini is missing its header.\nAdd [KEYS] to the top of the file.")
                    time.sleep(5)
                    break
                
                while True:
                    try:
                        config.get("KEYS","encryptkey")
                        config.get("KEYS","masterkey")
                        config.get("KEYS","alphakey")
                        config.get("KEYS","text")
                    except configparser.NoSectionError:
                        break
                    
                    except configparser.NoOptionError:
                        print("ERROR: ENDCRYPT.ini is missing data.\nCheck that it contains four keys:\nmasterkey\nalphakey\nencryptkey\ntext")
                        time.sleep(7.5)
                        break
                    
                    decryption=config.get("KEYS","encryptkey")  #Gets the encryption key
                    decryption=binascii.unhexlify(decryption)   #Converts the decrypted key from hex
                    decryption=decryption.decode("utf-8")
                    alpkey=config.get("KEYS","alphakey")        #Gets the alpha key
                    alpkey=binascii.unhexlify(alpkey)           #Converts the decrypted key from hex
                    alpkey=alpkey.decode("utf-8")
                    
                    masterKey=config.get("KEYS","masterkey")    #Gets the master key
                    masterKey=binascii.unhexlify(masterKey)     #Converts the masterkey from hex
                    masterKey=masterKey.decode("utf-8")
                    masterTrans=str.maketrans(masterKey, alpha) #Reconstructs the master translation
                    
                    decryptionT=decryption.translate(masterTrans)   #Decrypts the encryption key
                    alpkeyT=alpkey.translate(masterTrans)       #Decrypts the alpha key
                    
                    alpkeyT=binascii.unhexlify(alpkeyT)         #Converts the decrypted key from hex
                    alpkeyT=alpkeyT.decode("utf-8")
                    decryptionT=binascii.unhexlify(decryptionT) #Converts the decrypted key from hex
                    decryptionT=decryptionT.decode("utf-8")
                    
                    decryption=str.maketrans(decryptionT, alpkeyT)  #Reconstructs the cypher
                    
                    mesh=config.get("KEYS","text")  #Imports the message
                    mesh=binascii.unhexlify(mesh)   #Converts it from hex...
                    mesh=mesh.decode("utf-8")       #...to UTF-8
                    mesT=mesh.translate(masterTrans)
                    mesb=binascii.unhexlify(mesT)   #Converts it from hex...
                    mes=mesb.decode("utf-8")        #...to UTF-8
                    
                    dec=mes.translate(decryption)   #Runs the encrypted text back through the cypher

                    #Adjust display time based on message length
                    decDelay=len(dec)+1     #Gets message length
                    decDelay/=5             #Sets to average
                    decDelay/=readTime      #time to read
                    if decDelay<1:
                        decDelay=2          #Make sure the delay is at least 2 seconds
                    
                    print(clrLog)
                    print("{!s}".format(dec))   #Prints the decrypted text
                    
                    if readTime==0.1:
                        decHold=str(input(">"))
                    else:
                        time.sleep(decDelay)    #Delays the program reset by decDelay seconds
                    break

    #OPTIONS
    if mode in ['3']:
        while True:
            print(clrLog)
            print("Available options:\n    1)Encryption Export:        ON/OFF\n    2)ENDCRYPT_History.ini:     ON/OFF\n    3)Fast Mode:                ON/OFF\n    4)Auto-File Encryption:     AUTO/PROMPT/NEVER\n    5)Auto-File Encryption:     FILE PATH ENTRY\n    6)Read Speed:               OFF/SLOW/MED/FAST\nPress ENTER to go back.\nType 'ABOUT' to view the credits\n")
            opt=str(input(">")).lower()

            #Always Export
            if opt=="1":
                print(clrLog)
                print("Always export the files after encrypting? If no, will prompt to export.\n  1)Yes\n  2)No\n")
                exportOpt=str(input(">")).lower()
                if exportOpt == "1":
                    alwaysExport = 'on'
                    print("Now exporting without a prompt.")
                    time.sleep(3)
                elif exportOpt=="2":
                    alwaysExport="off"
                    print("Now prompting when trying to export encryptions.")
                    time.sleep(3)
                writeConfig()

            #ENDCRYPT_History.ini
            if opt=="2":
                print(clrLog)
                print("Export to 'ENDCRYPT_History.ini' when encrypting?\n    1)Yes\n    2)No\n")
                historyExport=str(input(">")).lower()
                if historyExport=="1":
                    endcryptHistory="on"
                    historyToggle()
                    print("Exporting to 'ENDCRYPT_History.ini'.")
                    time.sleep(3)
                elif historyExport=="2":
                    endcryptHistory="off"
                    historyToggle()
                    print("No longer exporting to 'ENDCRYPT_History.ini'.")
                    time.sleep(3)
                writeConfig()

            #Dev Mode
            if opt=="3":
                print(clrLog)
                if devMode=="off":
                    print("Fast Mode is now ON.\nAll delays (except for important ones) are now turned off.")
                    devMode="on"
                    devModeToggle()
                    time.sleep(3)
                elif devMode=="on":
                    print("Fast Mode is now OFF.\nAll delays have been turned back on.")
                    devMode="off"
                    devModeToggle()
                    time.sleep(3)
                writeConfig()

            #AFE
            if opt=="4":
                print(clrLog)
                print("Encrypt from a file, rather than a text input?\n    1)Always\n    2)Prompt\n    3)Never\n")
                afe=str(input(">")).lower()
                if afe=="1":
                    autoFileEncryption="on"
                    print("Auto-File encryption is now the default setting.\nENDCRYPT will read from '{}' unless File-Path Entry is turned on.".format(encryptionPath))
                elif afe=="2":
                    autoFileEncryption="prompt"
                    print("Auto-File encryption is an option when encrypting.\nENDCRYPT will read from '{}' unless File-Path Entry is turned on.".format(encryptionPath))
                elif afe=="3":
                    autoFileEncryption="off"
                    print("Auto-File encryption is now turned off.\nENDCRYPT will never ask you to encrypt from a file.")
                writeConfig()
                time.sleep(3)

            #FPE
            if opt=="5":
                print(clrLog)
                print("Allow file-path entry while using Auto-File Encryption?\n    1)Yes\n    2)No\n    3)Persistent Path\n")
                fpe=str(input(">")).lower()
                if fpe=="1":
                    filePathEntry="on"
                    print("File path entry is now turned ON.\nMake sure you include '.txt' at the end of the file!")
                elif fpe=="2":
                    filePathEntry="off"
                    print("File path entry is now turned OFF.")
                elif fpe=="3":
                    filePathEntry="off"
                    print("Please enter a persistent file path:\n")
                    encryptionPath = str(input(">"))
                    print("Default path set to {}".format(encryptionPath))
                writeConfig()
                time.sleep(3)

            #Read Speed
            if opt=="6":
                readSpeed=""
                while readSpeed!="complete":
                    print(clrLog)
                    print("Adjust the delay before decrypted text goes back to the menu.\nChoose a speed to preview it.\n    1)Off\n    2)Slow\n    3)Medium\n    4)Fast\nPress ENTER to go back.")
                    readSpeed=str(input(">")).lower()
                    if readSpeed=="1":
                        readTime=0.1
                        dec="Read time has been turned off.\nPress ENTER to advance.\nUse this if you don't like the auto-return."
                    elif readSpeed=="2":
                        readTime=2
                        dec="This is an example of slow read time.\nUse this if you're a slow reader."
                    elif readSpeed=="3":
                        readTime=3.5
                        dec="This is an example of medium read time.\nThis is the default."
                    elif readSpeed=="4":
                        readTime=7.5
                        dec="This is an example of fast read time.\nThis will be too fast for some people."
                    elif readSpeed=="":
                        break
                    
                    decDelay=len(dec)+1
                    decDelay/=5
                    decDelay/=readTime
                    if decDelay < 1:
                        decDelay=2
                        
                    print(clrLog)
                    print(dec)
                    if readTime==0.1:
                        rsPause = str(input('>'))
                    elif readTime>0.2:
                        time.sleep(decDelay)    #Delays the program reset by decDelay seconds
                    
                    print(clrLog)
                    print("Use this option?\n    1)Yes\n    2)No\n")
                    readSpeed = str(input('>'))
                    if readSpeed=="1":
                        writeConfig()
                        print(clrLog)
                        print("Speed saved.")
                        time.sleep(3)
                        readSpeed="complete"
                    elif readSpeed=="2":
                        print(clrLog)
                        readSpeed = ""
                        print("Returning to choices.")
                        time.sleep(shortDelay)

            #Credits
            if opt=="about":
                print(clrLog)
                print("Program made by Ema Pex.")
                print("Tested by David Beecher, Jakk Johnson, Ryan Foy, and Eden Hamilton.")
                print("First released 03/03/16.")
                print("Current version released 17/05/18.")
                print("Version 4 (B51-R2).\n")
                print("Press ENTER to go back.\n")
                credback=str(input(">"))

            #Back to Menu
            if opt=="":
                break
    #EXIT
    if mode in[""]:
        break
