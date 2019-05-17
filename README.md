<h1>write-up</h1>
<h4>the mossad 2019 CTF's first challenge</h4>
well' first we recieved a .apk file and a username.
I ran the file in an online emulator and fount it to be a mere username/password page.
Then I decompiled the .apk file and started looking threw the folder,
there I read threw the android manifenst, I was partcularly interested in the line that said:
"<application android:data="look for us on github.com" android:debuggable="true" android:icon="@mipmap/ic_launcher" android:label="LockSmither"...
So.... I did, and there I found the backend code of the server:
https://github.com/iwalk-locksmithers-app/server/blob/master/main.go
In it lie down a rather clear vulnarability:
<b>
for currentIndex < len(lock.Password) && currentIndex < len(loginData.Password) {
			if lock.Password[currentIndex] != loginData.Password[currentIndex] {
				break
			}
			//OG: securing against bruteforce attempts... ;-)
			time.Sleep(30 * time.Millisecond)
			currentIndex++
		}
    </b>
 if you look closely you might just notice that the step they are taking to avoid a brutforce is what makes bruteforce all that easier.
 what my script (brutefirce.py) does is it sends an http request to the sever with my seed(username) and every letter/digit
 (there was also a condition regarding the user agent) for the password and if its fits then the server runtime would extand by 30 miliseconds
 so I ran the script 32 times(when I was finally able to get it working...) and at the end got this pass:44d4129a07fd4be0b06e44f528f1f531
 and that link http://3d375032374147a7865753e4bbc92682.xyz/0ca14b2570c64a149ed9a44badfda2de which gave me the token and told me of my
 succes in challenge 1.
 
 This is my first writeup, hopefully I did'nt forget anything,
 hope you ennjoyed it!
 
