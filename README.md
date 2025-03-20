# ENDCRYPT 4

### The Program
This program encrypts and decrypts text using a pretty simplistic method and has options for encrypting entire text files and automatically saving the output. It's exactly as feature complete as it needs to be while still being pretty basic, and if you want more information there's a file included called "info.txt" that was the original readme. The way it works should be pretty straight forward and easy to use (as easy and simple as a CLI *can* be, anyway).

### The Story
This program was originally written in 2016 when I was in school as a simple test to see if I could do it. A friend was messing with some libraries that handled text encryption and I said "I bet I could do that myself."

Well my original attempt was awful since I was still fairly new to coding at the time, being over 1000 lines long and only being able to handle the lowercase alphabet. It was very poorly thrown together and, while it did work, I wasn't really happy with it.

Fast forward a year and now I'm in college. I figured it'd be fun to pick ENDCRYPT back up again and see if I could improve the key generation from 1000 lines to something more manageable. Since I had more knowledge and experience I figured it couldn't be that hard, and within a few days I got it down to just 100 lines instead.

With that improvement out the way I felt like I could start adding other features to the program to make it more usable, which ended up leading to the creation of the menu that exists now and the concept of the "alpha key". In the first versions there were a few hardcoded alphabet layouts that it would map the generated key to for added randomness in the encryption, but with simpler code base I decided to replace the hardcoded alphabets with *another* key, effectively generating two keys and mapping one over the other to create the cipher.

A few months later I was thinking about ENDCRYPT again and started thinking about how I cut it down from 1000 lines to just 100. It must be possible to knock it down even more, right? That line of thinking brought me down the rabbit hole of simplification that brought the key generation algorithm to where it is today.

**Seven lines.**

The way the encryption actually works never really changed throughout all that time, just the methods for key generation and replacing the hardcoded alphabets with the alpha key (ENDCRYPT 4 also introduced the master key but that was primarily for further obfuscation and to make cracking it more annoying without the source code).

The program was finished up and given an update in mid 2018 to fix some crashing bugs, then distributed through a website that I have since shut down. Since the reach of that site and the original program was pretty small I've wanted to put it on GitHub for a long time, but there were some issues stopping me from doing so.

First of all I'd distributed the program using a name that I no longer associate with so that needed to be replaced, but the bigger issue is I actually *lost the source code*. I had a compiled version of the final build on a hard drive, but not the actual code itself.

How did this happen?

I'd saved the code on Cloud9 so I could easily access it between college and home, and I don't entirely remember what happened to be honest. I seem to remember there being some kind of service migration or something and I just ignored it, then by the time I wanted to log in to Cloud9 a few years later I simply couldn't.

With the code missing on a server I couldn't access that seemed to be it. The goal of archiving my work on ENDCRYPT 4 was over...

...if decompilation wasn't a thing.

Turns out it's surprisingly easy to reverse a program compiled with PyInstaller to turn it into a .pyc file, and it's also surprisingly easy to revert a .pyc file to a .py file. All the comments were missing, but luckily I had an earlier build of ENDCRYPT 4's code on hand to refer to.

While looking at the old code I also realised that the way I wrote code was absolutely disgusting and hard to look at, and the decompiled build had cleaned itself up somewhat and was surprisingly tolerable. In the interest of accurate archival, I replicated the way the original code was written. Sorry not sorry.

Because I had no comments to refer to for features added after the early build, I had to just make some up. They're probably not what the original comments said and the code may be structured slightly differently to how it was originally, but it's close enough at this point. I replaced the deadnames, recompiled, and here we are. Everything is how it was back in the day, warts and all.

That leaves us in the present, with one simple question: will ENDCRYPT be updated or get a fifth version?

No.
