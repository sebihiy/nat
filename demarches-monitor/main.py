import requests
import re
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

URL = "https://www.val-de-marne.gouv.fr/booking/create/4963/1"
DiscordURL = ""

def main():
  firstTry = True
  appointment = []
  while True:
    print("Monitoring...")
    r = requests.session()
    r.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Content-Type': 'text/html'
    })
    out = r.get(URL)
    if out.status_code != 200:
      print("Erreur, retyring...")
    else:
      body = out.text
      # regex to find all the links
      links = re.findall(r'<label for=\"planning.+?\">(.+?)<\/label><\/p>', body)
      if firstTry:
        appointment = links
        firstTry = False
      elif (testResults(links, appointment) or len(appointment) != len(links)):
        ## Send notification
        sendNotification(appointment)
        appointment = links
       

    sleep(5) # sleep for 5 seconds

# Test all elements in list to check if appointments have changed
def testResults(listTests, appointment):
    for i in range(0, len(listTests)):
      print(appointment[i] != listTests[i])
      if (appointment[i] != listTests[i]):
        return True
    return False

# Send notification to discord webhook
def sendNotification(appointment):
  print("Nouvelle Dates Disponible !")
  webhook = DiscordWebhook(
    url = DiscordURL,
    username = "Nouvelles Dates Disponible !",
    rate_limit_retry = True,
    content = '@everyone'
    )
  
  desc = ""
  for i in range(0, len(appointment)):
    a = ""
    try:
      a = appointment[i].split(" - g")
      desc += "\n**g" + a[1] + "**"
    except:
       a = appointment[i]
    
  embed = DiscordEmbed(
    title = 'Nouvelle Dates Disponible! :white_check_mark:',
    url = 'https://www.val-de-marne.gouv.fr/booking/create/4963/1',
    description= desc, color=000000,
    )
  embed.set_timestamp()
  webhook.add_embed(embed)
  response = webhook.execute()
  print(response)

main()
