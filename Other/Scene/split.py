import Algorithmia

input = {
  "video": "https://www.youtube.com/watch?v=OMgIPnCnlbQ",
  "detector": "content"
}
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('media/SceneDetection/0.1.6')
print(algo.pipe(input).result)