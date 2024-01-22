echo "pkill START"
echo "running pkill paft"
pkill paft
echo "running pkill python3"
pkill python3
echo "running pkill chrom"
pkill chrom
echo "pkill COMPLETE"

echo "RESTARTING PAFT START"
cd /home/veeru
/usr/bin/bash /home/veeru/startpaft.sh
echo "RESTARTING PAFT DONE"
