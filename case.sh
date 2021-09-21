
for counter in 23018 23198 23199 23200 23201; do
case $counter in
  23018) Guichet=A;;
  23198) Guichet=B;;
  23199) Guichet=C;;
  23200) Guichet=D;;
  23201) Guichet=E	  
esac

echo "Guichet : " $Guichet
done
