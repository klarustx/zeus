export HADOOP_HEAPSIZE=2048
export HADOOP_CLIENT_OPTS="-Xmx2048m"

date=$1
if [ -z ${date} ]; then
    date=`date -d yesterday +%Y%m%d`
fi

spark-submit    --driver-memory 12g \
    --executor-memory 12g \
    --executor-cores 1 \
    --queue root.celuemoxingbu_driver_service_score \
    --conf "spark.dynamicAllocation.minExecutors=100" \
    --conf "spark.dynamicAllocation.maxExecutors=400" \
    --conf "spark.yarn.executor.memoryOverhead=3072" \
    --conf "spark.default.parallelism=10000" \
    utils.py 
