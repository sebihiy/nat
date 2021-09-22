#!/usr/bin/env bash

# Remove cookies

rm -f cookies.txt result.html message.txt

### Prefecture Essonne #########################################
### Choose Counter  for RDV  (There are 5 counters from A to E)#
### A: 23018                                                   #
### B: 23198                                                   #
### C: 23199                                                   #
### D: 23200                                                   #
### E: 23201                                                   #
################################################################
## mail template
TO="sebihiy@gmail.com"
echo "From: sebihiy@gmail.com" >> message.txt
echo "To: sebihiy@gmail.com" >> message.txt
echo "Subject: Alert RDV" >> message.txt

### Check the availability of RDV  in ALL Counters 


for counter in 23018 23198 23199 23200 23201; do 

case $counter in
  23018) Guichet=A;;
  23198) Guichet=B;;
  23199) Guichet=C;;
  23200) Guichet=D;;
  23201) Guichet=E
esac

codehttp=$(curl -XPOST -c cookies.txt -o  /dev/null  -s -w "%{http_code}\n" -H "Content-Type: application/x-www-form-urlencoded" \
     -d "planning=${counter}&nextButton=Etape+suivante"  \
     https://www.essonne.gouv.fr/booking/create/23014/1)
#echo "codehttp: " $codehttp

if [ "$codehttp" = "502" ]; then
    echo "502 Bad Gateway." 
    #ssmtp -vvv $TO < message.txt
    exit 1
fi


### Check 
codehttp=$(curl -o  /dev/null  -s -w "%{http_code}\n" 'http://www.essonne.gouv.fr/booking/create/23014/2' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,ar;q=0.6' \
  -b cookies.txt \
  --compressed \
  --insecure)

#echo "codehttp: " $codehttp

if [ "$codehttp" = "502" ]; then
    echo "502 Bad Gateway." 
    #ssmtp -vvv $TO < message.txt
    exit 1
fi

  
  
curl  'https://www.essonne.gouv.fr/booking/create/23014/2' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,ar;q=0.6' \
  -b cookies.txt \
  --compressed > result.html


grep -rin "502 Bad Gateway"  result.html > /dev/null 2>&1 

RDV=$?
if [ $RDV -eq 0 ]; then
	echo "502 Bad Gateway"  
	exit 1
else
	grep -rin "Il n'existe plus "  result.html > /dev/null 2>&1
	RDV=$?
        if [ $RDV -eq 0 ]; then
	   echo "Guichet =>  $Guichet" 
           echo "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement" 
        else 
           echo "Vite Vite des RDV sont disponibles sur le guichet :  $Guichet"	>> message.txt
           ssmtp -vvv $TO < message.txt
       fi
fi
done 


#ssmtp -vvv $TO < message.txt
