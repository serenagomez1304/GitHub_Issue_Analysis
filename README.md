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
    Silhouette coefficient: 0.70
    Inertia:6.982816198802295e-05
    Silhouette values:
        Cluster 1: Size:2 | Avg:0.97 | Min:0.97 | Max: 0.97
        Cluster 4: Size:3 | Avg:0.86 | Min:0.84 | Max: 0.89
        Cluster 0: Size:4 | Avg:0.85 | Min:0.82 | Max: 0.88
        Cluster 3: Size:6 | Avg:0.70 | Min:0.47 | Max: 0.82
        Cluster 6: Size:4 | Avg:0.68 | Min:0.59 | Max: 0.75
        Cluster 5: Size:2 | Avg:0.68 | Min:0.64 | Max: 0.71
        Cluster 8: Size:2 | Avg:0.60 | Min:0.57 | Max: 0.62
        Cluster 2: Size:1 | Avg:0.00 | Min:0.00 | Max: 0.00
        Cluster 7: Size:1 | Avg:0.00 | Min:0.00 | Max: 0.00
    (MiniBatchKMeans(batch_size=10, n_clusters=9), array([0, 1, 4, 0, 2, 3, 0, 3, 3, 4, 6, 8, 0, 5, 6, 6, 1, 7, 4, 5, 3, 6,
        8, 3, 3]))
  ```