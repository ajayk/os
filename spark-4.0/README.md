# Apache Spark 4.0

This package provides Apache Spark 4.0.0.

## Notable changes in Spark 4.0.0

- **First release in the 4.x series**
- **Java**: Now requires Java 17 (dropped support for Java 8/11)
- **Scala**: Only supports Scala 2.13 (dropped support for Scala 2.12)
- **Python**: Requires Python 3.9+ (dropped support for Python 3.8)
- **SparkR**: Deprecated in 4.0.0

## Key Features

- Spark Connect improvements
- VARIANT data type support in Spark SQL
- Native plotting API in PySpark
- Arbitrary State API v2 in Structured Streaming

## Configuration Changes

- ANSI SQL mode is now enabled by default (`spark.sql.ansi.enabled`)
- Default table creation now uses `spark.sql.sources.default` instead of Hive
- Map key normalization changed for certain functions
- Default partition bytes size changed from `Long.MaxValue` to `128m`

## Patches

- `guava.patch`: Updates Guava dependencies to newer versions
- `mvn.patch`: Fixes Maven download URL for build process

## Compatibility Notes

This package has the following compatibility variants:

1. `spark-4.0-scala-2.13`: Main package with Scala 2.13 support
2. `spark-4.0-scala-2.12`: Compatibility package (deprecated in upstream, but included for compatibility)
3. `spark-4.0-scala-*-compat`: Compatibility packages for various deployment environments

## Dependency Versions

- Hadoop: 3.4.1 (Upgraded from 3.3.x in previous Spark)
- Scala: 2.13.16
- Guava: 33.2.1-jre (Upgraded from 14.0.1 in previous Spark)
- Netty: 4.1.119.Final
- Log4j: 2.24.3
- ZooKeeper: 3.9.3
- Jackson: 2.18.2
- Protobuf: 4.29.3

## Resources

- [Spark 4.0.0 Documentation](https://spark.apache.org/docs/4.0.0/)
- [Spark SQL Migration Guide](https://spark.apache.org/docs/4.0.0/sql-migration-guide.html)