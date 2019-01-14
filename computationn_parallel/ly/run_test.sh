
export PYSPARK_DRIVER_PYTHON=/usr/bin/python

report_path=report
if [ ! -d ${report_path} ] ; then
    mkdir -p ${report_path}
fi

spark-submit \
    --num-executors 400 \
    --conf spark.dynamicAllocation.minExecutors=10 \
    --conf spark.dynamicAllocation.maxExecutors=1000 \
    --conf spark.driver.memory=10G \
    --executor-cores 3 \
    --executor-memory 12G \
    --conf spark.speculation=true \
    --conf spark.speculation.interval=5s \
    --conf spark.speculation.multiplier=10 \
    --queue root.celuemoxingbu_driver_service_score \
    --driver-memory 10g \
    --py-files markdown_report.py math_computation.py
