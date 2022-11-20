import os


class PythonSpark:
    def __init__(self,packages=None, jars=None):
        
        options = ""
        if packages is not None:
            packages = ",".join(packages)
            options += f"--packages {packages}"
        if jars is not None:
            jars = ",".join(jars)
            if options != "":
                options += " "
            options += f"--jars {jars}"
        
        if options != "":
            os.environ["PYSPARK_SUBMIT_ARGS"] = f"{options} pyspark-shell"
        self.sc, self.spark, self.pyspark = self.__setup_spark_session()
    
    def __setup_spark_session(self, jars=None):
        from pyspark import SparkContext, SparkConf
        from pyspark.sql import SQLContext, SparkSession
        import pyspark

        conf = SparkConf().setAppName("")
        
        sc = SparkContext(conf=conf)
        spark = SparkSession.builder.appName('Demo_Graph').getOrCreate()
        if jars is not None:
            spark.sparkContext.addPyFile(",".join(jars))
        return sc, spark, pyspark

    def get_session(self):
        return self.sc, self.spark, self.pyspark