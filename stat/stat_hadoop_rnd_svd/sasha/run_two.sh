DIR1=/home/burak/Downloads/sasha/node1/
DIR2=/home/burak/Downloads/sasha/node2/
RESPONSE=tcp://localhost:5040
CONF=local2
# split ../A.dat -n l/2; mv xaa $DIR1/A.dat; mv xab $DIR2/A.dat
python proj.py $CONF -i A.dat -o Y.dat  -r $RESPONSE
# python ata.py $CONF -i Y.dat -o YtY.dat -r $RESPONSE
# cat $DIR1/YtY.dat $DIR2/YtY.dat > YtY.dat 
# sort YtY.dat > YtY_sorted.dat # sort the results by key
# python chol.py YtY_sorted.dat /tmp/R.dat
# python a_inv_r.py $CONF -i Y.dat -o Q.dat  -f /tmp/R.dat -r $RESPONSE
# python join.py $CONF -i A.dat,Q.dat -o AQ.dat -r $RESPONSE
# python atq.py $CONF -i AQ.dat -o BT.dat -r $RESPONSE
# cat $DIR1/BT.dat $DIR2/BT.dat > BT.dat 
# sort -h BT.dat > $DIR1/BT_sorted.dat	
# sort -h BT.dat > $DIR2/BT_sorted.dat	
# python ata.py $CONF -i BT_sorted.dat -o BTB.dat -r $RESPONSE
# cat $DIR1/BTB.dat $DIR2/BTB.dat > BTB.dat
# sort -h BTB.dat > $DIR1/BTB_sorted.dat
# sort -h BTB.dat > $DIR2/BTB_sorted.dat
# python chol.py $DIR1/BTB_sorted.dat /tmp/R_BT.dat
# python q_uhat.py $CONF -i Q.dat -o U_final.dat  -f /tmp/R_BT.dat -r $RESPONSE
# cat $DIR1/U_final.dat $DIR2/U_final.dat > /tmp/U_final.dat
