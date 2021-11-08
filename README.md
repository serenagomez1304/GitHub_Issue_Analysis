# GitHub Issue Analysis

### Prerequisites
* Run
  > $ pip install -r requirements.txt
* Download and unzip [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g)

### How to run the code
* Setup the input data
  * Download the github issues into ./data/issues folder
  * Place one issue text document per file with the following format:
    ```
    title:
    <Raspberry Pi 4 aarch64: ModuleNotFoundError: No module named 'numpy.random.bit_generator' #14541>

    user:
    <kaoh>

    status:
    <open>

    labels:
    <Build issues
    defect
    scipy.stats>

    description:
    <I'm using the NLU framework Rasa using TensorFlow which is relying on scipy. I have no issues running the code on a amd64 platform, but I'm using a Raspberry Pi 4 aarch64 architecture, where I hit the problem:>
    ```
* Place `GoogleNews-vectors-negative300.bin` file in the ./model folder
* Run src/main.py
* Expected ouput
  ```
    For n_clusters = 9
    Silhouette coefficient: 0.56
    Inertia:0.00015649956294795149
    Silhouette values:
        Cluster 5: Size:3 | Avg:0.85 | Min:0.81 | Max: 0.89
        Cluster 2: Size:3 | Avg:0.76 | Min:0.69 | Max: 0.82
        Cluster 3: Size:4 | Avg:0.67 | Min:0.35 | Max: 0.78
        Cluster 4: Size:4 | Avg:0.64 | Min:0.26 | Max: 0.79
        Cluster 0: Size:4 | Avg:0.60 | Min:0.10 | Max: 0.79
        Cluster 6: Size:4 | Avg:0.39 | Min:0.20 | Max: 0.57
        Cluster 1: Size:1 | Avg:0.00 | Min:0.00 | Max: 0.00
        Cluster 7: Size:1 | Avg:0.00 | Min:0.00 | Max: 0.00
        Cluster 8: Size:1 | Avg:0.00 | Min:0.00 | Max: 0.00
    (MiniBatchKMeans(batch_size=10, n_clusters=9), array([4, 3, 8, 4, 3, 5, 6, 4, 6, 7, 0, 5, 0, 2, 0, 3, 3, 2, 1, 2, 4, 6,
           5, 0, 6]))
  ```
