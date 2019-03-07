#!/bin/sh

source ~/.bashrc

# check inputs
if [ $# -ne 3 ] ; then
    echo "the input parameters error."
    exit 1
fi

# parse inputs
city_id=$1
start_date=$2
stop_date=$3

# default folders
local_root_dir=`pwd`

hadoop_root="/user/bigdata_driver_ecosys_test/tangxu/data"

# output
hadoop_output=${hadoop_root}/${city_id}/${start_date}-${stop_date}
local_output=${local_root_dir}/datatemp/${city_id}/${start_date}-${stop_date}

local_temp=${local_root_dir}/datatemp/${city_id}

if [ ! -d "${local_temp}" ]; then
  mkdir ${local_temp}
fi

#mkdir -p ${local_output}

# build
#mvn clean package

# print parameters
echo pid=$$
echo hadoop_output=${hadoop_output}
echo city_id=${city_id}
echo date_window=${start_date}-${stop_date}

sleep 3

hadoop fs -rm -r ${hadoop_output}

time_spark_start=`date +%s`

spark-submit -v \
    --archives hdfs://DClusterNmg4/user/driver_ecosys/uprice_bin/common/lib64-485.tgz \
    --jars tools/xgboost4j-spark-0.7-jar-with-dependencies.jar \
    --master yarn-client \
    --class main.scala.WordCountMain \
    --queue root.celuemoxingbu_driver_ecosys \
    --conf "spark.dynamicAllocation.minExecutors=100" \
    --conf "spark.dynamicAllocation.maxExecutors=2000" \
    --conf spark.yarn.executor.memoryOverhead=4096 \
    --conf "spark.executor.cores=6" \
    --conf spark.executor.memory=10g \
     ./target/get_online_subsidy-1.0.jar ${city_id} ${start_date} ${stop_date} ${hadoop_output}

echo "${hadoop_output}/hour_subsidy"

hdfs dfs -cat ${hadoop_output}/hour_subsidy/* >${local_output}_hour_subsidy.csv

time_spark_stop=`date +%s`

echo Time: $((${time_spark_stop} - ${time_spark_start}))

#hadoop fs -touchz "${hadoop_output}/_SUCCESS"

