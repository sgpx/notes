### Prerequisites

1. **Java Development Kit (JDK)**: Hive requires Java. You can install OpenJDK by following these steps:
   
   ```bash
   sudo apt update
   sudo apt install openjdk-8-jdk
   ```

   Verify the installation:
   
   ```bash
   java -version
   ```

   You should see output indicating that Java is installed.

2. **Hadoop**: Hive requires a functioning Hadoop installation. You can either install it manually or use a pre-built version.

### Step 1: Install Hadoop

Here’s a brief way of installing a standalone version of Hadoop.

1. **Download Hadoop**:

   ```bash
   wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
   ```

2. **Extract the package**:

   ```bash
   tar -xzf hadoop-3.3.1.tar.gz
   ```

3. **Move it to /usr/local**:

   ```bash
   sudo mv hadoop-3.3.1 /usr/local/hadoop
   ```

4. **Set Environment Variables**:

   Open `~/.bashrc` in your favorite text editor:

   ```bash
   nano ~/.bashrc
   ```

   Add the following lines at the end of the file:

   ```bash
   export HADOOP_HOME=/usr/local/hadoop
   export PATH=$PATH:$HADOOP_HOME/bin
   ```

   Save the file and make it effective:

   ```bash
   source ~/.bashrc
   ```

5. **Verify Hadoop Installation**:

   ```bash
   hadoop version
   ```

### Step 2: Install Apache Hive

1. **Download Hive**:

   ```bash
   wget https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
   ```

2. **Extract the package**:

   ```bash
   tar -xzvf apache-hive-3.1.2-bin.tar.gz
   ```

3. **Move it to /usr/local**:

   ```bash
   sudo mv apache-hive-3.1.2-bin /usr/local/hive
   ```

4. **Set Environment Variables for Hive**:

   Open `~/.bashrc` again:

   ```bash
   nano ~/.bashrc
   ```

   Add the following lines at the end of the file:

   ```bash
   export HIVE_HOME=/usr/local/hive
   export PATH=$PATH:$HIVE_HOME/bin
   ```

   Save the file and make it effective:

   ```bash
   source ~/.bashrc
   ```

5. **Verify Hive Installation**:

   ```bash
   hive --version
   ```

### Step 3: Configure Hive

1. **Create Hive Metastore Directory**:

   ```bash
   mkdir -p /usr/local/hive/metastore
   ```

2. **Create Hive Configuration File**:

   Create a file named `hive-site.xml` in the `${HIVE_HOME}/conf/` directory:

   ```bash
   cp /usr/local/hive/conf/hive-default.xml.template /usr/local/hive/conf/hive-site.xml
   ```

   Open `hive-site.xml` for editing:

   ```bash
   nano /usr/local/hive/conf/hive-site.xml
   ```

   Add the following configuration properties inside the `<configuration>` tags:

   ```xml
   <property>
       <name>javax.jdo.option.ConnectionURL</name>
       <value>jdbc:derby:;databaseName=metastore_db;create=true</value>
   </property>
   <property>
       <name>javax.jdo.option.ConnectionDriverName</name>
       <value>org.apache.derby.jdbc.EmbeddedDriver</value>
   </property>
   <property>
       <name>javax.jdo.option.ConnectionUserName</name>
       <value>APP</value>
   </property>
   <property>
       <name>javax.jdo.option.ConnectionPassword</name>
       <value></value>
   </property>
   ```

### Step 4: Start Hadoop

In a terminal, start the Hadoop services. Enter the following commands:

```bash
start-dfs.sh
start-yarn.sh
```

### Step 5: Launch Hive

You can start the Hive shell by executing:

```bash
hive
```

You should see a prompt like this, indicating that Hive is running:

```
Hive >
```

### Step 6: Run a Sample Query

You can create a sample table and run a simple query:

```sql
CREATE TABLE IF NOT EXISTS test_table (key STRING, value STRING);
INSERT INTO test_table VALUES ('1', 'one'), ('2', 'two');
SELECT * FROM test_table;
```

### Troubleshooting

If you encounter issues:

- Make sure that the Java and Hadoop binaries are correctly installed and configured.
- Verify that environment variables are correctly set.
- Check logs in the Hadoop and Hive directories for any errors.

This covers the basic installation and setup process to run Apache Hive on Ubuntu 22.04. If you need further functionality or configurations (like using other databases for the metastore), you can refer to the official documentation.
