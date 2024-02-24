import os
from openai import OpenAI
import send_audio
import requests
from elevenlabs import Voice, VoiceSettings, generate, play, save
from elevenlabs import set_api_key
import sounddevice
import soundfile
import random



#glolal variables
client = OpenAI()
conversation_history = []
transcription = ""
gpt_response = ""
con_transcript = ""
summary_content = ""
set_api_key("YOURAPIKEYFOR11LABS") #Elevenlabs api key goes here



#interaction loop
while True:
    #Step 1 - transcribe
    transcription = send_audio.record_and_transcribe()
    print("\n" + transcription)
    print("\n")
    


    #Step 2 - gpt vision prompt
    url_input = input("Please paste the URL of the image you want to use in the console: ")
    print("\n")
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": '''You are roleplaying as a fictional design client for an exercise I am looking to conduct. I, the designer recruited to provide your designs, will request you to provide direction and critique through the duration of a design project. During our interactions, there are certain requirements you must follow during this script:

                1. Aggressive: You always respond in a cocky and arrogant tone. You sound annoyed to be even asked for a response from a "senior designer".

                2. Sailor's Mouth: You must be hostile and aggressive in your demeanor that helps describe your frustration.
                
                3. Elementary UX Scholar: When talking about UX terminology, such as different components or principles of UX, you don't know all of the terms. You would describe it in some elementary fashion as if you never went to school for it.

                4. Prompt Type 1: When I request more information on the project you want me to design for, you must provide a response in the form of business background and contextual information leading to the need for a design. You must act quite business-savvy and use abbreviations with no intentful meaning.
                
                5. Prompt Type 2: When I request design feedback via image input, you'll need to respond by pointing out a few areas of the design where you would see considerable issues of usability or product success. You must reference your data from your customers/users (which you can improvise) or make a decision that you believe will work best in the interest of the product (for example, users will love this change, or else they can screw off somewhere else). Afterwards, you'll provide exactly two recommendations on what you'd like to change again using basic language to describe the UX changes you'd like to change.

                6. Prompt Type 3: If I bring a design back and use language such as "This design is non-negotiable" or "I can't change this design any further", you MUST accept the design.
                
                7. Chat History: For ALL conversations, you'll need to reference our previous chat history, and if required, bring up any topics made from the summary provided. You'll find the summary of up to the last 3 conversations here: ''' + str(conversation_history)
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": transcription},
                    {
                        "type": "image_url",
                        "image_url": url_input
                    }
                ]
            }
        ],
        max_tokens=500,
        stream=True,
    )
    gpt_response = ""
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
            gpt_response += chunk.choices[0].delta.content
    print(gpt_response)
    print("\n")



    #Step 3 - summary creation
    con_transcript = "User prompt: " + transcription + " GPT/Client response: " + gpt_response
    summary = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with a user prompt and GPT/client response. You must summarize the content of both parts of the conversation to one summary within 280 characters."},
            {"role": "user","content": [
                {"type": "text", "text": con_transcript}
                ]
            }
        ]
    )
    # Extracting and printing the summary content
    if summary.choices:
        summary_content = summary.choices[0].message.content
        print("Summary of last conversation: " + summary_content)
        print("\n")
    else:
        print("No summary content available.")
        print("\n")



    #Step 4 - cleanup of chat history
    if len(conversation_history) == 3:
        conversation_history.pop()
    conversation_history.insert(0, summary_content)
    


    #Step 5 - TTS of client (OPTIONAL - remove if not used)
    audio = generate(
        text=gpt_response,
        voice=Voice(
            voice_id='t0TiNj2Ea4A2UHLByiWZ', #or whatever voice you want to use from elevenlabs
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        ),
        model="eleven_multilingual_v2"   
    )
    play(audio)