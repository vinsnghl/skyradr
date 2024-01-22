from datetime import datetime
import pyaudio
import wave
import audioop
import math
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
#import tweepy
import os
from datetime import date


##### BOX_CODE FUNCTION START - checks if plane in box / screenshot / write to HTML / JSON ######

def box_code(sdriver,dbvalue, currenttime,output_json,output_html):
    global firstoutputjsonrow
    input_aircraft_json = open('/run/dump1090-fa/aircraft.json')
    data = json.load(input_aircraft_json)
    input_aircraft_json.close()
    a = str(datetime.now())
    print("Start time", a, flush=True)
    for i in data['aircraft']:
        att = datetime.now()
        if (i.get('lat') is not None) and (i.get('lon') is not None):
            print(att, i['hex'], i['lat'], i['lon'], dbvalue , 
            i['alt_baro'] if 'alt_baro' in i else 'NA', 
            i['alt_geom'] if 'alt_geom' in i else 'NA', 
            i['baro_rate'] if 'baro_rate' in i else 'NA', 
            i['geom_rate'] if 'geom_rate' in i else 'NA' , 
            i['category'] if 'category' in i else 'NA',flush=True)
            icaocode = i['hex']
            if (i['lat'] > 37.703535) and (i['lon'] > -121.849880) and (i['lat'] < 37.731262) and (i['lon'] < -121.822907) and (i['alt_baro'] < 4000):
            #if (i['lat'] > 37.420754) and (i['lon'] > -122.053210) and (i['lat'] < 37.9) and (i['lon'] < -121.71699861410525):   ## LARGE BOX FOR TESTING
                print('IN THE BOX: ',att, i['hex'], i['lat'], i['lon'], dbvalue , 
                i['alt_baro'] if 'alt_baro' in i else 'NA', 
                i['alt_geom'] if 'alt_geom' in i else 'NA', 
                i['baro_rate'] if 'baro_rate' in i else 'NA', 
                i['geom_rate'] if 'geom_rate' in i else 'NA' , 
                i['category'] if 'category' in i else 'NA',flush=True)
            
                i["timestamp"] = att.strftime("%Y-%m-%d %H:%M:%S")
                i["decibel"] = dbvalue
                timest = str(i["timestamp"])
                imgfilename = todayoutputdir + "screenshot_"+icaocode+"_" + timest.replace(" ", "_") + ".png"
                imgfilename_forhtmlsrc = "screenshot_"+icaocode+"_" + timest.replace(" ", "_") + ".png"

                print("Start JSON write", str(datetime.now()), flush=True)
                print(i, flush=True)                
                output_json.writelines(str(i) + ',' + '\n')
                output_json.flush() 
                print("End JSON write", str(datetime.now()), flush=True)

                print("Start HTML write", str(datetime.now()), flush=True)

                testhtml = """
                <tr>
                    <th style="padding:10px">Airplane Data</th>
                    <th style="padding:10px">Flight Path</th> 
                </tr>
                <tr>
                    <td style="width:20% ; padding:20px">
                        ICAO = {0} <br/>
                        AIRCRAFT CATEGORY = {1} <br/>
                        ALITITUDE = {2} <br/>
                        VERT. RATE = {3} <br/>
                        SPEED = {4} <br/>
                        LAT = {5} <br/>
                        LON = {6} <br/>
                        TIME = {7} <br/>
                        NOISE (DECIBEL) = {8} <br/>
                    </td>
                    <td width="80%" align="center" style="padding:20px">
                        <img src="{9}"  alt="flight path">
                    </td>
                </tr>                
                """
                testhtml = testhtml.format(
                    str(i["hex"]) if "hex" in i else " ", 
                    str(i["category"]) if "category" in i else " ", 
                    str(i["alt_baro"]) if "alt_baro" in i else " ", 
                    str(i["baro_rate"]) if "baro_rate" in i else " " ,
                    str(i["gs"]) if "gs" in i else " ", 
                    str(i["lat"]) if "lat" in i else " ", 
                    str(i["lon"]) if "lon" in i else " ",
                    str(i["timestamp"]) if "timestamp" in i else " ", 
                    str(i["decibel"]) if "decibel" in i else " ",
                    imgfilename_forhtmlsrc)

                print(testhtml, flush=True)                
                output_html.writelines(testhtml + '\n')
                output_html.flush() 

                print("End HTML write", str(datetime.now()), flush=True)

                # FETCH ADSB MAP PAGE URL
                #print("Start screenshot GET time", str(datetime.now()), flush=True)
                #sdriver.get('https://globe.adsbexchange.com/?icao='+icaocode+'&lat=37.719308818039025&lon=-121.84063212768908&hideSidebar&hideButtons&zoom=12')
                #sdriver.get('https://globe.adsbexchange.com/?icao='+icaocode+'&lat=37.719308818039025&lon=-121.84063212768908&hideSidebar&hideButtons&zoom=12')
                #sdriver.get('https://globe.adsbexchange.com?lat=37.719308818039025&lon=-121.84063212768908&hideSidebar&hideButtons&zoom=12')
                #print("End screenshot GET time", str(datetime.now()), flush=True)

                # SAVE ADSB MAP PAGE
                #print("Start screenshot SAVE time", str(datetime.now()), flush=True)
                #sdriver.get_screenshot_as_file(imgfilename)
                #print("End screenshot SAVE time", str(datetime.now()), flush=True)
                

                

    # Closing file
    # PRINT TIME
    at = str(datetime.now())
    print("End time", at, flush=True)

##### BOX_CODE FUNCTION END ######



###### MAIN PROGRAM START #######
###### MAIN PROGRAM START #######
###### MAIN PROGRAM START #######
###### MAIN PROGRAM START #######


###### CHECK DATE AND CREATE NEW DATE BASED FOLDER & FILES ONLY IF NEEDED #######
todaysdate = date.today().strftime("%m%d%Y")
todayoutputdir = "./output/" + todaysdate + "/"
print("OUTPUT FOLDER: " + todayoutputdir)
isExist = os.path.exists(todayoutputdir)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(todayoutputdir)
    print("The new directory is created! : " + todayoutputdir)

###### OPEN OUTPUT JSON AND HTML FILES IN APPEND MODE - DONT WANT TO LOSE WHATS THERE ALREADY FOR THAT DAY #######
output_aircraftinbox_json = open(todayoutputdir + "aircraftinbox.json", 'a')
output_aircraftinbox_html = open(todayoutputdir + "aircraftinbox.html", 'a')
output_alldaynoisetrack_json = open(todayoutputdir + "alldaynoisetrack.json", 'a')

######### AUDIO RECORDING INIT #########
chunk = 1000  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 48000  # Record at 44100 samples per second
seconds = 30000000
secondstorec = 5
filename = "output2.wav"
p = pyaudio.PyAudio()  # Create an interface to PortAudio
print('Recording')
print('detals :', p.get_default_input_device_info())
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True, input_device_index = 1)
frames = []  # Initialize array to store frames


######### SCREENSHOT - DISPLAY INIT #########
print("Start display init", str(datetime.now()), flush=True)
display = Display(visible=0, size=(800, 800))
display.start()
print("End display init", str(datetime.now()), flush=True)                
# browser is Chromium instead of Chrome

######### SCREENSHOT - SELENIUM / CHROME BROWSER INIT ###########
print("Start selenium init", str(datetime.now()), flush=True)
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Firefox()
driver.set_page_load_timeout(300)
print("End selenium init", str(datetime.now()), flush=True)



######### MAIN LOOP - RUNS ALMOST FOREVER ############

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):

    ###### CHECK DATE AND CREATE NEW DATE BASED FOLDER & FILES ONLY IF NEEDED #######
    todaysdate = date.today().strftime("%m%d%Y")
    todayoutputdir = "./output/" + todaysdate + "/"
    print("OUTPUT FOLDER: " + todayoutputdir)
    isExist = os.path.exists(todayoutputdir)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(todayoutputdir)
        print("The new directory is created! : " + todayoutputdir)
        output_aircraftinbox_json = open(todayoutputdir + "aircraftinbox.json", 'a')    # Do only IF new folder needed / not every few seconds
        output_aircraftinbox_html = open(todayoutputdir + "aircraftinbox.html", 'a')    # Do only IF new folder needed / not every few seconds   
        output_alldaynoisetrack_json = open(todayoutputdir + "alldaynoisetrack.json", 'a')  # Do only IF new folder needed / not every few seconds


    ###### RECORD AUDIO FROM MIC FOR APPROX 1 SEC AND COMPUTE DECIBEL #######
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    
    #data = stream.read(chunk, exception_on_overflow=False)

    rmsval = 0
    maxrmsval = 0
    for j in range(0, int(fs / chunk * secondstorec)):
        data = stream.read(chunk, exception_on_overflow=False)
        rmsval = audioop.rms(data, 2)
        if maxrmsval < rmsval:
            maxrmsval = rmsval
        

    #print("RMS : ",rmsval)
    #frames.append(data)
    #20 * Math.Log10(rms)
    decibel = 20 * math.log10(maxrmsval)
    #print(' ',int(decibel))
    for i in range(int(decibel)):
        print('#', end='', flush=True)
    print('AUDIO STATS : ', int(decibel), int(maxrmsval), current_time, flush=True)
    
    ### PRINT RAW DATA START
    #result = []
    #sm = 0
    #for index in range(0, len(data), 2):
    #    value = int.from_bytes(data[index:index+2], 'big')
    #    result.append(value)
    #    sm = sm + ((value)**2)
        #print("AUDIO VAL: " , value , sm)
    #print(result)
    #print('AVERAGE : ' , sum(result) / len(result))
    #print('DECIBEL FROM AVG : ' , 20 * math.log10(sum(result) / len(result)))
    #print('RMS : ' , math.sqrt(sm/len(result)))
    #print('DECIBEL FROM RMS : ' , 20 * math.log10(math.sqrt(sm/len(result))))        
    ### PRINT RAW DATA END

    
    ######## ALL DAY AUDIO TRACK WRITE TO JSON #########
    audiorec = {}
    audiorec["timestamp"] = now.strftime("%Y-%m-%d %H:%M:%S")
    audiorec["decibel"] = str(round(decibel))
    print("AUDIO REC JSON write : ",str(audiorec), flush=True)
    output_alldaynoisetrack_json.writelines(str(audiorec) + ',' + '\n')
    output_alldaynoisetrack_json.flush() 

    ######## CALL BOX_CODE - MOST WORK DONE IN THAT FUNCTION - SCREENSHOT / WRITING TO HTML / JSON FILES #####
    box_code(driver,str(round(decibel)), current_time,output_aircraftinbox_json,output_aircraftinbox_html)
    ######## SLEEP ADDED TO ALLOW PLABES TO EXIT BOX - NOT THE BEST METHOD #####
    #sleep(7)


######### CLEANUP AND EXIT !! ############
# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

output_aircraftinbox_json.close()
output_aircraftinbox_html.close()
output_alldaynoisetrack_json.close()
# Stop and close the AUDIO stream
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()
driver.quit()

print('Finished recording')

