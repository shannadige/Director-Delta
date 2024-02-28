<h1>Director Delta</h1>

Director Delta can provide feedback on your designs, giving its honest and brutal critique before providing recommendations for improvement. Director Delta also serves as a challenge generator, providing you with a business context and problem that can be solved through the use of digital design.

Watch the video below, or get a full read on my website: <a href="https://www.shannadige.com/rabbithole/director-delta">shannadige.com</a>

[![image of person and cat on a laptop, looking shocked at an AI demanding to make the logo bigger](https://assets-global.website-files.com/5f41aabba3e6792b793258e8/65da55f60e3d6b113753d4cf_dirdelta-youtube.png)](https://www.youtube.com/watch?v=L0DxuSzwEnE)

<a href="https://chat.openai.com/g/g-fY3QZ6cu5-director-delta">Currently, this experience is available as a GPT for Pro users of ChatGPT.</a> So if you're looking to still experience this and save $20 for another subscription, you will certainly enjoy the coding adventure that I also took!
<br><br>
<h2>Setup</h2>
If you're running the script, there are a few requirements you should have so that things run smoothly:
<ul>
<li>Python 3.7 or greater, installed on a Windows or Mac machine.</li>
<li>Install all packages using pip listed in the Python files. (Best if you google this)</li>
<li>A code interpreter. I used VS Code during my demo and highly recommend it.</li>
<li>An OpenAI API key, and some familiarity with OpenAI's platform. Setup an account here.</li>
<li>An ElevenLabs key and a configured voice on VoiceLibrary. Read more here.</li>
<li>A functioning microphone input.</li>
<li>A public URL that has an image to your design (or placeholder image if you are not reviewing a design).</li>
</ul>
Running the master script (client-command.py) will take you through a workflow in order to interact with Director Delta and get your desired response. You'll be able to continue the context in a given session based on previously-stored conversations.
<br>
<img src="https://uploads-ssl.webflow.com/5f41aabba3e6792b793258e8/65d966d5cebc6c98857dec1b_flowchart.png" alt="Flowchart of an AI program"> 

<h2>Disclaimers</h2>
Some disclaimers I need to disclose regarding this script:
<ul>
<li>Download and use at your own risk, follow data compliance rules as you normally would, and read your signed agreements with 3rd party services (Python, OpenAI, ElevenLabs, etc.) - <b>me not responsible for anything!</b></li>
<li>You are free to use, abuse, and modify this script however you'd like, for personal or commercial use.</li>
<li>Yes, I understand the code is not perfect. Feel free to tinker around and send me a merge request if you want to see improvements.</li>
<li>The script does not confidently provide or reflect an expert UX opinion, and should not be reliably used for professional business decisions.</li>
<li>The "script" refers to two scripts - one called "client-command.py" which is the primary script, and "send_audio.py" as a sister script for transcribing microphone input.</li>
<li>In the demo video, I edited the recording across two identical conversations, in order to build the content. Additionally, there are some moments where the GPT incorrectly calls out user needs and business context, that can always be remedied in prompting the tool.</li>
<li>Transcribing text uses the Python repo of Whisper, OpenAI's speech recognition model. It's an amazing and pretty nimble technology, read more here.</li>
<li>System prompts for Director Delta can be modified as needed - they are what keep Director Delta in character.</li>
<li>On average each call of this script cost me <$0.02. We used "gpt-4-vision-preview" to get image recognition capabilities, and in its current state is pretty expensive in comparison to "gpt-3.5-turbo."</li>
<li>Summarizing conversations is currently with a ceiling of 3 conversations max to save on token spend, but you can always increase or decrease this number (see Step 4 in the script).</li>
<li>ElevenLabs is a totally optional augmentation of this code, you can delete it if you feel it entirely unnecessary (which it definitely is, but funny if you find the weirdest voice).</li>
