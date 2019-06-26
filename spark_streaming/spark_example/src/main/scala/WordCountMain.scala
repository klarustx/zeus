import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.sql.functions.lit
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.{SparkConf, SparkContext}

def PassengerflagSimu(spark: SparkSession, city_list: String, sday: String, eday: String): DataFrame = {
  import spark.implicits._
  val sql_string =
    s"""
       |        select
       |            *
       |        from
       |           tablename
       |
       |        where
       |            concat(year,month,day) between '$sday' and '$eday'
       |            and city_id = '$city_list'
       """.stripMargin
  val passenger_flag_simu = spark.sql(sql_string)

  return passenger_flag_simu

}

object WordCountMain {

  def main(args: Array[String]): Unit = {


    val city_id = args(0)
    val begin_date = args(1)
    val end_date = args(2)
    //hadoop_output is params file path
    val hadoop_output = args(3)

    val spark = SparkSession.builder().enableHiveSupport().getOrCreate()
    val city_list = args(0)
    val begin_date = args(1)
    val end_date = args(2)
    //hadoop_output is params file path
    val hadoop_output = args(3)
    val model_file_path = args(4)
    val batch_types = args(5)
    val sample_table_path = args(6)
    val batch_type = batch_types.toInt
    val spark = BuildSparkSession()
    import spark.implicits._

    val conf = new SparkConf().setAppName("wordcount")
    val sc = new SparkContext(conf)

    val conf = new SparkConf().setAppName("wordcount")
    val sc = new SparkContext(conf)

    val input = sc.textFile("")

    val lines = input.flatMap(line => line.split(" "))
    val count = lines.map(word => (word, 1)).reduceByKey { case (x, y) => x + y }

    val output = count.saveAsTextFile("/home/cjj/testfile")

}
