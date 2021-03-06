# Spark Hands On Training
# Databricks CE Cloud Practice
# Raul Arrabales / Conscious-Robots.com 

# Load text lines into an RDD
rdd1 = sc.textFile("/FileStore/tables/2ndixk251466511975346/quijote.txt") 

# Nested wordcount:
wordcounts = rdd1.map( lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower()) \
        .flatMap(lambda x: x.split()) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x,y:x+y) \
        .map(lambda x:(x[1],x[0])) \
        .sortByKey(False)
        
# Check Results
wordcounts.take(5)

# Step by step (explain each step)

rdd1 = sc.textFile("/FileStore/tables/2ndixk251466511975346/quijote.txt")
rdd1.take(15)

rdd2 = rdd1.map( lambda x: x.replace('.',' ').replace('-',' ').lower())
rdd2.take(10)

rdd3 = rdd2.flatMap(lambda x: x.split())
rdd3.count()

rdd4 = rdd3.map(lambda x: (x, 1))
rdd4.take(15)

rdd5 = rdd4.reduceByKey(lambda x,y:x+y)
rdd5.count()

rdd6 = rdd5.map(lambda x:(x[1],x[0]))
rdd6.take(10)

rdd7 = rdd6.sortByKey(False)
rdd7.take(100)
display(rdd7.take(4)) 

