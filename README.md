# Cluster overview

| Application     | URL                                      | Description                                                |
| --------------- | ---------------------------------------- | ---------------------------------------------------------- |
| JupyterLab      | [localhost:8888](http://localhost:8888/) | Cluster interface with built-in Jupyter notebooks          |
| Spark Driver    | [localhost:4040](http://localhost:4040/) | Spark Driver web ui                                        |
| Spark Master    | [localhost:8080](http://localhost:8080/) | Spark Master node                                          |
| Spark Worker I  | [localhost:8081](http://localhost:8081/) | Spark Worker node |
| Spark Worker II | [localhost:8082](http://localhost:8082/) | Spark Worker node |

# Prerequisites

 - [Docker](https://docs.docker.com/get-docker/)
 - [Docker Compose](https://docs.docker.com/compose/install/)

### Build Images

1. clone the repository;
2. `cd` to directory;

```bash
cd build
```

3. Change [build.yml](build/build.yml) and [docker compose](build/docker-compose.yml) for build versions;
4. Permission for building bash script;

```bash
chmod +x build.sh
```
5. Build up the images;
```bash
./build.sh
```
6. Start the cluster;

```bash
docker-compose up
```
or running cluster in background
```bash
docker-compose up -d
```

7. Run [localhost:8888](http://localhost:8888/);


## <a name="tech-stack"></a>Tech Stack

| Spark | Hadoop | Scala   | [Scala Kernel](https://almond.sh/) | Python | [Python Kernel](https://ipython.org/) | R     | [R Kernel](https://irkernel.github.io/) |Apache Spark   | JupyterLab     |
| ----- | ------ | ------- | ---------------------------------- | ------ | ------------------------------------- | ----- | --------------------------------------- | ----- |----- | 
| 3.x   | 3.2    | 2.12.10 | 0.10.9                             | 3.7.3  | 7.19.0                                 | 3.5.2 | 1.1.1                                   | 2.4.0(4) | 3.0.0 | 
| 2.x   | 2.7    | 2.11.12 | 0.6.0                              | 3.7.3  | 7.19.0                                 | 3.5.2 | 1.1.1                                   |2.1.4  | 3.0.0          | 
